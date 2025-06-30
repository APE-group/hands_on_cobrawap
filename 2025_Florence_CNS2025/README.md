# "2025_Florence_CNS2025" hands-on of Cobrawap

<img src="https://github.com/APE-group/hands_on_cobrawap/blob/main/doc/images/cobrawap_logo.png" align="left" width="200px">

Cobrawap (Collaborative Brain Wave Analysis Pipeline) is an adaptable and reusable analysis pipeline for the multi-scale, multi-methodology analysis of cortical wave activity. The pipeline ingests data from heterogeneous sources of spatially organized neuronal activity, such as ECoG or calcium imaging recordings, as well as the outcome of numerical simulations. The pipeline returns statistical measures to quantify the dynamic wave-like activity patterns found in the data.

The open-source software for Cobrawap official releases is available [here](https://github.com/NeuralEnsemble/cobrawap), and fully documented [here](https://cobrawap.readthedocs.io).

<br/>

## Cobrawap installation

From now on, we will refer to a root working directory, say `WK_DIR`, and all the paths will then contain in their first part the absolute path to it, say `/path/to/WK_DIR/`. Every user has then to replace it with the actual absolute path to `WK_DIR` on his/her laptop/platform. To this aim, it can be useful to store such path into an environment variable, and use afterwards:

```
WK_DIR="/path/to/WK_DIR/"
```

### Creating a virtual environment for Cobrawap

First of all, it's necessary to have a working recent release of [python3](https://www.python.org/download/releases/3.0/), **with version >=3.8 and <=3.11**, necessary for creating a virtual environment in which Cobrawap software and all its dependencies will be installed, without causing interferences with other python packages.

The easiest option is through [virtualenv](https://docs.python.org/3/library/venv.html). There is also the [conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html) option, that allows you more flexibility in which python3 sub-version install, but requires more steps and is in general deprecated by our Institutions, being a commercial solution.

Find below the necessary steps for setting up a virtual environmente in both ways:

<details><summary>Using virtualenv...</summary>
<p>

:warning: With virtualenv, the created environment will inherit the python sub-version of the command used to create it. Be sure to have a >=3.8, <=3.11 python3 installation locally available.

:pushpin: How to create it:
```
python3 -m venv env_cobrawap_cns
```

:pushpin: How to activate it:
```
source env_cobrawap_cns/bin/activate
```

:pushpin: How to deactivate it:
```
deactivate
```

:pushpin: How to definitely remove it:
```
rm -r env_cobrawap_cns
```

Notice that virtualenv creates in `WK_DIR` a folder with the same name as the environment just created, i.e. `env_cobrawap_cns` in our case. Indeed, if you want to get rid of your virtual environment, it is enough to delete such folder.

</p>
</details>

<details><summary>Using conda...</summary>
<p>

:warning: In this case, instead, it is possible to specify the python3 sub-version to install in the new (empty) virtual environment.

:pushpin: How to create it:
```
conda create --name env_cobrawap_cns python=3.10
```

:pushpin: How to activate it:
```
conda activate env_cobrawap_cns
```

:pushpin: How to deactivate it:
```
conda deactivate
```

:pushpin: How to definitely remove it:
```
conda remove --name env_cobrawap_cns --all
```

In this case, all the dependencies of the new environment will now stored in the conda default location for virtual environments, unless otherwise specified. Check conda documentation for further details.

</p>
</details>

After having activated the virtual environment, it is suggested to update `pip`:
```
pip install --upgrade pip
```
and then check the environment functionality by typing a simple command, as by listing the installed packages:
```
pip list
```

### Installing the latest official release

In order to install the latest official release of Cobrawap, let's activate the (empty) virtual environment created above and then run the following command:
```
git clone https://github.com/APE-group/cobrawap.git
```
which will clone the GitHub repository of Cobrawap, and then let's enter the cobrawap directory:
```
cd cobrawap
```
and then switch to the branch `hands_on/CNS_2025` containing the latest developments for this tutorial:
```
git checkout hands_on/CNS_2025
```

Finally, in order to take care of all the dependencies and to install Cobrawap CLI commands, let's proceed with the installation by running the following command in the root directory of the GitHub project just cloned:
```
pip install -e .
```
At variance with the standard package installation from pypi, this approach allows to leverage the latest features of Cobrawap even though they have not yet been released officially as a package. Notice that this command may not work with very old versions of `pip`, so be sure to have updated `pip` in first place, as suggested at the beginning.

### Initial configuration

Once the installation process has finished, it is then possible to configure its global settings. To this aim, one should launch the `cobrawap init` command by specifying the requested fields with the desired paths for Cobrawap output and configuration files. At the same time, also the root of Cobrawap source code will be pointed at, and a list of Cobrawap stages will be created (refer to the [docs](https://cobrawap.readthedocs.io/en/latest/pipeline_stages.html) for more details). All these info will be collected and made further customizable at the path `~/.cobrawap/config`; it's possible to show them by invoking the `cobrawap settings` command.

For our hands-on, it's not necessary to launche the `cobrawap init` command at this point; at variance, let's first retrieve the test datasets, and then let's fully configure Cobrawap for the chosen use-case.

## Configuring Cobrawap on a specific dataset

Indeed, the fine-level configuration of Cobrawap clearly depends on the actual dataset to be analyzed (e.g. coming from imaging or ECoG experiments, or from spiking simulations), as well as on the kind of analysis to perform. The modular structure of Cobrawap allows for a very deep customization of the processing, starting from the preliminar but necessary step of *data curation* (implemented in a dedicated *curation* block in the *data_entry* stage) and then going through the whole pipeline. For this reason, along with each test dataset present in this repository, also an analysis *profile* (i.e. a dedicated *curation_script* and a set of *configuration files*) is provided.

### Cloning this repository

In order to download the test datasets and their related analysis profiles, let's put ourselves into the chosen working directory `WK_DIR` and then type the command:
```
git clone https://github.com/APE-group/hands_on_cobrawap.git
```
which will download the whole content of this repository, storing it under the `hands_on_cobrawap` root folder.

### Configuration

Let's now choose a certain test dataset among those here available, calling it CHOSEN_DATASET from now on.

In order to configure the pipeline for running on the chosen dataset with the related analysis profile, we have to properly set the two fields `config_path` and `output_path` in the `~/.cobrawap/config` settings file, respectively referring to the root folder of the set of configuration files, and of the output of the analysis.

To this aim, we can build the `CONFIG_PATH` environment variable, pointing at the chosen dataset configuration profile:
```
CONFIG_PATH=$WK_DIR"hands_on_cobrawap/test_datasets/<CHOSEN_DATASET>/profiles"
```
and the `OUTPUT_PATH` environment variable, that can be something like:
```
OUTPUT_PATH=$WK_DIR"/output"
```

Finally, let's invoke the Cobrawap initialization command:
```
cobrawap init --config_path $CONFIG_PATH --output_path $OUTPUT_PATH
```

If the `~/.cobrawap/config` file already exists, paths in the settings file can be overwritten only after the explicit consensus of the user.

:warning: By default, at the end of the initialization step, Cobrawap will try to build the tree structure of folders containing the templates for the necessary configuration files. In our case, we already provided the suitable configuration files related to the chosen dataset, and pointed at it in the inizialization command. Hence, Cobrawap will throw a prompt, `The config directory /path/to/WK_DIR/hands_on_cobrawap/test_datasets/<CHOSEN_DATASET>/profiles already exists and is not empty. Create template config files anyway? [y/N]`, and we have to type `N` in order to use the provided configuration files.

To end the configuration, let's open the configuration file of stage01, `/path/to/WK_DIR/hands_on_cobrawap/test_datasets/<CHOSEN_DATASET>/profiles/stage01_data_entry/configs/config.yaml`, and change the `/path/to/WK_DIR` placeholder into the actual absolute path to `WK_DIR` for the user-defined parameter `DATA_SETS` where input data is specified. `/path/to/WK_DIR` must be replaced with the actual absolute path also for parameter `ARRAY_ANNOTATION_FILE`.

## Run Cobrawap on a specific dataset

Cobrawap can be launched as a whole pipeline, at the single stage level, or even at the elementary block level, thanks to the [versatile commands](https://cobrawap.readthedocs.io/en/latest/command_line_interface.html) provided by its CLI, respectively `cobrawap run`, `cobrawap run_stage` and `cobrawap run_block`.

For this hands-on session, it is useful to focus on the intermediate behaviour of running single stages of Cobrawap.

### Run stage 01

Cobrawap first stage is devoted to data curation, i.e. annotation and formatting into the standard `neo` format used through the whole pipeline. The core of this stage is basically represented by the execution of the curation script shipped along with the dataset (typically, it is developed by the data providers, and with their close collaboration). At the end of the curation, time traces for some channels are provided as plots.

The related command to execute stage01 is:
```
cobrawap run_stage --stage 1 --profile spiking_hippocampus
```

### Run stage 02

Then, the actual processing of data, dealing with each channel independently from the others, takes place in stage02. Among the many possible elementary processing operations that can be applied, one can find the detrending, the frequency filter, the z-score normalization, and so on... Again, at the end of the stage, a comparison of original and processed time traces for some channels is provided, together with plots specific to the processing blocks chosen by the user.

The related command to execute stage02 is:
```
cobrawap run_stage --stage 2 --profile spiking_hippocampus
```

### Run stage 03

After data curation and processing, in stage03 Cobrawap focuses on the detection of timestamps marking an increased activity in the channel, e.g. a transition from a down state to an up state. In the framework of cortical slow waves, where Cobrawap has been initially designed and developed, that would represent a potential activation due to the passage of a slow wave. The so-called *trigger detection* can be performed via different algorithms, and once again further implementations can be easily contributed by the user. The final result is a collection of timestamps for each channel, still analyzed independently from one another.

The related command to execute stage03 is:
```
cobrawap run_stage --stage 3 --profile spiking_hippocampus
```

### Run stage 04

In this stage, timestamps recognized independently channel by channel are now clustered together, relying on the spatial arrangement of channels. Also in this case, the resulting waves of propagation can be classified according to different algorithms, allowing for a remarkable customizability.
The final result is here a collection of waves, to be then quantitatively analyzed in the next stage.

The related command to execute stage04 is:
```
cobrawap run_stage --stage 4 --profile spiking_hippocampus
```

### Run stage 05

Finally, the set of detected waves can be quantitatively analyzed, so to extract the interesting metrics. This can be done at the channel level, or collectively at the wave level; to this aim, two different versions of this stage are offered, `5` and `5b`. We will use the latter, for this use-case.

The related command to execute stage05 is:
```
cobrawap run_stage --stage 5b --profile spiking_hippocampus
```
