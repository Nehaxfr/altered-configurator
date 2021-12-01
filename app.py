import tkinter as tk
from os import path
import glob
import os


class Application:
    def __init__(self, parent):
        self.lst_configuration = self.load_existing_configuration()
        if self.lst_configuration:
            self.main_frame = self.load_win_select_configuration()
        else:
            self.main_frame = self.load_win_create_configuration()
        self.main_frame.pack()

    @staticmethod
    def load_existing_configuration():
        lst_configuration = []
        config_path = os.path.join(os.curdir, "config")
        if path.exists(config_path):
            lst_configuration = glob.glob(f"{config_path}/*.txt")
        else:
            os.makedirs(config_path)
        return lst_configuration

    @staticmethod
    def load_win_select_configuration():
        main_frame = tk.Frame()
        return main_frame

    @staticmethod
    def load_win_create_configuration():
        main_frame = tk.Frame()
        lbl_path = tk.Label(main_frame, text="Path to your AE server directory").pack()
        input_path = tk.Entry(main_frame).pack()
        btn_validate = tk.Button(main_frame, text="Validate").pack()
        return main_frame


if __name__ == "__main__":
    root = tk.Tk()
    Application(root)
    root.mainloop()
