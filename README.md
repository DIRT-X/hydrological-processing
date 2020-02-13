# Purpose
Python package for automating data processing. Current capacities:

- Read files with same data field size as `numpy.array` (dimensions: `number of files` x `rows` x `columns`)

# Requirements<a name="requirements"></a>
The code is designed for being used with [Python Anaconda](https://www.anaconda.com/distribution/). With Python Anaconda installed, used the provided `environment.yml` file to create a conda environment:

1. Open Anaconda prompt
1. Navigate to the download directory of this packages (use [`cd`](https://www.digitalcitizen.life/command-prompt-how-use-basic-commands))
1. Enter `conda env create -f environment.yml` (this creates the environment `geopython`)
1. [OPTIONAL] To install more packages, type (in Anaconda prompt):
    - `conda activate geo-python`
    - `conda install PACKAGE_NAME`
    
To use the new environment, download a Python IDE (e.g., Spyder (provided along with Anaconda) or [PyCharm](https://www.jetbrains.com/de-de/pycharm/download/#section=windows)).


# Structure

The pool folder includes static values (e.g., written into the `config` file) and graphics used by the graphical user interface. The `media/` directory contains imagery for code explanations.

| `.py` file name | Purpose |
|:----------------|:--------|
|`pool/config.py` | Repetitively used variables (e.g., `no_data_value = -9999`) |
|`fData.py` | pool of functions |
|`launch_gui.py` | Main script for [Usage](#usage)|
|`file_analyzer.py`| Function master script (see [Modify code](modc) section) |
|`environment.yml`| conda environment (see [Requirements](#requirements))|

# Usage<a name="usage"></a>
## Getting started
Launching the main script `launch_gui.py` opens up a graphical user interface (GUI). For help with getting started with Python, refer to the [[Requirements]] section.

![guiimage](https://github.com/sschwindt/dirtx/raw/master/media/gui.png)

The GUI provides options to change the input file directory and to choose global as well as sliding time window statistics. The global statistic analysis type is applied to the stack of all data files in the input directory. The time window statistics can be optionally applied to use for example daily maximum or monthly mean (average) of the files in the input directory. In this case, the global statistics will be applied on top of the time window (sliding window).
To avoid any time averaging, select `EXACT` (default) from the comboboxes (drop-down menus).
A click on the "Analyze files in input directory" button will start the calculations (file processing).


## Calculate statistics
The available statistic functions are stored in a dictionary in  `fData.array_stats(array, stat_type)`:

| `stat_type` | statistics |
|:------------|:--------|
|`MAX` | Maximum (`numpy.nanmax`) |
|`MIN` | Maximum (`numpy.nanmin`) |
|`MED` | Maximum (`numpy.nanmedian`) |
|`MEAN` | Maximum (`numpy.nanmean`) |
|`STD` | Maximum (`numpy.nanstd`) |
|`SUM` | Sum (`numpy.nansum`) |

With an input array (`numpy.array`) with the shape `(f, x, y)`, the output of `fData.array_stats(array, stat_type)` has the shape `(x, y)`; where `f` is the number of files provided, `x` is the number of data rows, and `y` is the number of data columns. 

## Modify code<a name="modc"></a>
The GUI calls the functional from `file_analyzer.py` within the `process_files(...)` function (main function in earlier versions.
`file_analyzer.py` can also be executed independently from the GUI. The `process_files(...)` function first sorts the file names, then it calls the optional time window statistics and only afterwards, it calculates the global statistics. Finally, it directly saves the results produced with the `array_stats(...)` function (`fData.py`) to a file called `result_timeSTAT_globalSTAT` in the same directory where `file_analyzer.py` is located (please note: this step can take some time depending on the number of files).
The variable `array_stack` is filled from `fData.read_multiple_files('file_names')` if exactly all files without time stats are applied. It has the size of `number of files` x `rows` x `columns`.
The results directory and file name can be changed within the `config.py` file and the `process_files(...)` function, respectively.
Note that the analysis currently uses hard-coded identifiers to extract dates from file names. If these need to be changed, go to the `sort_file_names(...)` function (`function_analyzer.py`) and modify the argument passed to the `make_date_key(...)` function (produces the variable `date_key`).

