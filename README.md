# pyto
Python command tools

## How setup looks
```shell

pyto new

Package name: pip
Version [0.1.0]: 

Build tool:
    [*] setuptools
    [ ] poetry
    [ ] flit
    
Security tools [black]: 

Test tools [pytest]:

```

## Install
```
pipx install pyto
brew install pyto
pip install pyto
conda install pyto
```

## Config
```
# pyproject.toml

[tool.pyto.build]
...

[tool.pyto.security]
...
```

## CLI
```shell
❯ poetry run pyto          
Usage: pyto [OPTIONS] COMMAND [ARGS]...

  pyto - python command tools

Options:
  --version  Show the version and exit.
  --help     Show this message and exit.

Commands:
  add        Add new dependency
  adopt      Adopt the current setup of the package
  build      Build the project
  check      Perform static check of the target
  clean      Clean env from unused dependecies
  docs       Generate docs
  env        Create virtual evirment
  graph      Show dependecy graph of the project
  init       Initialize a new project in this directory
  install    Install all packages
  new        Create a new project in specified directory
  pin        Pin requirements
  publish    publish package
  run        Run scripts
  uninstall  Uninstall all packages
```

## Python Ecosystem

### Files
| Filename           | Used by       |
| ------------------ | ------------- |
| `setup.py`         |               |
| `setup.cfg`        |               |
| `Pipfile`          |               |
| `Pipfile.lock`     |               |
| `pyproject.toml`   |               |
| `MANIFEST.in`      |               |
| `.bandit`          |               |
| `requirements.txt` |               |
| `.flake8`          |               |
| `poetry.lock`      |               |
| `tox.ini`          |               |

