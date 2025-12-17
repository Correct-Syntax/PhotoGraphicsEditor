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
## The majority of this code is from Miguel Martinez Lopez

from tkinter import *
from tkinter.constants import *
from tkinter import ttk
from PIL import ImageTk

from lib.SWIFT.tooltip import ToolTip


class DockerFrame(Frame):
    def __init__(self, master, value, width=200, height=200, selection_handler=None,
                 drag_handler=None, drop_handler=None, icon=None, text='', **kwargs):
        Frame.__init__(self, master, class_=DockerFrame, **kwargs)
        
        self._x = None
        self._y = None
        
        self._width = width
        self._height = height

        self._tag = "item%s" % id(self)
        self._value = value
        self._icon = icon
        self._text = text

        self._selection_handler = selection_handler
        self._drag_handler = drag_handler
        self._drop_handler = drop_handler

    @property
    def x(self):
        return self._x
        
    @property
    def y(self):
        return self._y
        
    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height
        
    @property
    def value(self):
        return self._value
        
    def init(self, container, x, y):
        self._x = x
        self._y = y

        self.place(in_=container, x=x, y=y, width=self._width, height=self._height)

        ## Separator
        SeparatorStyle = ttk.Style()
        SeparatorStyle.configure("Line.TSeparator", background="black")
        Separator = ttk.Separator(self, orient=HORIZONTAL, style="Line.TSeparator")
        Separator.pack(pady=4, padx=4, side=TOP, fill=X)

        ## Title Frame
        self.DockerTitle_Frame = Frame(self, width=self._width, height=self._height, bg="#969696")
        self.DockerTitle_Frame.pack(side=TOP, fill=X)

        ## Main icon for the docker
        if self._icon != None:
            self.Icon = ImageTk.PhotoImage(file=self._icon)
            self.TitleIcon = Label(self.DockerTitle_Frame, image=self.Icon, bg="#969696")
            self.TitleIcon.pack(side=LEFT)

        else:
            self.TitleIcon = Label(self.DockerTitle_Frame, text='   ', bg="#969696")
            self.TitleIcon.pack(side=LEFT)   

        ## Written label for the docker
        self.TitleLabel = Label(self.DockerTitle_Frame, anchor=W, text=self._text,
                                bg="#969696", font=("Arial", 9))
        ToolTip(self.TitleLabel, "Docker name: {}".format(self._text))
        self.TitleLabel.pack(padx=4, side=LEFT)

        ## grip
        self.IconGrip = ImageTk.PhotoImage(file="lib/SWIFT/bitmaps/Grip.png")
        self.TitleFrameGrip = Label(self.DockerTitle_Frame, anchor=W, image=self.IconGrip,
                                    bg="#969696")
        self.TitleFrameGrip.pack(padx=4, side=RIGHT)

        ## interior
        self.interior = Frame(self, width=self._width, height=self._height, bg="#969696")
        self.interior.pack(expand=True, side=TOP, fill=X)#, pady=18)
        
        self.bind_class(self.TitleFrameGrip, "<ButtonPress-1>", self._on_selection)
        self.bind_class(self.TitleFrameGrip, "<B1-Motion>", self._on_drag)
        self.bind_class(self.TitleFrameGrip, "<ButtonRelease-1>", self._on_drop)

        self._add_bindtag(self)
        
        # Python3 compatibility: dict.values() return a view
        list_of_widgets = list(self.children.values())
        while len(list_of_widgets) != 0:
            widget = list_of_widgets.pop()
            list_of_widgets.extend(widget.children.values())
            
            self._add_bindtag(widget)
    
    def _add_bindtag(self, widget):
        bindtags = widget.bindtags()
        if self._tag not in bindtags:
            widget.bindtags((self._tag,) + bindtags)


    def _on_selection(self, event):
        self.tkraise()

        self._move_lastx = event.x_root
        self._move_lasty = event.y_root
        
        if self._selection_handler:
            self._selection_handler(self)

    def _on_drag(self, event):
        self.master.update_idletasks()
        
        cursor_x = self._x + event.x
        cursor_y = self._y + event.y

        self._x += event.x_root - self._move_lastx
        self._y += event.y_root - self._move_lasty

        self._move_lastx = event.x_root
        self._move_lasty = event.y_root

        self.place_configure(x=self._x, y=self._y)

        if self._drag_handler:
            self._drag_handler(cursor_x, cursor_y)
           
    def _on_drop(self, event):
        if self._drop_handler:
            self._drop_handler()
            
    def set_position(self, x,y):
        self._x = x
        self._y = y
        self.place_configure(x =x, y =y)
        
    def move(self, dx, dy):
        self._x += dx
        self._y += dy

        self.place_configure(x =self._x, y =self._y)


