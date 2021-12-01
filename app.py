from tkinter import *
from tkinter.ttk import *
from os import path
from src import utils
import glob
import os


class Application:
    def __init__(self):
        self.lst_configuration = self.load_existing_configuration()
        if self.lst_configuration:
            self.main_frame = self.load_win_select_configuration(lst_config=self.lst_configuration)
        else:
            self.main_frame = self.load_win_create_configuration()
        self.main_frame.pack()

    @staticmethod
    def load_existing_configuration():
        lst_configuration = []
        config_path = os.path.join(os.curdir, "config")
        if path.exists(config_path):
            lst_configuration = glob.glob("./config/*.txt")
        else:
            os.makedirs(config_path)
        return lst_configuration

    @staticmethod
    def load_win_select_configuration(lst_config):
        main_frame = Frame()
        lbl_select = Label(main_frame, text="Select the configuration to load").pack()
        list_obj_config = utils.create_config_list(lst_config)
        select_config = Combobox(main_frame, values=[config.name for config in list_obj_config]).pack()
        return main_frame

    @staticmethod
    def load_win_create_configuration():
        main_frame = Frame()
        lbl_path = Label(main_frame, text="Path to your AE server directory").pack()
        input_path = Entry(main_frame).pack()
        btn_validate = Button(main_frame, text="Validate").pack()
        return main_frame


if __name__ == "__main__":
    root = Tk()
    Application()
    root.mainloop()
