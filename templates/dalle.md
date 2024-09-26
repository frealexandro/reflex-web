---
title: DALL-E
description: "DALL-E is a Reflex app for generating images using OpenAI's API"
author: "Reflex"
image: "dalle.webp"
demo: "https://dalle.reflex.run/"
source: "https://github.com/reflex-dev/reflex"
meta: [
    {"name": "keywords", "content": ""},
]
---

In this example we create a simple app for generating images using OpenAI's API.

## Usage

To run this app locally, install Reflex and run:

```bash
git clone https://github.com/reflex-dev/reflex-examples.git
cd reflex-examples/ci-job
```

Set up your OpenAI API key:
```bash
export OPEN_AI_KEY=your-openai-api-key
```

Install the dependencies and run the app:

```bash
pip install -r requirements.txt
reflex run
```

