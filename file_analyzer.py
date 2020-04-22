from fData import *
import datetime as dt


def process_files(file_dir, mode='exact', stat_glob='MAX', stat_time='MAX'):
    """ processes all files provided in file_dir using mode
    :param file_dir: STR
    :param mode: STR    Exact = overlay all files
                        Daily = only use daily stat_type (e.g., daily max or min)
                        Monthly = only use monthly stat_type (e.g., daily max or min)
    :param stat_glob: STR default = 'MAX'; options: 'MIN', 'MEAN', 'MED', STD', 'SUM'
    :param stat_time: STR default = 'MAX'; options: 'MIN', 'MEAN', 'MED', STD', 'SUM'
    :return: None
    """
    print("Starting analysis of all files in folder {0}\n - processing mode: {1} ({2})\n - global statistics type: {3}".format(file_dir, mode, stat_time, stat_glob))
    file_dict = sort_file_names(list_file_type_in_dir(file_dir, '*'), mode)

    if not ("exact" in mode):
        time_window_results = []
        for k in file_dict.keys():
            file_contents = read_multiple_files(file_dict[k])
            time_window_results.append(array_stats(file_contents, stat_type=str(stat_time).upper()))
        array_stack = np.array(time_window_results)
    else:
        array_stack = read_multiple_files(file_dict.values())

    save_result(array_stats(array_stack, stat_type=stat_glob.upper()), config.save_file_dir + "result_" + mode + stat_time.upper() + "_" + stat_glob.upper())


def make_date_key(date_string, time_stamp):
    """     generates a key entry for sorted-file dictionary
    :param date_string: STR e.g., "20160115"
    :param time_stamp: STR (either "days" or "months")
    :return: STR
    """
    f_date = dt.datetime.strptime(date_string, "%Y%m%d")
    if "day" in time_stamp.lower():
        return "%4i" % f_date.year + "%02i" % f_date.month + "%02i" % f_date.day
    if "month" in time_stamp.lower():
        return "%4i" % f_date.year + "%02i" % f_date.month


def sort_file_names(file_list, time_stamp):
    """   rearranges a list of file by either day or month
    :param file_list: LIST of files
    :param time_stamp: STR (either "days" or "months")
    :return: DICT
    """
    sorted_files = {}
    if not ("exact" in time_stamp):
        for fn in file_list:
            # convert file names (e.g., "precbanja_20160131.006") to date
            date_key = make_date_key(str(fn).split("_")[-1].split(".")[0], time_stamp)
            if not (date_key in sorted_files.keys()):
                sorted_files.update({date_key: [fn]})
            else:
                sorted_files[date_key].append(fn)
    else:
        [sorted_files.update({fn: fn}) for fn in file_list]
    return sorted_files


if __name__ == '__main__':
    file_dir = 'C:\\Users\\Mouris\\Desktop\\Test_Prec\\'
    process_files(file_dir)
