# Learning_Python

In this repo, I document how I learned python. You can find the main course in [learning_python](./learning_python)


Below are the content of the course 
- Section01: Python basics
    - L01: Basic_syntax
    - L02: if condition
    - L03: loop
    - L04: Error and Exception handling
    - L05: Logging 
    - L06: Testing
    - L07: Documentation
- lesson2: Python I/O
- lesson3: Python Data types

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
```
