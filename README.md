# A short tutorial for Cobrawap hands-on sessions

First of all, it's necessary to have a working recent release of [python3](https://www.python.org/download/releases/3.0/), necessary for creating a virtual environment in which Cobrawap software and all its dependencies will be installed, without causing interferencies with other python packages.

### Creating a virtual environment for Cobrawap

There are two possible options, [conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html) and [virtualenv](https://docs.python.org/3/library/venv.html). Be sure to have one of them installed and properly working.

Then, find below a minimal set of instructions to make them work for our hands-on:

|  How to...   |      conda      |  virtualenv  |
|----------|-------------|------|
| Create it |  ```conda create --name env_cobrawap python=3.9``` | ```python3 -m venv env_cobrawap``` |
| Activate it | ```conda activate env_cobrawap``` | ```source env_cobrawap/bin/activate``` |
| Deactivate it | ```conda deactivate``` | ```deactivate``` |

After having activated the virtual environment, it is possible to check its functionality by typing a simple command, as e.g.
```
pip list
```

### Installation

In order to install the latest official release of Cobrawap, let's activate the virtual environment created above and then run the following command:
```
pip install cobrawap
```
which will take care of fetching all the correct dependencies.

### Configuration

...

### Running

...
