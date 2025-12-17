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


class ContextMenu(object):
   """ Context Menu widget.

    Parameters
    ----------
    widget:
      Widget to place this widget into
    x:
      X value of where to have the widget appear
    y:
      Y value of where to have the widget appear
    options:
      List of options for the menu (as strings)
    commands:
      Commands for each of the specified options as a dict, with the key being the
      option specified in the 'options' parameter
      Example: ...options=['Print'], commands={'Print':print_out(self)}...
    width:
      Width of the context menu
    title:
      Title of the context menu
    """
   def __init__(self, widget, x, y, options=[], commands={}, width=10, title=''):
      self.widget = widget
      self.options = options
      self.commands = commands
      self.width = width
      self.title = title

      ## create a toplevel window
      self.tplvl = Toplevel(self.widget)
      self.tplvl.wm_overrideredirect(True)
      self.tplvl.wm_geometry("+%d+%d" % (x, y))

      ## Make the menu to have some transparency and color
      self.tplvl.attributes("-alpha", 0.9)
      self.tplvl.configure(bg='grey40')

      ## Modifier Frame
      Modifier_Frame = Frame(self.tplvl, bg='grey40')
      Modifier_Frame.pack(padx=4, side=TOP, fill=X)

      ## Modifier Title
      ModifierTitle_Label = Label(
         Modifier_Frame,
         bg='grey40',
         fg='grey70',
         font=("Arial", 8),
         text=self.title,
         anchor=W
         )
      ModifierTitle_Label.pack(side=TOP, fill=BOTH)

      ## Separator
      ModifierSeparator = ttk.Separator(Modifier_Frame, orient=HORIZONTAL,
                                       style="Line.TSeparator")
      ModifierSeparator.pack(padx=2, side=TOP, fill=X)

      ## Search entry
      self.SearchModifiers_Var = StringVar()
      self.SearchModifiers_Var.trace('w', lambda name, index, mode: self.update_listbox())
      self.SearchModifiers_Entry = Entry(
         Modifier_Frame,
         textvariable=self.SearchModifiers_Var,
         width=16,
         selectbackground='#94afc9',
         bg='grey70',
         fg='black',
         font=("Calibri", 11),
         selectforeground='white',
         insertbackground='grey40'
         )
      self.SearchModifiers_Entry.pack(pady=6, padx=2, side=TOP, fill=X)

      ## Listbox
      self.ModifiersMenu_Listbox = Listbox(
         Modifier_Frame,
         bg='grey40',
         fg='white',
         font=("Calibri", 10),
         highlightbackground='grey40',
         highlightcolor='grey40',
         width=self.width + 2,
         height=10,
         relief=FLAT,
         activestyle='none',
         selectbackground='#94afc9',
         selectforeground='black'
         )
      self.ModifiersMenu_Listbox.pack(side=TOP, fill=BOTH)

      ## configure the height to be the number of lines
      self.ModifiersMenu_Listbox.configure(height=self.ModifiersMenu_Listbox.size())

      ## update the listbox according to the search 
      self.update_listbox()

      ## binding to get the option
      self.ModifiersMenu_Listbox.bind("<Double-Button-1>", lambda event: self.hide_menu())

      ## bindings to destroy the menu
      Modifier_Frame.bind("<Leave>", self.hide_menu)
      self.widget.bind("<Button-1>", lambda event: self.hide_menu())


   def update_listbox(self):
      ## setup to update list
      searched_var = self.SearchModifiers_Var.get()
      self.ModifiersMenu_Listbox.delete(0, END)

      ## add the options that match the search to the listbox
      for item in self.options:
         if searched_var.lower() in item.lower():
             self.ModifiersMenu_Listbox.insert(END, item)
                

   def hide_menu(self, event=None):
      try:
         ## Get the current selection
         sel = self.ModifiersMenu_Listbox.get(ACTIVE)

         ## get the command from the dict
         command = self.commands[sel]

         ## Run a command, if there was one specified
         if command != None:
             command()

         ## Destroy the menu
         self.tplvl.destroy()

         ## unbind binding
         self.widget.unbind("<Button-1>")

      except:
         ## Destroy the menu
         self.tplvl.destroy()

         ## unbind binding
         self.widget.unbind("<Button-1>")


 ## example of use:
from contextmenu import ContextMenu

def layer_img():
    print('printing layer')


def prev_img():
    print('prev')

def modifier_context_menu(self, event):
    if self.data.image != None:
        ContextMenu(self, event.x, event.y, options=['Layer', 'Add Text'],
                    title='Add Modifier:',
                    commands={
                        'Layer':layer_img,
                        'Add Text': prev_img
                        }
                    )
