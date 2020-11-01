import configparser
import tkinter

from visual_elements.BaseSounds import BaseSounds
from visual_elements.SoundBoard import SoundBoard


class BaseFrame(tkinter.Frame):
    def __init__(self, parent):
        super().__init__(parent, background="#8c887e",
                         highlightbackground="#8c887e", highlightcolor="green", highlightthickness=5)

        config_parser = self.get_config_parser()

        SoundBoard(self, config_parser).pack(padx=0, pady=0)
        BaseSounds(self, config_parser).pack(padx=0, pady=0)

    @staticmethod
    def get_config_parser():
        config = configparser.ConfigParser()
        config.read('config.ini')
        return config
