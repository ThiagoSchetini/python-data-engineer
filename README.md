# Python for Data Engineer

*Advanced samples and code remember for data engineer work*

### Python virtual env create with *venv*:

using your IDE or manually, create the venv like:

    python -m venv ~/.venv/python-data-engineer
    
manual activate *(if you are not using an IDE)*

    source ~/.venv/python-data-engineer/bin/activate

**inside your venv** use pip to install dependencies:

	pip install --upgrade setuptools
	pip install ...
	
manual deactivate *(if you are not using an IDE)*:

	deactivate

### How to package (we use the modern setuptools):

from root folder:

    python3 setup.py sdist

official docs about using setuptools as python build tool:

    https://setuptools.readthedocs.io/en/latest/setuptools.html
