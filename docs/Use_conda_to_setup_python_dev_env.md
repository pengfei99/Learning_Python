# Python dev env set up

https://medium.com/semantixbr/getting-started-with-conda-or-poetry-for-data-science-projects-1b3add43956d#:~:text=Conda%20and%20Poetry%20stand%20out,environment%20management%20for%20any%20language.

## Install conda

The official doc can be found [here]
https://docs.conda.io/projects/conda/en/latest/user-guide/install/linux.html

For windows, it's quite simple, just download the installer and double click on it.

## Using conda to set up dev env

You can find conda cheatsheet [here](https://conda.io/projects/conda/en/latest/user-guide/cheatsheet.html)

### Managing conda

```shell
# show all basic info of conda
conda info

# check current conda version
conda --version

# update conda
conda update conda
```

### Managing conda envs (virtural environment)

```shell
# create a virtuel env with a specific python version
conda create --name pyqt-dev python=3.9

# list existing conda env
conda env list
conda info --envs

# The active/current environment is the one with an asterisk (*).

# activate a conda env
conda activate pyqt-dev

# test python version of the virtual env
python -V


# deactiate an env
conda deactivate
```

### Remove conda env

```shell
# remove env by its name, the --all option remove all related files
conda remove -n corrupted_env --all

# remove env by its path, If you have the path where a conda environment is located, you can directly 
# specify the path instead of name of the conda environment.
conda env remove --prefix /path/to/env
```

### Managing packages inside an env

```shell
# list installed package in current virtual env
conda list

# to check if a package is available 
conda search beautifulsoup4

# to install a package
conda install beautifulsoup4

# uninstall a package
conda uninstall beautifulsoup4
```