### Scaffold
- [pyscaffold](https://github.com/pyscaffold/pyscaffold)
- [cookiecutter](https://github.com/cookiecutter/cookiecutter)
- [python-cli-tool-scaffold](https://github.com/dotanuki-labs/python-cli-tool-scaffold)
- [yehua](https://github.com/moremoban/yehua) - **@unmaintained**
- [carcass](https://github.com/MSAdministrator/carcass) - **@unmaintained**
- [scaffold-py](https://github.com/Aaronontheweb/scaffold-py) - **@unmaintained**
- [simplepkg](https://gitlab.com/b5n/simplepkg) - **@unmaintained**

### Build
- [setuptools](https://github.com/pypa/setuptools) **@pypa**
- [build](https://github.com/pypa/build) **@pypa**
- [packaging](https://github.com/pypa/packaging) **@pypa**
- [pipenv](https://pipenv.pypa.io/en/latest/) **@pypa**
- [pybuilder](https://github.com/pybuilder/pybuilder)
- [conda](https://docs.conda.io/en/latest/)
- [pip-tools](https://github.com/jazzband/pip-tools/)
- [bento](https://github.com/cournape/Bento) - **@unmaintained**
- [distutils](https://docs.python.org/3/library/distutils.html) - **@deprecated** in favor of setuptools

### Publish
- [twine](https://github.com/pypa/twine) **@pypa**
- [flit](https://github.com/pypa/flit) **@pypa**

### Dependecies
- [pip](https://github.com/pypa/pip) **@pypa @python2 @python3**
- [pipx](https://github.com/pypa/pipx) **@pypa**
- [poetry](https://github.com/python-poetry/poetry)
- [rez](https://github.com/AcademySoftwareFoundation/rez)
- [easy_install](https://setuptools.pypa.io/en/latest/deprecated/easy_install.html) - **@deprecated** in favor of setuptools

### Environment
- [venv](https://docs.python.org/3/library/venv.html) **@default @std @python3**
- [virtualenv](https://github.com/pypa/virtualenv) **@pypa @python2 @python3**
- [autoenv](https://github.com/hyperupcall/autoenv)
- [pyenv-virtualenv](https://github.com/pyenv/pyenv-virtualenv) **@extension** for pyenv
- [pyenv-virtualenvwrapper](https://github.com/pyenv/pyenv-virtualenvwrapper) **@unmaintained @extension** for pyenv
- [virtualenvwrapper](https://pypi.org/project/virtualenvwrapper/) **@unmaintained @extension** for virtualenv
- [pyvenv](https://docs.python.org/3/whatsnew/3.8.html#api-and-feature-removals) **@deprecated** in favor of venv

### Static Checks
#### Type Checker
- [mypy](https://github.com/python/mypy)
- [pytype](https://github.com/google/pytype)
- [pyright](https://github.com/microsoft/pyright)
- [pyre-check](https://github.com/facebook/pyre-check)
- [pyanalyze](https://github.com/quora/pyanalyze)

#### Security
- [bandit](https://github.com/PyCQA/bandit)
- [pyre](https://github.com/facebook/pyre-check)
- [safety](https://github.com/pyupio/safety)
- [spaghetti](https://github.com/pysal/spaghetti)
- [pyntch](https://www.unixuser.org/~euske/python/pyntch/index.html) **@umaintained @python2**
- [pyt](https://github.com/python-security/pyt) **@deprecated** in favor of pyre, bandit


### Linting
- [flake8](https://github.com/PyCQA/flake8)
- [pycodestyle](https://github.com/PyCQA/pycodestyle)
- [pyflakes](https://github.com/PyCQA/pyflakes)
- [mccabe](https://github.com/PyCQA/mccabe)
- [pydocstyle](https://github.com/PyCQA/pydocstyle/)
- [pylint](https://github.com/PyCQA/pylint)
- [pylama](https://github.com/klen/pylama)
- [radon](https://github.com/rubik/radon)
- [black](https://github.com/psf/black)
- [isort](https://pycqa.github.io/isort/)
- [autopep8](https://github.com/hhatto/autopep8)
- [pychecker](http://pychecker.sourceforge.net)
- [eradicate](https://github.com/myint/eradicate)
- [vulture](https://github.com/jendrikseipp/vulture)
- [yapf](https://github.com/google/yapf)
- [pylava](https://github.com/pylava/pylava) - **@unmaintained**
- [pep8ify](https://github.com/spulec/pep8ify) - **@unmaintained**

### Documentation
- [doxygen](https://www.doxygen.nl/index.html)
- [docutils](https://docutils.sourceforge.io)
- [sphinx](https://www.sphinx-doc.org/en/master/index.html)
- [autodoc](https://pypi.org/project/autodoc/)

### Test
- [nose](https://nose.readthedocs.io/en/latest/)
- [unittest](https://docs.python.org/3/library/unittest.html)
- [tox](https://tox.wiki/en/latest/)
- [hypothesis](https://hypothesis.readthedocs.io/en/latest/)
- [pytest](https://docs.pytest.org/en/latest/)
- [nox](https://github.com/wntrblm/nox)

### Package Version
- [bumpver](https://github.com/mbarkhau/bumpver)

### Python Versioning
- [pyenv](https://github.com/pyenv/pyenv)
- [pew](https://github.com/berdario/pew)
- [p](https://github.com/qw3rtman/p) - **@unmaintained**

### Python Implementation
- [cpython](https://github.com/python/cpython) - basic python we love
- [pypy](https://www.pypy.org) **@unsuported**
- [stackless](https://github.com/stackless-dev/stackless) **@unsuported**
- [micropython](https://micropython.org) **@unsuported**
- [rustpython](https://rustpython.github.io) **@unsuported**
- [anaconda](https://www.anaconda.com) **@unsuported**

## Read and Remove
- https://packaging.python.org/en/latest/key_projects/#virtualenv
- `pip install —editable .`
- [Sample Python Module](https://github.com/navdeep-G/samplemod)
- [Python Typing](https://github.com/typeddjango/awesome-python-typing)
- [Python Project Template](https://github.com/Kwpolska/python-project-template)
- [Awesome Python](https://github.com/vinta/awesome-python)
- [Testing & Packaging](https://hynek.me/articles/testing-packaging/)
- [Packaging a python library](https://blog.ionelmc.ro/2014/05/25/python-packaging/#the-structure)
- [Source distribution format](https://packaging.python.org/en/latest/specifications/source-distribution-format/)
- [PyPi publish package](https://realpython.com/pypi-publish-python-package/)

## Dev
https://click.palletsprojects.com/en/7.x/utils/
https://setuptools.readthedocs.io/en/latest/userguide/entry_point.html


Pyto abstracts over all tools you love to bring a uniform experince.

Pyto is a wrapper around other powerful tools that evolve and change, 
pyto in the same manner adapts to always use the most up-to-date convention by default.

Pyto can also be setup to used as simple project creation tool or something else.
Pyto know about all of the best tools for python and tries to use them, 
if we do not have support for some awsome tools, please open an issue.

Inspired by [cargo](https://doc.rust-lang.org/cargo/), [raco](https://docs.racket-lang.org/raco/) and [yeoman](https://yeoman.io).
Written in pure typed Python.

Whole Python ecosystem in one command line.

Even for simple projects we recommend using `pyto` as it structures all the code and makes sure all your project are consistent

Pyto works the same on all OS and has same commands.

Pyto always defaults to the newest PEPs to be shiny.
But you can ovveride behavioyr using `pyto.toml`

You live before Python 3.6? Do not have pyproject.toml? 
No problem `pyto` can be used with any setup even `distutils` !

# Info

### Project Structure

Strcuture of your project is very personal thing, however, as we are not only charming, but also very opninated manager, we decided to enforce standart project structure. You are probably already familier with it, as a large number of Python project are using same or very similar structure. Our was highly influnced by the following:

https://docs.python-guide.org/writing/structure/
https://github.com/navdeep-G/samplemod

## Todo
- Have autometic resolution of things like `setup.py` and only create them for versions that require it.
- Have generator declaration, so other can make other types of projects
- Generate git
- Generate `.gitignore`
- Generate License
