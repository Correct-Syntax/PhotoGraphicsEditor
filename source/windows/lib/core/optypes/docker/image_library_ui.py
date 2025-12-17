## This code is Copyright (C) 2019 Noah Rahm
##
## This program is free software: you can redistribute it and/or modify it 
## under the terms of the GNU General Public License as published by 
## the Free Software Foundation; either version 3 of the License, 
## or (at your option) any later version.
##
## This program is distributed in the hope that it will be useful, 
## but WITHOUT ANY WARRANTY; without even the implied warranty 
## of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
## GNU General Public License for more details.
##
## You should have received a copy of the GNU General Public License 
## along with this program. If not, see: http://www.gnu.org/licenses/
##
## Contributor(s): Noah Rahm

from tkinter import *
from tkinter.constants import *
from tkinter import ttk
from PIL import ImageTk

from lib.SWIFT.tooltip import ToolTip
from lib.SWIFT.flatbutton import FlatButton


def docker_image_library_ui(self):
    ## create the docker
    self.ImageLibrary_Docker = self.Docker_Panel.create_item(text='Image Library',
                                                             value='Image Library Docker',
                                                             icon="lib/datafiles/icons/interface/ImageLibraryDocker.png")

    ## add the docker
    self.Docker_Panel.add_item(self.ImageLibrary_Docker)

    ## create the preview canvas
    ImagePreview_Frame = Frame(self.ImageLibrary_Docker.interior, bd=1, relief=SOLID)
    ImagePreview_Frame.pack()

    ## main frame
    self.BaseImageSelector_Frame = Frame(ImagePreview_Frame, bg="grey80")
    self.BaseImageSelector_Frame.pack(fill=BOTH, side=TOP)

    self.ImageSelectorCanvas = Canvas(self.BaseImageSelector_Frame, highlightthickness=0,
                                      width=200, height=200, bg="#969696")
    self.ImageSelector_Frame = Frame(self.BaseImageSelector_Frame, bd=0, bg="#969696")
    self.ImageSelector_Frame.pack(expand=True, fill=BOTH)
    ImageSelectorScrollbar = Scrollbar(self.BaseImageSelector_Frame, orient=VERTICAL,
                             command=self.ImageSelectorCanvas.yview)
    self.ImageSelectorCanvas.configure(yscrollcommand=ImageSelectorScrollbar.set)
    ImageSelectorScrollbar.pack(side=RIGHT, fill=Y)
    self.ImageSelectorCanvas.pack(side=LEFT, fill=BOTH, expand=True)

    self.ImageSelectorCanvas.create_window((0, 0), window=self.ImageSelector_Frame, anchor=N)

    self.ImageSelector_Frame.bind("<Configure>", lambda event: config_frame(self))

    ## buttons
    self.ImageSelection_Var = IntVar()
    self.ImageSelection_Var.set(1)

    self.ICON_IMG001 = ImageTk.PhotoImage(file="lib/datafiles/icons/interface/imglib/img_001.png")
    self.IMG001_Radiobtn = Radiobutton(self.ImageSelector_Frame,
                                       value=1,
                                       indicatoron=False,
                                       image=self.ICON_IMG001,
                                       relief=GROOVE,
                                       offrelief=SOLID,
                                       variable=self.ImageSelection_Var,
                                       selectcolor='grey40',
                                       bd=1,
                                       bg="#969696",
                                       font=("Arial", 8),
                                       activebackground='#969696',
                                       command=lambda:select_image(self))
    self.IMG001_Radiobtn.grid(row=0, column=0, padx=6, pady=4)
    ToolTip(self.IMG001_Radiobtn, "img_001 (1024X1024)")

    self.ICON_IMG002 = ImageTk.PhotoImage(file="lib/datafiles/icons/interface/imglib/img_002.png")
    self.IMG002_Radiobtn = Radiobutton(self.ImageSelector_Frame, value=2,
                                        indicatoron=False,
                                        image=self.ICON_IMG002,
                                        offrelief=SOLID,
                                        relief=SOLID,
                                        variable=self.ImageSelection_Var,
                                        selectcolor='grey40', bd=1,
                                        bg="#969696", font=("Arial", 8),
                                        activebackground='#969696',
                                        command=lambda:select_image(self))
    self.IMG002_Radiobtn.grid(row=0, column=1, padx=6, pady=4)
    ToolTip(self.IMG002_Radiobtn, "img_002 (1024X1024)")

    self.ICON_IMG003 = ImageTk.PhotoImage(file="lib/datafiles/icons/interface/imglib/img_003.png")
    self.IMG003_Radiobtn = Radiobutton(self.ImageSelector_Frame, value=3,
                                        indicatoron=False,
                                        image=self.ICON_IMG003,
                                        offrelief=SOLID,
                                        relief=SOLID,
                                        variable=self.ImageSelection_Var,
                                        selectcolor='grey40', bd=1,
                                        bg="#969696", font=("Arial", 8),
                                        activebackground='#969696',
                                        command=lambda:select_image(self))
    self.IMG003_Radiobtn.grid(row=0, column=2, padx=6, pady=4)
    ToolTip(self.IMG003_Radiobtn, "img_003 (1024X1024)")

    self.ICON_IMG004 = ImageTk.PhotoImage(file="lib/datafiles/icons/interface/imglib/img_004.png")
    self.IMG004_Radiobtn = Radiobutton(self.ImageSelector_Frame, value=4,
                                        indicatoron=False,
                                        image=self.ICON_IMG004,
                                        offrelief=SOLID,
                                        relief=SOLID,
                                        variable=self.ImageSelection_Var,
                                        selectcolor='grey40', bd=1,
                                        bg="#969696", font=("Arial", 8),
                                        activebackground='#969696',
                                        command=lambda:select_image(self))
    self.IMG004_Radiobtn.grid(row=0, column=3, padx=6, pady=4)
    ToolTip(self.IMG004_Radiobtn, "img_004 (1024X1024)")

    self.ICON_IMG005 = ImageTk.PhotoImage(file="lib/datafiles/icons/interface/imglib/img_005.png")
    self.IMG005_Radiobtn = Radiobutton(self.ImageSelector_Frame, value=5,
                                        indicatoron=False,
                                        image=self.ICON_IMG005,
                                        offrelief=SOLID,
                                        relief=SOLID,
                                        variable=self.ImageSelection_Var,
                                        selectcolor='grey40', bd=1,
                                        bg="#969696", font=("Arial", 8),
                                        activebackground='#969696',
                                        command=lambda:select_image(self))
    self.IMG005_Radiobtn.grid(row=1, column=0, padx=6, pady=4)
    ToolTip(self.IMG005_Radiobtn, "img_005 (1024X1024)")

    self.ICON_IMG006 = ImageTk.PhotoImage(file="lib/datafiles/icons/interface/imglib/img_006.png")
    self.IMG006_Radiobtn = Radiobutton(self.ImageSelector_Frame, value=6,
                                        indicatoron=False,
                                        image=self.ICON_IMG006,
                                        offrelief=SOLID,
                                        relief=SOLID,
                                        variable=self.ImageSelection_Var,
                                        selectcolor='grey40', bd=1,
                                        bg="#969696", font=("Arial", 8),
                                        activebackground='#969696',
                                        command=lambda:select_image(self))
    self.IMG006_Radiobtn.grid(row=1, column=1, padx=6, pady=4)
    ToolTip(self.IMG006_Radiobtn, "img_006 (1024X1024)")

    self.ICON_IMG007 = ImageTk.PhotoImage(file="lib/datafiles/icons/interface/imglib/img_007.png")
    self.IMG007_Radiobtn = Radiobutton(self.ImageSelector_Frame, value=7,
                                        indicatoron=False,
                                        image=self.ICON_IMG007,
                                        offrelief=SOLID,
                                        relief=SOLID,
                                        variable=self.ImageSelection_Var,
                                        selectcolor='grey40', bd=1,
                                        bg="#969696", font=("Arial", 8),
                                        activebackground='#969696',
                                        command=lambda:select_image(self))
    self.IMG007_Radiobtn.grid(row=1, column=2, padx=6, pady=4)
    ToolTip(self.IMG007_Radiobtn, "img_007 (1024X1024)")

    self.ICON_IMG008 = ImageTk.PhotoImage(file="lib/datafiles/icons/interface/imglib/img_008.png")
    self.IMG008_Radiobtn = Radiobutton(self.ImageSelector_Frame, value=8,
                                        indicatoron=False,
                                        image=self.ICON_IMG008,
                                        offrelief=SOLID,
                                        relief=SOLID,
                                        variable=self.ImageSelection_Var,
                                        selectcolor='grey40', bd=1,
                                        bg="#969696", font=("Arial", 8),
                                        activebackground='#969696',
                                        command=lambda:select_image(self))
    self.IMG008_Radiobtn.grid(row=1, column=3, padx=6, pady=4)
    ToolTip(self.IMG008_Radiobtn, "img_008 (1024X1024)")

    self.ICON_IMG009 = ImageTk.PhotoImage(file="lib/datafiles/icons/interface/imglib/img_009.png")
    self.IMG009_Radiobtn = Radiobutton(self.ImageSelector_Frame, value=9,
                                        indicatoron=False,
                                        image=self.ICON_IMG009,
                                        offrelief=SOLID,
                                        relief=SOLID,
                                        variable=self.ImageSelection_Var,
                                        selectcolor='grey40', bd=1,
                                        bg="#969696", font=("Arial", 8),
                                        activebackground='#969696',
                                        command=lambda:select_image(self))
    self.IMG009_Radiobtn.grid(row=2, column=0, padx=6, pady=4)
    ToolTip(self.IMG009_Radiobtn, "img_009 (1024X1024)")

    self.ICON_IMG010 = ImageTk.PhotoImage(file="lib/datafiles/icons/interface/imglib/img_010.png")
    self.IMG010_Radiobtn = Radiobutton(self.ImageSelector_Frame, value=10,
                                        indicatoron=False,
                                        image=self.ICON_IMG010,
                                        offrelief=SOLID,
                                        relief=SOLID,
                                        variable=self.ImageSelection_Var,
                                        selectcolor='grey40', bd=1,
                                        bg="#969696", font=("Arial", 8),
                                        activebackground='#969696',
                                        command=lambda:select_image(self))
    self.IMG010_Radiobtn.grid(row=2, column=1, padx=6, pady=4)
    ToolTip(self.IMG010_Radiobtn, "img_010 (1024X1024)")

    self.ICON_IMG011 = ImageTk.PhotoImage(file="lib/datafiles/icons/interface/imglib/img_011.png")
    self.IMG011_Radiobtn = Radiobutton(self.ImageSelector_Frame, value=11,
                                        indicatoron=False,
                                        image=self.ICON_IMG011,
                                        offrelief=SOLID,
                                        relief=SOLID,
                                        variable=self.ImageSelection_Var,
                                        selectcolor='grey40', bd=1,
                                        bg="#969696", font=("Arial", 8),
                                        activebackground='#969696',
                                        command=lambda:select_image(self))
    self.IMG011_Radiobtn.grid(row=2, column=2, padx=6, pady=4)
    ToolTip(self.IMG011_Radiobtn, "img_011 (1024X1024)")

    self.ICON_IMG012 = ImageTk.PhotoImage(file="lib/datafiles/icons/interface/imglib/img_012.png")
    self.IMG012_Radiobtn = Radiobutton(self.ImageSelector_Frame, value=12,
                                        indicatoron=False,
                                        image=self.ICON_IMG012,
                                        offrelief=SOLID,
                                        relief=SOLID,
                                        variable=self.ImageSelection_Var,
                                        selectcolor='grey40', bd=1,
                                        bg="#969696", font=("Arial", 8),
                                        activebackground='#969696',
                                        command=lambda:select_image(self))
    self.IMG012_Radiobtn.grid(row=2, column=3, padx=6, pady=4)
    ToolTip(self.IMG012_Radiobtn, "img_012 (1024X1024)")

    self.ICON_IMG013 = ImageTk.PhotoImage(file="lib/datafiles/icons/interface/imglib/img_013.png")
    self.IMG013_Radiobtn = Radiobutton(self.ImageSelector_Frame, value=13,
                                        indicatoron=False,
                                        image=self.ICON_IMG013,
                                        offrelief=SOLID,
                                        relief=SOLID,
                                        variable=self.ImageSelection_Var,
                                        selectcolor='grey40', bd=1,
                                        bg="#969696", font=("Arial", 8),
                                        activebackground='#969696',
                                        command=lambda:select_image(self))
    self.IMG013_Radiobtn.grid(row=3, column=0, padx=6, pady=4)
    ToolTip(self.IMG013_Radiobtn, "img_013 (1024X1024)")

    self.ICON_IMG014 = ImageTk.PhotoImage(file="lib/datafiles/icons/interface/imglib/img_014.png")
    self.IMG014_Radiobtn = Radiobutton(self.ImageSelector_Frame, value=14,
                                        indicatoron=False,
                                        image=self.ICON_IMG014,
                                        offrelief=SOLID,
                                        relief=SOLID,
                                        variable=self.ImageSelection_Var,
                                        selectcolor='grey40', bd=1,
                                        bg="#969696", font=("Arial", 8),
                                        activebackground='#969696',
                                        command=lambda:select_image(self))
    self.IMG014_Radiobtn.grid(row=3, column=1, padx=6, pady=4)
    ToolTip(self.IMG014_Radiobtn, "img_014 (1024X1024)")

    self.ICON_IMG015 = ImageTk.PhotoImage(file="lib/datafiles/icons/interface/imglib/img_015.png")
    self.IMG015_Radiobtn = Radiobutton(self.ImageSelector_Frame, value=15,
                                        indicatoron=False,
                                        image=self.ICON_IMG015,
                                        offrelief=SOLID,
                                        relief=SOLID,
                                        variable=self.ImageSelection_Var,
                                        selectcolor='grey40', bd=1,
                                        bg="#969696", font=("Arial", 8),
                                        activebackground='#969696',
                                        command=lambda:select_image(self))
    self.IMG015_Radiobtn.grid(row=3, column=2, padx=6, pady=4)
    ToolTip(self.IMG015_Radiobtn, "img_015 (1024X1024)")

    self.ICON_IMG016 = ImageTk.PhotoImage(file="lib/datafiles/icons/interface/imglib/img_016.png")
    self.IMG016_Radiobtn = Radiobutton(self.ImageSelector_Frame, value=16,
                                        indicatoron=False,
                                        image=self.ICON_IMG016,
                                        offrelief=SOLID,
                                        relief=SOLID,
                                        variable=self.ImageSelection_Var,
                                        selectcolor='grey40', bd=1,
                                        bg="#969696", font=("Arial", 8),
                                        activebackground='#969696',
                                        command=lambda:select_image(self))
    self.IMG016_Radiobtn.grid(row=3, column=3, padx=6, pady=4)
    ToolTip(self.IMG016_Radiobtn, "img_016 (1024X1024)")

    self.ICON_IMG017 = ImageTk.PhotoImage(file="lib/datafiles/icons/interface/imglib/img_017.png")
    self.IMG017_Radiobtn = Radiobutton(self.ImageSelector_Frame, value=17,
                                        indicatoron=False,
                                        image=self.ICON_IMG017,
                                        offrelief=SOLID,
                                        relief=SOLID,
                                        variable=self.ImageSelection_Var,
                                        selectcolor='grey40', bd=1,
                                        bg="#969696", font=("Arial", 8),
                                        activebackground='#969696',
                                        command=lambda:select_image(self))
    self.IMG017_Radiobtn.grid(row=4, column=0, padx=6, pady=4)
    ToolTip(self.IMG017_Radiobtn, "img_017 (1024X1024)")

    self.ICON_IMG018 = ImageTk.PhotoImage(file="lib/datafiles/icons/interface/imglib/img_018.png")
    self.IMG018_Radiobtn = Radiobutton(self.ImageSelector_Frame, value=18,
                                        indicatoron=False,
                                        image=self.ICON_IMG018,
                                        offrelief=SOLID,
                                        relief=SOLID,
                                        variable=self.ImageSelection_Var,
                                        selectcolor='grey40', bd=1,
                                        bg="#969696", font=("Arial", 8),
                                        activebackground='#969696',
                                        command=lambda:select_image(self))
    self.IMG018_Radiobtn.grid(row=4, column=1, padx=6, pady=4)
    ToolTip(self.IMG018_Radiobtn, "img_018 (1024X1024)")

    self.ICON_IMG019 = ImageTk.PhotoImage(file="lib/datafiles/icons/interface/imglib/img_019.png")
    self.IMG019_Radiobtn = Radiobutton(self.ImageSelector_Frame, value=19,
                                        indicatoron=False,
                                        image=self.ICON_IMG019,
                                        offrelief=SOLID,
                                        relief=SOLID,
                                        variable=self.ImageSelection_Var,
                                        selectcolor='grey40', bd=1,
                                        bg="#969696", font=("Arial", 8),
                                        activebackground='#969696',
                                        command=lambda:select_image(self))
    self.IMG019_Radiobtn.grid(row=4, column=2, padx=6, pady=4)
    ToolTip(self.IMG019_Radiobtn, "img_019 (1024X1024)")

    self.ICON_IMG020 = ImageTk.PhotoImage(file="lib/datafiles/icons/interface/imglib/img_020.png")
    self.IMG020_Radiobtn = Radiobutton(self.ImageSelector_Frame, value=20,
                                        indicatoron=False,
                                        image=self.ICON_IMG020,
                                        offrelief=SOLID,
                                        relief=SOLID,
                                        variable=self.ImageSelection_Var,
                                        selectcolor='grey40', bd=1,
                                        bg="#969696", font=("Arial", 8),
                                        activebackground='#969696',
                                        command=lambda:select_image(self))
    self.IMG020_Radiobtn.grid(row=4, column=3, padx=6, pady=4)
    ToolTip(self.IMG020_Radiobtn, "img_020 (1024X1024)")

    self.ICON_IMG021 = ImageTk.PhotoImage(file="lib/datafiles/icons/interface/imglib/img_021.png")
    self.IMG021_Radiobtn = Radiobutton(self.ImageSelector_Frame, value=21,
                                        indicatoron=False,
                                        image=self.ICON_IMG021,
                                        offrelief=SOLID,
                                        relief=SOLID,
                                        variable=self.ImageSelection_Var,
                                        selectcolor='grey40', bd=1,
                                        bg="#969696", font=("Arial", 8),
                                        activebackground='#969696',
                                        command=lambda:select_image(self))
    self.IMG021_Radiobtn.grid(row=5, column=0, padx=6, pady=4)
    ToolTip(self.IMG021_Radiobtn, "img_021 (512X512)")

    self.ICON_IMG022 = ImageTk.PhotoImage(file="lib/datafiles/icons/interface/imglib/img_022.png")
    self.IMG022_Radiobtn = Radiobutton(self.ImageSelector_Frame, value=22,
                                        indicatoron=False,
                                        image=self.ICON_IMG022,
                                        offrelief=SOLID,
                                        relief=SOLID,
                                        variable=self.ImageSelection_Var,
                                        selectcolor='grey40', bd=1,
                                        bg="#969696", font=("Arial", 8),
                                        activebackground='#969696',
                                        command=lambda:select_image(self))
    self.IMG022_Radiobtn.grid(row=5, column=1, padx=6, pady=4)
    ToolTip(self.IMG022_Radiobtn, "img_022 (200X200)")

    self.ICON_IMG023 = ImageTk.PhotoImage(file="lib/datafiles/icons/interface/imglib/img_023.png")
    self.IMG023_Radiobtn = Radiobutton(self.ImageSelector_Frame, value=23,
                                        indicatoron=False,
                                        image=self.ICON_IMG023,
                                        offrelief=SOLID,
                                        relief=SOLID,
                                        variable=self.ImageSelection_Var,
                                        selectcolor='grey40', bd=1,
                                        bg="#969696", font=("Arial", 8),
                                        activebackground='#969696',
                                        command=lambda:select_image(self))
    self.IMG023_Radiobtn.grid(row=5, column=2, padx=6, pady=4)
    ToolTip(self.IMG023_Radiobtn, "img_023 (798X798)")

    self.ICON_IMG024 = ImageTk.PhotoImage(file="lib/datafiles/icons/interface/imglib/img_024.png")
    self.IMG024_Radiobtn = Radiobutton(self.ImageSelector_Frame, value=24,
                                        indicatoron=False,
                                        image=self.ICON_IMG024,
                                        offrelief=SOLID,
                                        relief=SOLID,
                                        variable=self.ImageSelection_Var,
                                        selectcolor='grey40', bd=1,
                                        bg="#969696", font=("Arial", 8),
                                        activebackground='#969696',
                                        command=lambda:select_image(self))
    self.IMG024_Radiobtn.grid(row=5, column=3, padx=6, pady=4)
    ToolTip(self.IMG024_Radiobtn, "img_024 (512X512)")

    self.ICON_IMG025 = ImageTk.PhotoImage(file="lib/datafiles/icons/interface/imglib/img_025.png")
    self.IMG025_Radiobtn = Radiobutton(self.ImageSelector_Frame, value=25,
                                        indicatoron=False,
                                        image=self.ICON_IMG025,
                                        offrelief=SOLID,
                                        relief=SOLID,
                                        variable=self.ImageSelection_Var,
                                        selectcolor='grey40', bd=1,
                                        bg="#969696", font=("Arial", 8),
                                        activebackground='#969696',
                                        command=lambda:select_image(self))
    self.IMG025_Radiobtn.grid(row=6, column=0, padx=6, pady=4)
    ToolTip(self.IMG025_Radiobtn, "img_025 (512X512)")

    self.ICON_IMG026 = ImageTk.PhotoImage(file="lib/datafiles/icons/interface/imglib/img_026.png")
    self.IMG026_Radiobtn = Radiobutton(self.ImageSelector_Frame, value=26,
                                        indicatoron=False,
                                        image=self.ICON_IMG026,
                                        offrelief=SOLID,
                                        relief=SOLID,
                                        variable=self.ImageSelection_Var,
                                        selectcolor='grey40', bd=1,
                                        bg="#969696", font=("Arial", 8),
                                        activebackground='#969696',
                                        command=lambda:select_image(self))
    self.IMG026_Radiobtn.grid(row=6, column=1, padx=6, pady=4)
    ToolTip(self.IMG026_Radiobtn, "img_026 (512X512)")

    self.ICON_IMG027 = ImageTk.PhotoImage(file="lib/datafiles/icons/interface/imglib/img_027.png")
    self.IMG027_Radiobtn = Radiobutton(self.ImageSelector_Frame, value=27,
                                        indicatoron=False,
                                        image=self.ICON_IMG027,
                                        offrelief=SOLID,
                                        relief=SOLID,
                                        variable=self.ImageSelection_Var,
                                        selectcolor='grey40', bd=1,
                                        bg="#969696", font=("Arial", 8),
                                        activebackground='#969696',
                                        command=lambda:select_image(self))
    self.IMG027_Radiobtn.grid(row=6, column=2, padx=6, pady=4)
    ToolTip(self.IMG027_Radiobtn, "img_027 (512X512)")

    self.ICON_IMG028 = ImageTk.PhotoImage(file="lib/datafiles/icons/interface/imglib/img_028.png")
    self.IMG028_Radiobtn = Radiobutton(self.ImageSelector_Frame, value=28,
                                        indicatoron=False,
                                        image=self.ICON_IMG028,
                                        offrelief=SOLID,
                                        relief=SOLID,
                                        variable=self.ImageSelection_Var,
                                        selectcolor='grey40', bd=1,
                                        bg="#969696", font=("Arial", 8),
                                        activebackground='#969696',
                                        command=lambda:select_image(self))
    self.IMG028_Radiobtn.grid(row=6, column=3, padx=6, pady=4)
    ToolTip(self.IMG028_Radiobtn, "img_028 (512X512)")


def config_frame(self):
    self.ImageSelectorCanvas.configure(scrollregion=self.ImageSelectorCanvas.bbox("all"))


def select_image(self):
    ImageSelection = int(self.ImageSelection_Var.get())

    ## we want to make sure the leading zeros does not cause problems
    if ImageSelection < 10:
        self.data.selectedimagefromlib = "lib/datafiles/imglib/img_00{}.png".format(ImageSelection)

    else:
        self.data.selectedimagefromlib = "lib/datafiles/imglib/img_0{}.png".format(ImageSelection)

