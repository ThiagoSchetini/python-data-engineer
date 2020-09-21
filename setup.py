from setuptools import setup, find_packages

# sample configuration on: https://github.com/pypa/sampleproject/blob/master/setup.py
# official setuptools: https://setuptools.readthedocs.io/en/latest/setuptools.html

setup(
    name="python-data-engineer",
    version="0.1",
    author="Thiago Schetini",
    author_email="thiagoschetini@gmail.com",
    description="Coding for data engineer with Python",
    url="https://github.com/ThiagoSchetini/python-data-engineer",
    
    # auto find packages inside 'src' to compile/pkg
    packages=find_packages(where='src'),
    package_dir={'': 'src'},

    # more classifiers: https://pypi.org/classifiers/
    classifiers=[
        "Programming Language :: Python :: Implementation :: PyPy",
        "Operating System :: POSIX :: Linux",
    ],

    python_requires='>=3.6',
    
    install_requires=[
        'py4j>=0.10.9',
        'pyspark>=3.0.1'
    ],
    
    data_files=[('sample_data', ['data/sample_data'])]
)
