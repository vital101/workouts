Workouts
========

Workouts is a self-hosted workout tracking service.

### License

Workouts uses GNU GENERAL PUBLIC LICENSE Version 3. See the `LICENSE` file for details.

### Local Development Setup

1. Install [PyEnv](https://github.com/pyenv/pyenv#installation)
2. Install the version of Python listed in the `.python-version` file.
3. Create a virtual environment: `python3 -m venv venv`
4. Activate: `source venv/bin/activate`
5. Install dependencies: `pip install -r requirements.txt`

### Installing a new dependency

1. `pip install my-dep`
2. `pip freeze > requirements.txt`
3. Add the dependency to `requirements_base.txt`

### Upgrading Dependencies

1. Blow away your virtual environment `rm -rf venv`
2. Delete `requirements.txt`
3. `pip install -r requirements_base.txt`
4. `pip freeze > requirements.txt`