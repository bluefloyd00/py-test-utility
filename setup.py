import setuptools
from version import get_git_version

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="0.0.2",
    version=get_git_version(),
    author="Simone Fiorentini",
    author_email="simone.fiorentini@gmail.com",
    description="useful package for pipelines testing and data mocking for new generation data warehouse",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bluefloyd00/py-test-utility",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
