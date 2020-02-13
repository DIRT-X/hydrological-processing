import os
try:
    import os, sys, datetime
except:
    print("ImportERROR: Missing fundamental packages (required: os, sys, datetime).")

try:
    import tkinter as tk
    from tkinter import ttk
    from tkinter.messagebox import askokcancel, showinfo, askyesno
    from tkinter.filedialog import *
except:
    print("ImportERROR: Missing package: tkinter.")

available_stats = ['MAX', 'MIN', 'MEAN', 'MED', 'STD', 'SUM']  # if changed here, also update fData.calc_stats
no_data_value = -9999
r2skip = ['ncols', 'nrows', 'xllcorner', 'yllcorner', 'cellsize', 'nodata_value']
save_file_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..')) + "\\"


# tkinter variables
code_icon = os.path.dirname(__file__) + "\\icon.ico"
xd = 5
yd = 5
ww = 600
wh = 350