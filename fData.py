import sys, os, glob
import numpy as np
import config


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
    print("Reading {0} files (takes a while) ...".format(str(list_of_files.__len__())))
    file_contents = []
    for file_dir in list_of_files:
        file_contents.append(read_file(file_dir))
    return np.array(file_contents)



