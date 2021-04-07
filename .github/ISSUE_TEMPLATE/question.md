---
name: Question or Problem
about: Ask a question or ask about a problem
title: ""
labels: question
assignees: ""

---

### First check

* [ ] I added a very descriptive title to this issue.
* [ ] I used the GitHub search to find a similar issue and didn't find it.
* [ ] I searched the Pyle38 documentation.
* [ ] I already read and followed all the tutorial in the docs and didn't find an answer.
* [ ] I already checked if it is not related to Pyle38 but to [Pydantic](https://github.com/samuelcolvin/pydantic).
* [ ] I already checked if it is not related to FastAPI but to [aioredis](https://github.com/aio-libs/aioredis-py).


<!--

I'm asking all this because answering questions and solving problems in GitHub issues consumes a lot of time. I end up not being able to add new features, fix bugs, review Pull Requests, etc. as fast as I wish because I have to spend too much time handling issues.

-->

### Example

Here's a self-contained, [minimal, reproducible, example](https://stackoverflow.com/help/minimal-reproducible-example) with my use case:

<!-- Replace the code below with your own self-contained, minimal, reproducible, example, if I (or someone) can copy it, run it, and see it right away, there's a much higher chance I (or someone) will be able to help you -->

```Python
import asyncio
from pyle38.tile38 import Tile38


async def main():
    tile38 = Tile38(url="redis://localhost:9851")

    response = await tile38.ping()
    assert response.ping == "pong"


asyncio.run(main())
```

### Description

<!-- Replace the content below with your own problem, question, or error -->

* I ran my example code.
* It retuns an error.
* But I expected it to return assert correctly.

### Environment

* OS: [e.g. Linux / Windows / macOS]:
* FastAPI Version [e.g. 0.3.0]:

To know the Pyle38 version use:

```bash
python -c "import pyle38; print(pyle38.__version__)"
```

* Python version:

To know the Python version use:

```bash
python --version
```

### Additional context

<!-- Add any other context or screenshots about the question here. -->
