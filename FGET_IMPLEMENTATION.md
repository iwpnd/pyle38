# FGET Command Implementation

This document summarizes the implementation of the FGET command support for the pyle38 Tile38 Python client.

## Overview

The FGET command retrieves the value of a specific field for a given ID within a key in Tile38.

**Tile38 Command Syntax:**
```
FGET key id field
```

## Implementation Details

### 1. Command Enum (`src/pyle38/client.py`)
- Added `FGET = "FGET"` to the `Command` enum

### 2. Response Model (`src/pyle38/responses.py`)
- Created `FgetResponse` class:
  ```python
  class FgetResponse(JSONResponse):
      value: int | float | str | None = None
  ```
- Returns the field value as an int, float, string, or None
- Returns `None` when the field doesn't exist (determined by FEXISTS check)
- Uses FEXISTS internally to verify field existence before returning the value

### 3. Command Implementation (`src/pyle38/commands/fget.py`)
- Created `Fget` class extending `Executable`
- Implements fluent interface with methods:
  - `key(str)`: Set the collection key
  - `id(str)`: Set the object ID
  - `field(str)`: Set the field name to retrieve
  - `compile()`: Compiles the command for Tile38
  - `exec()`: Executes the command with FEXISTS check and returns `FgetResponse`
- The `exec()` method:
  1. First calls FEXISTS to check if the field exists
  2. Then calls FGET to get the field value
  3. Returns None if FEXISTS indicates the field doesn't exist
  4. Returns the actual value if FEXISTS indicates the field exists

### 4. Client Integration (`src/pyle38/follower.py`)
- Added `fget()` method to the `Follower` class
- Returns a `Fget` command builder instance
- Method signature:
  ```python
  def fget(self, key: str, oid: str, field: str) -> Fget
  ```

## Usage Examples

### Basic Usage
```python
from pyle38 import Tile38

tile38 = Tile38("redis://localhost:9851")

# Set an object with fields
await tile38.set("fleet", "truck1").fields({
    "speed": 90,
    "driver": "John"
}).point(52.25, 13.37).exec()

# Get a field value
response = await tile38.fget("fleet", "truck1", "speed").exec()
print(response.value)  # Output: 90
```

### With FSET
```python
# Set a field using FSET
await tile38.fset("fleet", "truck1", {"speed": 120}).exec()

# Retrieve the updated field value
response = await tile38.fget("fleet", "truck1", "speed").exec()
print(response.value)  # Output: 120
```

### Non-existent Field
```python
# When field doesn't exist, returns None
response = await tile38.fget("fleet", "truck1", "cargo").exec()
print(response.value)  # Output: None
```

### Field Set to Zero
```python
# Note: Tile38's FEXISTS returns False for fields set to 0
# So FGET will also return None for such fields
await tile38.fset("fleet", "truck1", {"count": 0}).exec()
response = await tile38.fget("fleet", "truck1", "count").exec()
print(response.value)  # Output: None (FEXISTS returns False)
```

## Testing

### Test Coverage (`tests/test_command_fget.py`)
1. **test_command_fget_compile**: Verifies command compilation
2. **test_command_fget**: Tests retrieving numeric field values
3. **test_command_fget_string_value**: Tests retrieving string field values
4. **test_command_fget_nonexistent_field**: Tests behavior with non-existent fields (returns None)
5. **test_command_fget_after_fset**: Tests FGET after FSET operations
6. **test_command_fget_field_set_to_zero**: Tests that fields set to 0 return None

All tests pass successfully! ✅

## Files Modified/Created

### Created:
- `src/pyle38/commands/fget.py` - FGET command implementation
- `tests/test_command_fget.py` - Comprehensive test suite

### Modified:
- `src/pyle38/client.py` - Added FGET to Command enum
- `src/pyle38/responses.py` - Added FgetResponse class
- `src/pyle38/follower.py` - Added fget() method and import

## Compatibility

- Follows the existing command pattern in pyle38
- Compatible with Tile38 1.36.2 (tested)
- Works with both Leader and Follower instances (via inheritance)
- Supports all field value types: int, float, string

## Related Commands

- **FSET**: Sets field values (write operation)
- **FEXISTS**: Checks if a field exists
- **GET**: Retrieves entire objects with optional WITHFIELDS

## Notes

- FGET is a read-only operation, implemented in the `Follower` class
- Uses FEXISTS internally to determine if a field exists before returning the value
- Returns `None` if FEXISTS indicates the field doesn't exist
- Returns the actual field value (including 0) if FEXISTS indicates the field exists
- **Important**: Tile38's FEXISTS returns False for fields set to 0, so FGET will return None for such fields
- Raises an error if the key or ID doesn't exist in Tile38
- The response follows the standard Tile38 JSON format with `ok` and `elapsed` fields

## Tile38 Semantics for Zero Values

In Tile38, FEXISTS treats fields set to 0 as non-existent:
- `FSET fleet truck1 count 0` → Sets field "count" to 0
- `FEXISTS fleet truck1 count` → Returns False (treats 0 as non-existent)
- `FGET fleet truck1 count` (raw) → Returns 0
- `pyle38 FGET fleet truck1 count` → Returns None (because FEXISTS returns False)

This behavior is based on Tile38's FEXISTS command, which considers 0-valued fields as non-existent.

