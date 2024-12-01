# A short tutorial for Cobrawap hands-on sessions

Cobrawap (Collaborative Brain Wave Analysis Pipeline) is an adaptable and reusable analysis pipeline for the multi-scale, multi-methodology analysis of cortical wave activity. The pipeline ingests data from heterogeneous sources of spatially organized neuronal activity, such as ECoG or calcium imaging recordings, as well as the outcome of numerical simulations. The pipeline returns statistical measures to quantify the dynamic wave-like activity patterns found in the data.

The open-source software for Cobrawap official releases is available [here](https://github.com/NeuralEnsemble/cobrawap), and fully documented [here](https://cobrawap.readthedocs.io).

## Cobrawap installation

### Creating a virtual environment for Cobrawap

First of all, it's necessary to have a working recent release of [python3](https://www.python.org/download/releases/3.0/), necessary for creating a virtual environment in which Cobrawap software and all its dependencies will be installed, without causing interferences with other python packages.

There are two possible options, [conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html) and [virtualenv](https://docs.python.org/3/library/venv.html). Be sure to have one of them installed and properly working.

Then, find below a minimal set of instructions to make them work for our hands-on:

| How to... | conda | virtualenv |
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

## Configuring Cobrawap on a specific dataset

The fine-level configuration of Cobrawap clearly depends on the actual dataset to be analyzed (e.g. coming from imaging or ECoG experiments), as well as on the kind of analysis to perform. The modular structure of Cobrawap allows for a very deep customization of the processing, starting from the preliminar but necessary step of *data curation* (implemented in a dedicated *curation* block in the *data_entry* stage) and then going through the whole pipeline. For this reason, along with each test dataset present in this repository, also an analysis *profile* (i.e. a dedicated *curation_script* and a set of *configuration files*) is provided.

In order to donwload the test datasets and their related analysis profiles, choose your working directory and then type the command:
```
git clone https://github.com/APE-group/hands_on_cobrawap.git
```
which will download the whole content of this repository, storing it under the `hands_on_cobrawap` root folder.

### Configuration

Let's now choose a certain test dataset among those here available, calling it TEST_DATASET from now on.

In order to configure the pipeline for running on the chosen dataset with the related analysis profile, we have to modify the accordingly the `~/.cobrawap/config` settings file, acting on the two fields `config_path` and `output_path`, respectively referring to the root folder of the set of configuration files, and of the output of the analysis.

To this aim, we can either directly edit the `~/.cobrawap/config` file, or reuse the `cobrawap init` command as:
```
cobrawap init --config_path <CONFIG_PATH> --output_path <OUTPUT_PATH>
```

TBD: curation file, data set location, ...

## Run Cobrawap on a specific dataset

TBD: run, run_stage & run_block
