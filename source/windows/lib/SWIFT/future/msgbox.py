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
from tkinter import ttk

#from lib.API.widgets.flatbutton import FlatButton
#from flatbutton import FlatButton

class MsgBox(object):
    def __init__(self, master, title='', message='', msgtype='YESNO',
                 width=400, height=200):

        self.title = title
        self.message = message
        self.type = msgtype

        self.value = None

        # create the window
        self.msgbox_window = Toplevel(master)
        self.msgbox_window.wm_overrideredirect(True)
        self.msgbox_window.attributes("-alpha", 0.95)
        self.msgbox_window.configure(bg='grey40')
        self.msgbox_window.update_idletasks() # Actualize geometry information

        # calculate the placement of the window
        if master.winfo_ismapped():
            m_width = master.winfo_width()
            m_height = master.winfo_height()
            m_x = master.winfo_rootx()
            m_y = master.winfo_rooty()

        else:
            m_width = master.winfo_screenwidth()
            m_height = master.winfo_screenheight()
            m_x = m_y = 0
            
        w_width = self.msgbox_window.winfo_reqwidth()
        w_height = self.msgbox_window.winfo_reqheight()
        x = m_x + (m_width - w_width) * 0.5
        y = m_y + (m_height - w_height) * 0.3

        if x + w_width > master.winfo_screenwidth():
            x = master.winfo_screenwidth() - w_width

        elif x < 0:
            x = 0

        if y + w_height > master.winfo_screenheight():
            y = master.winfo_screenheight() - w_height

        elif y < 0:
            y = 0

        # place the window
        self.msgbox_window.wm_geometry("%dx%d+%d+%d" % (width, height, x, y))

        ## if a title was given, create it
        if self.title != None:
            title = Label(self.msgbox_window, text=self.title, bg='grey40',
                          justify=LEFT, fg='grey70', anchor=W, font=("Georgia", 11))
            title.pack(side=TOP)
        else:
            title = Label(self.msgbox_window, text='', bg='grey40',
                          justify=LEFT, fg='grey60', anchor=W, font=("Georgia", 11))
            title.pack(side=TOP)

        # separator
        SeparatorStyle = ttk.Style()
        SeparatorStyle.configure("MLine.TSeparator", background="grey20")
        Separator = ttk.Separator(self.msgbox_window, orient=HORIZONTAL,
                                  style="MLine.TSeparator")
        Separator.pack(padx=2, side=TOP, fill=X)

        # message
        message = Label(self.msgbox_window, text=self.message, bg='grey40',
                        justify=LEFT, fg='grey90', anchor=W, font=("Arial", 9))
        message.pack(padx=6, pady=6, side=TOP)

        if self.type == 'YESNO':

            btn_frm = Frame(self.msgbox_window, bg='grey40')
            btn_frm.pack(padx=4, pady=4, side=BOTTOM)
            
            btn1 = Button(btn_frm, text=' Yes ', command=self.return_true)
            btn1.pack(padx=6, pady=4, side=LEFT)

            btn2 = Button(btn_frm, text=' No ', command=self.return_false)
            btn2.pack(padx=6, pady=4, side=LEFT)


        #self.return_true()

    def get(self):
        self.msgbox_window.wait_visibility()
        print(self.value)
        return self.value
    
    
    def return_true(self):
        self.msgbox_window.destroy()
        self.value = True
        print(self.value)

    def return_false(self):
        self.msgbox_window.destroy()
        self.value = False
        print(self.value)
        
root = Tk()

a = MsgBox(root, "Save Edited Image?", """If you do not save the image, any change(s) to
the current image will be lost!
        
Would you like to save the current image before
creating a new one?""")

if a.get() == True:
    print("true")


root.mainloop()
