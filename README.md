# A short tutorial for Cobrawap hands-on sessions

Cobrawap (Collaborative Brain Wave Analysis Pipeline) is an adaptable and reusable analysis pipeline for the multi-scale, multi-methodology analysis of cortical wave activity. The pipeline ingests data from heterogeneous sources of spatially organized neuronal activity, such as ECoG or calcium imaging recordings, as well as the outcome of numerical simulations. The pipeline returns statistical measures to quantify the dynamic wave-like activity patterns found in the data.

The open-source software for Cobrawap official releases is available [here](https://github.com/NeuralEnsemble/cobrawap), and fully documented [here](https://cobrawap.readthedocs.io).

## Cobrawap installation

From now on, we will refer to a root working directory, say `WK_DIR`, and all the paths will then contain in their first part the absolute path to it, say `/path/to/WK_DIR/`. Every user has then to replace it with the actual absolute path to `WK_DIR` on his/her laptop/platform.

### Creating a virtual environment for Cobrawap

First of all, it's necessary to have a working recent release of [python3](https://www.python.org/download/releases/3.0/), necessary for creating a virtual environment in which Cobrawap software and all its dependencies will be installed, without causing interferences with other python packages.

There are two possible options, [conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html) and [virtualenv](https://docs.python.org/3/library/venv.html). Be sure to have one of them installed and properly working.

Then, find below a minimal set of instructions to make them work for our hands-on:

| How to... | conda | virtualenv |
|----------|-------------|------|
| Create it |  ```conda create --name env_cobrawap python=3.9``` | ```python3 -m venv env_cobrawap``` |
| Activate it | ```conda activate env_cobrawap``` | ```source env_cobrawap/bin/activate``` |
| Deactivate it | ```conda deactivate``` | ```deactivate``` |

Notice that, in the case of virtualenv, in `WK_DIR` will be created a folder with the same name as the environment just created, i.e. `env_cobrawap` in our case. At variance, conda will not create further folders in `WK_DIR`.

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

In fact, due to a recent update of the `PulP` package being in conflict with `snakemake`, the former package has to be pinned to an older version. To this aim, let's then type the command:
```
pip install pulp==2.6.0
```

### Initial configuration

Once the installation process through pypi has finished, it is then possible to configure its global settings. To this aim, one should launch the command:
```
cobrawap init --config_path <CONFIG_PATH> --output_path <OUTPUT_PATH>
```
by specifying the requested fields with the desired paths for Cobrawap output and configuration files. At the same time, also the root of Cobrawap source code will be pointed at, and a list of Cobrawap stages will be created (refer to the [docs](https://cobrawap.readthedocs.io/en/latest/pipeline_stages.html) for more details). All these info will be collected and made further customizable at the path `~/.cobrawap/config`; it's possible to show them by invoking the command
```
cobrawap settings
```

For our hands-on, it's not necessary to launche the `cobrawap init` command at this point; at variance, let's first retrieve the test datasets, and then let's fully configure Cobrawap for the chosen use-case.

## Configuring Cobrawap on a specific dataset

Indeed, the fine-level configuration of Cobrawap clearly depends on the actual dataset to be analyzed (e.g. coming from imaging or ECoG experiments), as well as on the kind of analysis to perform. The modular structure of Cobrawap allows for a very deep customization of the processing, starting from the preliminar but necessary step of *data curation* (implemented in a dedicated *curation* block in the *data_entry* stage) and then going through the whole pipeline. For this reason, along with each test dataset present in this repository, also an analysis *profile* (i.e. a dedicated *curation_script* and a set of *configuration files*) is provided.

In order to donwload the test datasets and their related analysis profiles, let's put ourselves into the chosen working directory `WK_DIR` and then type the command:
```
git clone https://github.com/APE-group/hands_on_cobrawap.git
```
which will download the whole content of this repository, storing it under the `hands_on_cobrawap` root folder.

### Configuration

Let's now choose a certain test dataset among those here available, calling it TEST_DATASET from now on.

In order to configure the pipeline for running on the chosen dataset with the related analysis profile, we have to modify the accordingly the `~/.cobrawap/config` settings file, acting on the two fields `config_path` and `output_path`, respectively referring to the root folder of the set of configuration files, and of the output of the analysis.

To this aim, we can now invoke the initialization command:
```
cobrawap init --config_path <CONFIG_PATH> --output_path <OUTPUT_PATH>
```

`CONFIG_PATH` has to point at the chosen dataset, e.g. `/path/to/WK_DIR/hands_on_cobrawap/test_datasets/<CHOSEN_DATASET>/profiles`, while a suggested choice for `OUTPUT_PATH` is `/path/to/WK_DIR/output`.

By default, Cobrawap will try to build the tree structure of folders containing the templates for the necessary configuration files. In our case, we already provided the suitable configuration files related to the chosen dataset, and pointed at it in the inizialization command. Hence, Cobrawap will throw a prompt, `The config directory /path/to/WK_DIR/hands_on_cobrawap/test_datasets/<CHOSEN_DATASET>/profiles already exists and is not empty. Create template config files anyway? [y/N]`, and we have to type `N` in order to use the provided configuration files.

To end the configuration, let's open the configuration file of stage01, and change the `/path/to/WK_DIR` placeholder into the actual absolute path to `WK_DIR`.

## Run Cobrawap on a specific dataset

TBD: run, run_stage & run_block
