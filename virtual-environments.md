# virtual environments in python (venv)

## what are they?
- a venv is a self-contained directory in which you can choose the Python version and packages for a specific project.

## why use them?
- avoid breaking projects because of version conflicts.
- keep projects organized: each project and its unique package/dependency versions.
- easy to share with other people (they can recreate your setup).

## how to create and use one?
```bash
# create a virtual environment
python -m venv [name]
# or for a specific Python version:
python3.12 -m venv [name]

# activate the venv:
# mac/linux:
source [name]/bin/activate
# windows:
[name]\Scripts\activate

# deactivate when done:
deactivate
```

## (optional) Save and reuse dependencies
```bash
pip freeze > requirements.txt    # save installed packages
pip install -r requirements.txt  # recreate environment later
```

## references:
- [venv docs](https://docs.python.org/3/library/venv.html)