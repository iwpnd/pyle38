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
- Returns 0 when the field doesn't exist (per Tile38 specification)

### 3. Command Implementation (`src/pyle38/commands/fget.py`)
- Created `Fget` class extending `Executable`
- Implements fluent interface with methods:
  - `key(str)`: Set the collection key
  - `id(str)`: Set the object ID
  - `field(str)`: Set the field name to retrieve
  - `compile()`: Compiles the command for Tile38
  - `exec()`: Executes the command and returns `FgetResponse`

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
# When field doesn't exist, returns 0
response = await tile38.fget("fleet", "truck1", "cargo").exec()
print(response.value)  # Output: 0
```

## Testing

### Test Coverage (`tests/test_command_fget.py`)
1. **test_command_fget_compile**: Verifies command compilation
2. **test_command_fget**: Tests retrieving numeric field values
3. **test_command_fget_string_value**: Tests retrieving string field values
4. **test_command_fget_nonexistent_field**: Tests behavior with non-existent fields
5. **test_command_fget_after_fset**: Tests FGET after FSET operations

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
- Returns `0` for non-existent fields (per Tile38 specification)
- Raises an error if the key or ID doesn't exist in Tile38
- The response follows the standard Tile38 JSON format with `ok` and `elapsed` fields

