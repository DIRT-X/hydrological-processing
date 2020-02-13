try:
    import sys, os
    sys.path.append(os.path.dirname(__file__) + "\\pool\\")
    from config import *
    import file_analyzer as fa
except:
    print("ERROR: Could not import config.")


class Xgui(tk.Frame):
    # master GUI for all RiverArchitect modules
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack()
        self.set_geometry()

        # make common tkinter objectss
        tk.Label(self, text="Current input directory:").grid(sticky=tk.W, row=0, column=0, padx=xd)
        self.dir_init = "P:\\aktiv\\2018_DIRT-X\\DIRT-X_Intern\\10_Data\\01_Banja\\Precip_Banja\\"
        self.l_dir_init = tk.Label(self, text=self.dir_init, width=65, justify=tk.LEFT, anchor=tk.W)
        self.l_dir_init.grid(sticky=tk.W, row=1, column=0, padx=xd)
        tk.Button(self, fg="RoyalBlue3", bg="white", text="Change", command=lambda: self.change_data_dir()).grid(sticky=tk.EW, row=1, column=1, padx=xd, pady=yd)
        tk.Label(self, text=" ").grid(sticky=tk.W, row=2, column=0, padx=xd)  # dummy
        tk.Label(self, text="Select global statistic analysis type:").grid(sticky=tk.W, row=3, column=0, padx=xd, pady=yd)
        self.c_stat = ttk.Combobox(self, width=8)
        self.c_stat.grid(sticky=tk.W, row=3, column=1, padx=xd, pady=yd*4)
        self.c_stat['state'] = 'readonly'
        self.c_stat['values'] = available_stats
        self.c_stat.set(available_stats[0])
        tk.Label(self, text="Choose length of time window:").grid(sticky=tk.W, row=4, column=0, padx=xd, pady=yd)
        self.c_mode = ttk.Combobox(self, width=8)
        self.c_mode.grid(sticky=tk.W, row=4, column=1, padx=xd, pady=1)
        self.c_mode['state'] = 'readonly'
        self.c_mode['values'] = ["Exact", "Daily", "Monthly"]
        self.c_mode.set("Exact")
        tk.Label(self, text="if the time window is not EXACT, set time window statistics:").grid(sticky=tk.E, row=5, column=0, padx=xd, pady=yd)
        self.c_stat_time = ttk.Combobox(self, width=8)
        self.c_stat_time.grid(sticky=tk.W, row=5, column=1, padx=xd, pady=1)
        self.c_stat_time['state'] = 'readonly'
        self.c_stat_time['values'] = available_stats
        self.c_stat_time.set("EXACT")

        tk.Button(self, fg="RoyalBlue3", bg="white", text="Analyze files in input directory",
                  command=lambda: self.analyze_files()).grid(sticky=tk.EW, row=6, column=0, columnspan=2, padx=xd, pady=yd*4)

        self.b_return = tk.Button(self, fg="RoyalBlue3", bg="white", text="QUIT",
                                  command=lambda: self.close_window())
        self.b_return.grid(row=25, column=25, padx=xd, pady=yd)

    def analyze_files(self):
        fa.process_files(self.dir_init, mode=str(self.c_mode.get()).lower(), stat_glob=str(self.c_stat.get()).lower(),
                         stat_time=str(self.c_stat_time.get()).lower())
        showinfo("FINISHED", "The results have been written to \n%s\n(see console message)" % save_file_dir)


    def change_data_dir(self):
        self.dir_init = askdirectory(initialdir=self.dir_init) + "/"
        self.l_dir_init.config(text=self.dir_init)

    def close_window(self):
        self.master.destroy()

    def set_geometry(self):
        # ww and wh = INT of window width and window height
        # Upper-left corner of the window.
        wx = (self.master.winfo_screenwidth() - ww) / 2
        wy = (self.master.winfo_screenheight() - wh) / 2
        # Set the height and location
        self.master.geometry("%dx%d+%d+%d" % (ww, wh, wx, wy))
        self.master.iconbitmap(code_icon)
        self.master.title("DIRT-X File Processor")


if __name__ == '__main__':
    Xgui().mainloop()
