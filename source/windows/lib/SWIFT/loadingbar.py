
from tkinter import *


class LoadingBar(object):
    def __init__(self, master=None, minvalue=0, maxvalue=100, height=20,
                 width=180, value=0.1):
        
        ## define variables
        self.minvalue = minvalue
        self.maxvalue = maxvalue
        self.width = width
        self.height = height
        self.value = value
        self.dolabel = 1
        
        ## create loadingbar
        self.frame = Frame(master, relief=SOLID, bd=0.5, width=self.width)
        self.frame.pack()
        self.canvas = Canvas(self.frame, bd=0, highlightthickness=0, bg='white',
                             width=self.width, height=self.height)
        self.canvas.pack(fill=BOTH)
        self.scale = self.canvas.create_rectangle(0, 0, self.width, self.height, fill='green')
        self.label = self.canvas.create_text(self.width/2, self.height/2, text='',
                                             anchor=CENTER)
        
        self.update()
        self.canvas.bind('<Configure>', self.on_resize) # monitor size changes


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


    def reset(self):
        # Adjust the rectangle
        self.canvas.coords(self.scale, 0, 0, 0, self.height)

        # And update the label
        self.canvas.itemconfig(self.label, text='')


    def update(self):
        # Trim the values to be between min and max
        value = self.value
        if value > self.maxvalue:
          value = self.maxvalue
        if value < self.minvalue:
          value = self.minvalue
          
        # Adjust the rectangle
        self.canvas.coords(self.scale, 0, 0, float(value) / self.maxvalue * self.width, self.height)


        self.canvas.itemconfig(self.label, text='Loading...')

if __name__ == '__main__':
  p = 0
  def IncrememtProgress():
    global p
    p = p + 1
    if p > 100:
      bar.reset()
      sys.exit()
    bar.update_progress(p)
    root.after(10,IncrememtProgress)
  root=Tk()
  root.title("Progress bar!")
  bar = LoadingBar(root, value=33)
  root.after(40,IncrememtProgress)
  root.mainloop()
  
