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

        
class Notebook(object):
    """ Create a notebook widget (tabs).

    Parameters
    ----------
    master:
      widget to place notebook into
    side:
      what side of the notebook to pack the tabs

    Notes
    -----
    Pack your widgets before adding the frame 
    to the notebook (not the frame itself, though)!
    """
    def __init__(self, master, side=TOP):

        ## variables
        self.active_frame = None
        self.count = 0
        self.side = side
        self.choice = IntVar(0)

        ## position of tabs around the frame(s)
        if side in (TOP, BOTTOM):
            self.side = LEFT
        else:
            self.side = TOP

        ## create the tabs frame
        self.tabs_frame = Frame(master, bg="grey40")
        self.tabs_frame.pack(side=side, fill=BOTH)

        ## create the frame for the tabs
        self.frame = Frame(master, bg="grey40")
        self.frame.pack(expand=True, fill=BOTH)

                
    def add_tab(self, frame, title, image=None):
        ## frame to create border effect
        borderframe = Frame(self.tabs_frame, bg="#969696")
        borderframe.pack(side=LEFT)
        
        ## add a new frame (tab) to the notebook
        tab = Radiobutton(
            borderframe,
            text=title,
            indicatoron=False,
            variable=self.choice,
            value=self.count, 
            bg="grey50",
            bd=0,
            selectcolor="#969696",
            activebackground="#94afc9",
            command=lambda: self._display(frame)
            )

        ## if there is an icon
        if image != None:
            tab.configure(image=image, compound=LEFT)
            
        tab.pack(fill=BOTH, side=self.side)

        ## we want the first tab to be selected first
        if not self.active_frame:
            frame.pack(fill=BOTH, expand=True)
            self.active_frame = frame

        self.count += 1

        ## return a reference to the tab     
        return tab, borderframe


    def _display(self, frame):
        ## hide the last active tab
        self.active_frame.forget()

        ## show the active tab
        frame.pack(fill=BOTH, expand=True)
        self.active_frame = frame

    
    def __call__(self):
        ## return a reference of the frame 
        return self.frame


## example code
if __name__ == '__main__':

    root = Tk()
    n = Notebook(root, TOP)

    f1 = Frame(n(), bg="#969696")
    b1 = Button(f1, text="Button 1")
    b1.pack(fill=BOTH, expand=1)

    f2 = Frame(n(), bg="#969696")
    b2 = Button(f2, text='Button 2')
    b3 = Button(f2, text='Button')
    b2.pack(fill=BOTH, expand=1, padx=4, pady=50)
    b3.pack(fill=BOTH, expand=1)

    f3 = Frame(n(), bg="#969696")

    x1 = n.add_tab(f1, "Screen 1")
    n.add_tab(f2, "Screen 2")
    n.add_tab(f3, " hello ")

    root.mainloop()