class DragDropDockerList(Frame):
    def __init__(self, master, item_width, item_height, item_relief=FLAT,
                 item_background="#969696", item_borderwidth=0, offset_x=0,
                 offset_y=0, gap=0, **kwargs):
        Frame.__init__(self, master, width=item_width+offset_x*2, height=offset_y*2, bg="#969696", **kwargs)

        self._item_borderwidth = item_borderwidth
        self._item_relief = item_relief
        self._item_background = item_background
        self._item_width = item_width
        self._item_height = item_height
        
        self._offset_x = offset_x
        self._offset_y = offset_y
               
        self._left = offset_x
        self._top = offset_y
        self._right = self._offset_x + self._item_width
        self._bottom = self._offset_y

        self._gap = gap

        self._index_of_selected_item = None
        self._index_of_empty_container = None

        self._list_of_items = []
        self._position = {}

        self._new_y_coord_of_selected_item = None

    def create_item(self, text='', icon=None, value=None, **kwargs):
        
        if self._item_relief is not None:
            kwargs.setdefault("relief", self._item_relief)
            
        if self._item_background is not None:
            kwargs.setdefault("background", self._item_background)

        item = DockerFrame(self.master, value, width=self._item_width, height=self._item_height,
                           selection_handler=self._on_item_selected,
                           drag_handler=self._on_item_dragged,
                           drop_handler=self._on_item_dropped,
                           icon=icon, text=text, **kwargs)   
        return item

    def configure_items(self, **kwargs):
        for item in self._list_of_items:
            item.configure(**kwargs)

    def add_item(self, item, index=None):
        if index is None:
            index = len(self._list_of_items)
        else:
            if not -len(self._list_of_items) < index < len(self._list_of_items):
                raise ValueError("Item index out of range")

            for i in range(index, len(self._list_of_items)):
                _item = self._list_of_items[i]
                _item.move(0,  self._item_height + self._gap)
                
                self._position[_item] += 1
        
        x = self._offset_x
        y = self._offset_y + index * (self._item_height + self._gap)

        self._list_of_items.insert(index, item)
        self._position[item] = index

        item.init(self, x, y)

        if len(self._list_of_items) == 1:
            self._bottom += self._item_height
        else:
            self._bottom += self._item_height + self._gap
            
        self.configure(height=self._bottom + self._offset_y)

        return item

    def delete_item(self, index):
        
        if isinstance(index, Item):
            index = self._position[index]
        else:
            if not -len(self._list_of_items) < index < len(self._list_of_items):
                raise ValueError("Item index out of range")

        item = self._list_of_items.pop(index)
        value = item.value

        del self._position[item]

        item.destroy()
        
        for i in range(index, len(self._list_of_items)):
            _item = self._list_of_items[i]
            _item.move(0,  -(self._item_height+self._gap))
            self._position[_item] -= 1
        
        if len(self._list_of_items) == 0:
            self._bottom -= self._item_height
        else:
            self._bottom -= self._item_height + self._gap

        self.configure(height=self._bottom + self._offset_y)
        
        return value

    del_item = delete_item
    
    def pop(self):
        return self.delete_item(-1)
        
    def shift(self):
        return self.delete_item(0)
        
    def append(self, item):
        self.add_item(item)
        
    def unshift(self, item):
        self.add_item(0, item)
        
    def get_item(self, index):
        return self._list_of_items[index]

    def get_value(self, index):
        return self._list_of_items[index].value

    def _on_item_selected(self, item):        
        self._index_of_selected_item = self._position[item]
        self._index_of_empty_container = self._index_of_selected_item

    def _on_item_dragged(self, x, y):

        if self._left < x < self._right and self._top < y < self._bottom:

            quotient, remainder = divmod(y-self._offset_y, self._item_height + self._gap)

            if remainder < self._item_height:
            
                new_container = quotient

                if new_container != self._index_of_empty_container:
                    if new_container > self._index_of_empty_container:
                        for index in range(self._index_of_empty_container+1, new_container+1, 1):
                            item = self._get_item_of_virtual_list(index)                            

                            item.move(0,-(self._item_height+self._gap))
                    else:
                        for index in range(self._index_of_empty_container-1, new_container-1, -1):
                            item = self._get_item_of_virtual_list(index)

                            item.move(0,self._item_height+self._gap)

                    self._index_of_empty_container = new_container
                    
    def _get_item_of_virtual_list(self, index):
        if self._index_of_empty_container == index:
            raise Exception("No item in index: %s"%index)
        else:
            if self._index_of_empty_container != self._index_of_selected_item:
                if index > self._index_of_empty_container:
                    index -= 1

                if index >= self._index_of_selected_item:
                    index += 1
            item = self._list_of_items[index]
            return item

    def _on_item_dropped(self):
        
        item = self._list_of_items.pop(self._index_of_selected_item)
        self._list_of_items.insert(self._index_of_empty_container, item)
        
        x = self._offset_x
        y = self._offset_y + self._index_of_empty_container *(self._item_height + self._gap)
        
        item.set_position(x,y)
        
        for i in range(min(self._index_of_selected_item, self._index_of_empty_container),max(self._index_of_selected_item, self._index_of_empty_container)+1):
            item = self._list_of_items[i]
            self._position[item] = i
            
        self._index_of_empty_container = None
        self._index_of_selected_item = None
