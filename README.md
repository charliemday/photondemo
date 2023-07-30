## PhotonDemo

This is a demo of the Photon framework for deploying LLMs into production.

### Installation

```
pip install photondemo
```

### Getting Started

#### Example

`llms/openai.py`

```
from photon import Photon
import openai

# Think of us as a high level wrapper around your LLM modules
openai = Photon(openai)
openai.photon_api_key = "YOUR PHOTON API KEY"

# We never save this 👇
openai.api_key = "YOUR API KEY"

```

`app.py`

```
from .llms.openai import openai

# Use your LLM as normal. Now every time you make an LLM request
# in your application it will be logged

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": prompt},
        {"role": "user", "content": content},
    ],
    temperature=0,
    max_tokens=500,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0,
    functions=functions,
    function_call={"name": "convert_to_json"},
)

```

## Developing Locally

Developing locally is easy. Just clone the repo and install the package in editable mode.

```
pip install -e <project-folder>
```

### Testing

Be sure to set your own OPENAI_API_KEY in `tests/conftest.py` before running tests.

```

```
