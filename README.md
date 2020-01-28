# Purpose
Python package for automating data processing. Current capacities:

- Read files with same data field size as `numpy.array` (dimensions: `number of files` x `rows` x `columns`)


# Structure

| `.py` file name | Purpose |
|:---------------:|:-------:|
|`config.py` | Repetitively used variables (e.g., `no_data_value = -9999`) |
|`fData.py` | pool of functions |
|`main.py` | main script for [[Usage]]|

# Usage
For normal usage, redefine `file_dir` with the directry where data files are stored. The variable `file_names` comes from `fData.list_file_type_in_dir('directory', 'file_type')`, which receives `file_dir` and `'*'` (for all file types) as input arguments.
The variable `file_contents` is filled from `fData.read_multiple_files('file_names')` and has the size of `number of files` x `rows` x `columns` (please note: this step can take some time depending on the number of files).

For help with getting started with Python, refer to the [[Requirements]] section.

# Requirements
The code is designed for being used with [Python Anaconda](https://www.anaconda.com/distribution/). With Python Anaconda installed, used the provided `environment.yml` file to create a conda environment:

1. Open Anaconda prompt
1. Navigate to the download directoy of this packages (use [`cd`](https://www.digitalcitizen.life/command-prompt-how-use-basic-commands))
1. Enter `conda env create -f environment.yml` (this creates the environment `geopython`)
1. [OPTIONAL] To install more packages, type (in Anaconda prompt):
	- `conda activate geo-python`
	- `conda install PACKAGE_NAME`
	
In order to use the new environment, download a Python IDE (e.g., Spyder (provided along with Anaconda) or [PyCharm](https://www.jetbrains.com/de-de/pycharm/download/#section=windows)).
