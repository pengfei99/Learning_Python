## Python dev env set up

https://medium.com/semantixbr/getting-started-with-conda-or-poetry-for-data-science-projects-1b3add43956d#:~:text=Conda%20and%20Poetry%20stand%20out,environment%20management%20for%20any%20language.

### Install conda

The official doc can be found [here]
https://docs.conda.io/projects/conda/en/latest/user-guide/install/linux.html

### Setup an conda env

```shell
# create a virtuel env with a specific python version
conda create --name pyqt-dev python=3.9

# list existing conda env
conda env list

# activate a conda env
conda activate pyqt-dev

# test python version of the virtual env
python -V

# search a package
conda search pandas

# install the package  in the virtual env
conda install pandas

# list installed package
conda list

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
