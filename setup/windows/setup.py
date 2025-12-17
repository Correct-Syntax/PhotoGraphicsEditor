#!python3

import sys
from cx_Freeze import setup, Executable

base = None
if sys.platform == 'win32':
    base = 'Win32GUI'

executables = [
    Executable('C:/SETUP/PHOTO/PhotoGraphics Editor.py', base=base, icon="C:/SETUP/PHOTO/lib/datafiles/icons/program/Program_Icon.ico")
]



setup(name='PhotoGraphics Editor',
      version='0.1.0',
      options={"build_exe": {"packages": ["tkinter", "PIL", "numpy", "scipy", "collections", "ctypes", "imghdr"], "excludes": ["matplotlib", "PySide", "wx", "win32", "pywin", "win32com", "email", "html", "multiprocessing", "http", "win32api", "win32evtlog", "win32pdh"], "include_files": ["C:/SETUP/PHOTO/lib", "C:/SETUP/PHOTO/__plugins__"]}},
      description='PhotoGraphics Editor version 1.1.0',
      executables=executables

)
