# Aficionado

> An AWS Lambda HTTP Lib 🧙

An unopinionated library for AWS lambda. Useful when integrating with API gateway. Similar API to Flask, Bottle or Chalice.

## Getting Started

Install with pip

```
pip install aficionado
```

Create lambda handler file

```python
from aficionado import Aficionado

app = Aficionado()

@app.route('/')
def index():
  return 'hello world'

handler = app.handler
```

