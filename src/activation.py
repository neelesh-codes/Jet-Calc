import numpy as np
import subprocess
import tkinter as tk

class Activate:
    def __init__(self):
        pass

    @staticmethod
    def install_build_requirments(arg):
        massage.config(text="""
        Now click on the
        black window that you saw
        when starting the programm\n
        and follow the instructions""")

        subprocess.run(
            [
                "powershell",
                "-ExecutionPolicy",
                "Bypass",
                "-File",
                "D:\AI Enginerring cource\Jet-Calc\Jet-Calc\\activation.ps1",
            ]
        )
        quit
        exit


if __name__ == "__main__":
    print("This is the activation file.")
    root = tk.Tk()
    root.geometry("400x400")
    tk.Label(text="After clicking to \"install requirmetns\":").pack()
    tk.Label(text="Go to the black window that you see ").pack()
    tk.Label(text="When it says to start the main programm: ").pack()
    tk.Label(text="Say no").pack()
    tk.Label(text="Because there is a error causing we are trying to resolve it.").pack()
    install_all = tk.Button(root, text="Install Requirments!!")
    massage = tk.Label()
    
    install_all.pack()
    massage.pack()

    install_all.bind("<Button-1>", Activate.install_build_requirments)
    print("Go back to the main window and close the programm we have sttoped the background files.")
    root.mainloop()
    # Activate.install_build_requirments()
