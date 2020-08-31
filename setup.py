import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="python-data-engineer",
    version="0.0.1",
    author="Thiago Schetini",
    author_email="thiagoschetini@gmail.com",
    description="Coding for data engineer with Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ThiagoSchetini/python-data-engineer",
    packages=setuptools.find_packages(),

    # more classifiers: https://pypi.org/classifiers/
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: POSIX :: Linux",
    ],
    python_requires='>=3.8',
)
