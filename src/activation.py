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


if __name__ == "__main__":
    print("This is the activation file.")
    root = tk.Tk()
    root.geometry("150x150")
    install_all = tk.Button(root, text="Install Requirments!!")
    exit_window = tk.Button(root, text="Exit")
    massage = tk.Label()
    
    install_all.pack()
    massage.pack()
    exit_window.pack()

    install_all.bind("<Button-1>", Activate.install_build_requirments)
    exit_window.bind("<Button-2>", exit)
    root.mainloop()
    # Activate.install_build_requirments()
