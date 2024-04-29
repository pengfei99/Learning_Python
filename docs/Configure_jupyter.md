# Configure jupyter lab/notebook server

If you run jupyter lab/notebook locally, you dont need to do much. But if you run it on a server which will be accessed
remotely, you need to configure it well. Otherwise, you can't access it.
## Use command line config
```shell
# after installing jupyter lab/notebook

jupyter notebook password

# this command will generate a config file
/home/pliu/.jupyter/jupyter_server_config.json

# run jupyter notebook server
# --ip='*' means allow all ip to access the server, by default only localhost is allowed
# port specifies the port number
# --no-browser don't try to open it with browser locally
jupyter notebook --ip='*' --port=8080 --no-browser
```
## Generate default config

```shell
# for jupyter lab
jupyter lab --generate-config
# This will generate jupyter_lab_config.py  

# for notebook
jupyter notebook --generate-config
# this will generate jupyter_notebook_config.py

```

### Notebook config

#### Allow remote access 

```shell
c.ServerApp.allow_origin = '*' #allow all origins
c.SeverApp.ip = '0.0.0.0' # listen on all IPs 
```

#### Disable password and token 
https://jupyter-server.readthedocs.io/en/stable/operators/security.html#security-in-notebook-documents
```shell
# ServerApp.token is deprecated, use 
IdentityProvider.token

```

### Add kernel to jupyter

```shell
# Activate the virtualenv
source your-venv/bin/activate

# install jupyter inside the virtuel env
pip install jupyter 

# the local python vir env is used as the default one 
# add the local python vir env explicitly
ipython kernel install --name "local-venv" --user

# list existing kernel  
jupyter kernelspec list

# output
Available kernels:
  global-tf-python-3    /home/felipe/.local/share/jupyter/kernels/global-tf-python-3
  local_venv2           /home/felipe/.local/share/jupyter/kernels/local_venv2
  python2               /home/felipe/.local/share/jupyter/kernels/python2
  python36              /home/felipe/.local/share/jupyter/kernels/python36
  scala                 /home/felipe/.local/share/jupyter/kernels/scala
  
  
# remove kernel
jupyter kernelspec remove old_kernel

# Change Kernel name
1) Use $ jupyter kernelspec list to see the folder the kernel is located in

2) In that folder, open up file kernel.json and edit option "display_name"
```