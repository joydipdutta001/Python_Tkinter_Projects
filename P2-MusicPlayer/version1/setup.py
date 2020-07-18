import sys
import cx_Freeze

# Dependencies are automatically detected, but it might need fine tuning.
executables = [cx_Freeze.Executable("main.py")]
# GUI applications require a different base on Windows (the default is for a
# console application).

cx_Freeze.setup(  name = "musically",
        version = "0.1",
        description = "Music Player by Cybotians",
        options = {"build_exe": {"packages":["pygame","os","tkinter","mutagen","ttkthemes","threading"],
                                               "include_files":["./images/"]}},
        executables = executables)
