# A short tutorial for Cobrawap hands-on sessions

Cobrawap (Collaborative Brain Wave Analysis Pipeline) is an adaptable and reusable analysis pipeline for the multi-scale, multi-methodology analysis of cortical wave activity. The pipeline ingests data from heterogeneous sources of spatially organized neuronal activity, such as ECoG or calcium imaging recordings, as well as the outcome of numerical simulations. The pipeline returns statistical measures to quantify the dynamic wave-like activity patterns found in the data.

The open-source software for Cobrawap official releases is available [here](https://github.com/NeuralEnsemble/cobrawap), and fully documented [here](https://cobrawap.readthedocs.io).

## Cobrawap installation

### Creating a virtual environment for Cobrawap

First of all, it's necessary to have a working recent release of [python3](https://www.python.org/download/releases/3.0/), necessary for creating a virtual environment in which Cobrawap software and all its dependencies will be installed, without causing interferences with other python packages.

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

### Installing the latest official release

In order to install the latest official release of Cobrawap, let's activate the virtual environment created above and then run the following command:
```
pip install cobrawap
```
which will take care of fetching all the correct dependencies.

### Initial configuration

Once the installation process through pypi has finished, it is then possible to configure its global settings. To this aim, launch the command:
```
cobrawap init
```
and fill the requested fields with the desired paths for Cobrawap output and configuration files. At the same time, also the root of Cobrawap source code will be pointed at, and a list of Cobrawap stages will be created (refer to the [docs](https://cobrawap.readthedocs.io/en/latest/pipeline_stages.html) for more details). All these info will be collected and made further customizable at the path `~/.cobrawap/config`.

## Cobrawap configuration & run on an test imaging dataset

### Configuration

...

### Running

...
