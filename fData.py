import os, sys, glob
import numpy as np
sys.path.append(os.path.dirname(__file__) + "\\pool\\")
import config
from functools import partial


def array_stats(array, stat_type='MAX'):
    """     calculates array statistics
    :param array: 3-dimensional np.array (shape n x m x o)
    :param stat_type: STR (default = 'MAX'; options: 'MIN', 'MEAN', 'MED', STD')
    :return: 2-dimensional np.array (shape m x o)
    """
    stats = np.ones((array.shape[1], array.shape[2])) * np.nan  # instantiate output field
    for x in range(array.shape[1]):
        for y in range(array.shape[2]):
            stats[x, y] = calc_stats(list(array[:, x, y]), stat_type)
    return np.array(stats)


def calc_stats(value_list, stat_type='MAX'):
    """ calculates statistics of the list of values provided in value_list
    :param value_list: LIST
    :param stat_type: STR (default = 'MAX'; options: 'MIN', 'MEAN', 'MED', 'STD', 'SUM')
    :return: float
    """
    stat_dict = {'MAX': partial(np.nanmax, value_list),
                 'MIN': partial(np.nanmin, value_list),
                 'MEAN': partial(np.nanmean, value_list),
                 'MED': partial(np.nanmedian, value_list),
                 'STD': partial(np.nanstd, value_list),
                 'SUM': partial(np.nansum, value_list)}
    return stat_dict[stat_type]()


def list_file_type_in_dir(directory, f_ending):
    """
    :param directory: full directory ending on "/" or "\\"
    :param f_ending: STR, e.g., ".py"
    :return: LIST of full file paths"""
    return glob.glob(directory + "*" + f_ending)


def read_file(file_dir):
    """ loads ascii file as matrix
    :param file_dir: STR of full file path
    :return: numpy.array
    """
    data = []
    if os.path.isfile(file_dir):
        file = open(file_dir)
        for line in file:
            if not(line.split('\t')[0] in config.r2skip):
                line_entries = []
                for e in line.split('\t'):
                    try:
                        line_entries.append(float(e))
                    except:
                        print('WARNING: Invalid entry ({0}) in {1} (set to np.nan)'.format(str(e), file_dir))
                        line_entries.append(np.nan)
                line_entries = [np.nan if float(x) == float(config.no_data_value) else x for x in line_entries]  # overwrite define no_data values
                data.append(line_entries)
    return np.array(data)


def read_multiple_files(list_of_files):
    """
    :param list_of_files: LIST of STR of full file dirs
    :return: np.array (dimensions: file x rows x columns)
    """
    file_contents = []
    for file_dir in list_of_files:
        file_contents.append(read_file(file_dir))
    return np.array(file_contents)


def save_result(data_array, file_name):
    """ saves data array to file_name
    :param data_array: numpy.array
    :param file_name: STR
    """
    print(" - saving %s ... " % str(file_name))
    with open(file_name, 'wb') as f:
        np.savetxt(f, data_array)


