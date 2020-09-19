# Python for Data Engineer

*Advanced samples and code remember for data engineer work*

Using PyPy3 to get JIT performance and do serious work.

### The correct way to work with Python

Install pypy3 on your system, like:

	(arch) sudo pacman -S pypy3
	(debian) sudo apt install pypy3
	(mac) brew install pypy3
	(windows) choco install pypy3

#### Why using the virtual Environment and PyPy:

Python “Virtual Environments” allow Python packages to be installed in an isolated location for a particular application, rather than being installed globally.

Python normaly runs on its default interpreter. PyPy runs on a most powerfull virtual machine and has much more performance.

Do not ever install dependencies on the local/original installed PyPy (or Python). **Always** use virtual environments to work with it. It's created by the installed global instance. Create them inside *.venv* that is inside your home:

	pypy3 -m venv ~/.venv/dtengineer

Inside this virtual environment you will **find** the famous **pip** (the dependency manager):

	source ~/.venv/dtengineer/bin/activate
	pip list
	
With the virtual environment activated, if you call for *python*, it will be the virtual environment: 
	
	python --version
	deactivate

### Install this project to develop

On Python/PyPy the *pip* install command makes pip install dependencies declared with *install_requires* on *setup.py*. Install using the virtualenv that we just created. The *--editable* flag does not allow to package (with wheel), we will package on another step:

	source ~/.venv/dtengineer/bin/activate
	pip install --editable .

### Package

To make a package, we will use the recommended and modern wheel . From project root folder run:

	pip install wheel
	pip wheel .
	
TODO Now, look at the *??????* folder on the root dir of this project. There you will find *.whl* compressed file.
TODO how to package whl on another folder

### Install the package .whl on another virtual environment

This project should be inside on another virtual environment on production. 

Create this env and copy all *.whl* generated files (including dependencies) to the root of it:

    pypy3 -m venv ~/.venv/production

Install it:

    source ~/.venv/production/bin/activate
    pip install python_data_engineer-0.1-py3-none-any.whl

Run it:

    TODO how to execute on best way.... with main maybe ... or initial script to run...

Official docs about using setuptools as python build tool:

    https://setuptools.readthedocs.io/en/latest/setuptools.html
