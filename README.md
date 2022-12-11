# Poet.AI
Bring your poetry to life, With AI

## Project
### What is the project?
- Poet.AI takes an audio recording of your poetry, transcribes it using AssemblyAI and then visually imagines scenes using Stable Diffusion 

### Try it out!
- Run pipenv shell and pipenv install
- Create a file `./mysite/app/secret_keys.py` that looks like this:
```
ASSEMBLY_AI_KEY="..."
REPLICATE_KEY="..."
GPT_KEY = "..."
```
- And it has the API keys for those services with proper setup
- Run python manage.py runserver, enjoy!
