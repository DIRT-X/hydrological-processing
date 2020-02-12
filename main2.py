from fData import *


def main():
    # only change file_dir:
    # file_dir = 'P:\\aktiv\\2018_DIRT-X\\DIRT-X_Intern\\10_Data\\01_Banja\\Precip_Banja\\'
    # file_dir = 'C:\\Users\\Mouris\\Desktop\\Prec_SSC_Meas\\'
    # file_dir = 'C:\\Users\\Mouris\\Desktop\\Test_Prec2\\'
    file_dir = 'C:\\Users\\Mouris\\Desktop\\Prec_2_years\\'

    file_names = list_file_type_in_dir(file_dir, '*')
    file_contents = read_multiple_files(file_names)
    print(file_contents)
    print('Read {0} files of size {1}x{2}'.format(np.shape(file_contents)[0], np.shape(file_contents)[1], np.shape(file_contents)[2]))
    print('Cross-check number of provided input files: ' + str(file_names.__len__()))

   # write result raster
    result = (array_stats(file_contents, stat_type='MAX'))
    with open('result _raster','wb') as f:
        np.savetxt(f,result_)

    # try statistics
    print('Max of files: ')
    print(np.nanmax(array_stats(file_contents, stat_type='MAX')))


if __name__ == '__main__':
    main()