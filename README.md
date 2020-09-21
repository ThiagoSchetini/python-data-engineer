# Python for Data Engineer

*Advanced samples and code remember for data engineer work*

Use PyPy3 to get JIT performance and do serious work.

Use the last and best practices about python development, package and distribution!

It's Unix/GNU Linux only!

### Setup environment

Install *pypy3* on your system, like:

	(arch) sudo pacman -S pypy3
	(debian) sudo apt install pypy3
	(mac) brew install pypy3

##### Use the virtual Environment:

Python “Virtual Environments” allow Python packages to be installed in an isolated location for a particular application, rather than being installed globally.

Do not ever install dependencies on the local/original installed PyPy (or Python). Create the virtual environment inside *.venv* on your home:

	pypy3 -m venv ~/.venv/dtengineer

Inside this virtual environment you will find the famous *pip* (the dependency manager):

	source ~/.venv/dtengineer/bin/activate
	pip list
	
With the virtual environment activated, if you call for *python*, actually it will be the virtual environment: 
	
	python --version
	deactivate

### Install this project to develop

On Python/PyPy the *pip* install command makes pip install dependencies declared with *install_requires* on *setup.py*. Install using the virtualenv that we just created. The *--editable* flag does not allow to package (with wheel), we will package on another step. From the root folder run:

	source ~/.venv/dtengineer/bin/activate
	pip install --editable .

### Package with Wheel

To make a package, we will use the recommended and modern *wheel*. From project root folder run:

	pip install wheel
	pip wheel .
	
TODO Now, look at the *??????* folder on the root dir of this project. There you will find *.whl* compressed file.
TODO how to package whl on another folder

### Install the *.whl* wheel package

Create or enter on another virtual environment, like production:

    deactivate 
    pypy3 -m venv ~/.venv/production

Copy all *.whl* generated files (including dependencies) to the root of *production*:

    cp ~/Repositories/github/python-data-engineer/*.whl ~/.venv/production

Activate the *production* virtual environment, them, from its root folder install:

    source ~/.venv/production/bin/activate
    pip install python_data_engineer-0.1-py3-none-any.whl

### Run the installed project as production

TODO how to execute on best way.... with main maybe ... or initial script to run...

### Run the source as developer 

TODO create the mechanisms to run inside this folder
    
