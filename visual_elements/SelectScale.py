from tkinter import StringVar
from tkinter.ttk import OptionMenu


class SelectScaleOptionMenu(OptionMenu):
    def __init__(self, parent, ):
        self.variable = StringVar(parent)
        self.variable.set("Chromatic Scale")
        scales = [
            "Chromatic Scale",
            "C",
            "D",
            "E",
            "F",
            "G",
            "A",
            "B"
        ]
        super().__init__(parent, self.variable, "Chromatic Scale", *scales)

