
from tkinter import *


class LoadingBar(Toplevel):
    def __init__(self, master=None, text='Loading...', minvalue=0, maxvalue=100, height=40,
                 width=100, value=0.1, labelformat="%d%%", labeltext=''):
        Toplevel.__init__(self, master)

        self.title(text)
        self.geometry('300x30')
        
        ## define variables
        self.minvalue = minvalue
        self.maxvalue = maxvalue
        self.width = width
        self.height = height
        self.value = value
        self.labelformat = labelformat
        self.labeltext = labeltext
        self.dolabel = 1
        
        ## create loadingbar
        self.frame = Frame(self, relief=SOLID, bd=0.5, width=self.width)
        self.canvas = Canvas(self.frame, bd=0, highlightthickness=0, bg='white',
                             width=self.width, height=self.height)
        self.canvas.pack(fill=BOTH)
        self.scale = self.canvas.create_rectangle(0, 0, self.width, self.height, fill='green')
        self.label = self.canvas.create_text(self.width/2, self.height/2, text=self.labeltext,
                                             anchor=CENTER)
        
        self.update()
        self.canvas.bind('<Configure>', self.on_resize) # monitor size changes


    def pack(self, *args, **kw):
        self.frame.pack(*args, **kw)


    def on_resize(self, event):
        if (self.width == event.width) and (self.height == event.height):
          return
        
        # Set new sizes
        self.width  = event.width
        self.height = event.height
        
        # Move label
        self.canvas.coords(self.label, event.width/2, event.height/2)

        # Display bar in new sizes
        self.update()
    
    def update_progress(self, newvalue, newmaxvalue=None):
        if newmaxvalue:
          self.max = newmaxvalue
        self.value = newvalue
        self.update()


    def update(self):
        # Trim the values to be between min and max
        value = self.value
        if value > self.maxvalue:
          value = self.maxvalue
        if value < self.minvalue:
          value = self.minvalue
          
        # Adjust the rectangle
        self.canvas.coords(self.scale, 0, 0, float(value) / self.maxvalue * self.width, self.height)

        # And update the label
        if self.dolabel:
          if value:
            if value >= 0:
              pvalue = int((float(value) / float(self.maxvalue)) * 100.0)
            else:
              pvalue = 0
            self.canvas.itemconfig(self.label, text=self.labelformat % pvalue)
          else:
            self.canvas.itemconfig(self.label, text='')
        else:
          self.canvas.itemconfig(self.label, text=self.labelformat % self.labeltext)
        self.canvas.update_idletasks()


if __name__ == '__main__':
  p = 0
  def IncrememtProgress():
    global p
    p = p + 1
    if p > 100:
      bar.destroy()
      sys.exit()
    bar.update_progress(p)
    root.after(50,IncrememtProgress)
  root=Tk()
  root.title("Progress bar!")
  bar = LoadingBar(root, value=33)
  bar.pack(fill=X)
  root.after(40,IncrememtProgress)
  root.mainloop()
  
