# python-chatGPT

## Development

### 1. Register with openai to creat an API key for your application.
> https://platform.openai.com/

### 2. Create and update local .env
``` Bash
> touch .env
> echo "OPENAI_API_KEY=YOUR_OPENAI_API_KEY" >> .env
```

### 3. Setup virtual env and install dependencies
``` Bash
> python3.9 -m venv venv
> source ./venv/bin/activate
> pip install -r requirements.txt

