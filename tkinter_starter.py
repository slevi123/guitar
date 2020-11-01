import tkinter as tk


def main(base_frame, title: str):
    root = tk.Tk()
    root.title(title)
    base_frame(root).pack()
    root.mainloop()
    return root


if __name__=="__main__":
    main(None, 'program futtatasa')
