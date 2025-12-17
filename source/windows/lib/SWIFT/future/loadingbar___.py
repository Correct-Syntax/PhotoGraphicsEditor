
from tkinter import *

import threading
import sys
import tkinter.simpledialog as tkSimpleDialog
import tkinter.messagebox as tkMessageBox
import tkinter as Tkinter
import queue as Queue


class LoadingBar(object):
    def __init__(self, master=None, text='Loading...', minvalue=0, maxvalue=100, height=40,
                 width=100, value=0.1, labelformat="%d%%", labeltext=''):
        #Toplevel.__init__(self, master)

##        self.title(text)
##        self.geometry('300x30')
        
        ## define variables
        self.master = master
        self.minvalue = minvalue
        self.maxvalue = maxvalue
        self.width = width
        self.height = height
        self.value = value
        self.labelformat = labelformat
        self.labeltext = labeltext
        self.dolabel = 1
        
        ## create loadingbar
        self.frame = Frame(self.master, relief=SOLID, bd=0.5, width=self.width)
        self.frame.pack(fill=X)
        self.canvas = Canvas(self.frame, bd=0, highlightthickness=0, bg='white',
                             width=self.width, height=self.height)
        self.canvas.pack(fill=BOTH)
        self.scale = self.canvas.create_rectangle(0, 0, self.width, self.height, fill='green')
        self.label = self.canvas.create_text(self.width/2, self.height/2, text=self.labeltext,
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

        
class ThreadsConnector:

  def __init__(self):
    """ Initialize object """
    self.messages = Queue.Queue()
    self.running = 1
    self.silent_ack = 0

  def put_message(self, msg):
    """ Just a wrapper to Queue.put_nowait() """
    self.messages.put_nowait(msg)

  def get_message(self):
    """ Just a wrapper to Queue.get_nowait() """
    return self.messages.get_nowait()

  def cancel(self):
    """ Terminate calculations thread """
    self.running = 0

  def isRunning(self):
    """ Return true value if calculations are running now """
    return self.running

  def ack(self):
    """ Monitor activeness of calculations thread """
    if not(self.running):
      # Raise exception only once and
      # only if current thread is the cakcukations thread.
      # Check for thread is required because logger calls ack(),
      # and gui thread can call caller before calculations thread.
      if not(self.silent_ack):
        if self.calc_thread == threading.currentThread():
          self.silent_ack = 1
          print('ThreadsConnectorTerminateException!')

  def start(self, group, target, name, args, kw):
    """ Create and start calculations thread """
    self.calc_thread = threading.Thread(group, self.wrap_calc, name, (target, args, kw))
    self.calc_thread.start()

  def wrap_calc(self, target, args, kw):
    """ Function start() continues, but now in calculations thread """
    try:
      kw['connector'] = self
      kw['progress'] = self.progress
      target(*args, **kw)
      #self.put_message([MESSAGE_EXIT_OK,     TEXT_EXIT_OK])
    except:
      # All other exception
      self.running = 0
      print('# All other exception')

  def runInGui(self, wnd, conn, group=None, target=None, name=None, args=(), kwargs={}):
    """ Run calculations, using window as a progress indicator
        "wnd" is an object of class ''ActionWindow
        all other parameters are passed to threading.Thread
    """
    wnd.setConnector(self)
    self.progress = ProgressBar(self)
    wnd.setProgressBar(self.progress)
    self.start(group, target, name, args, kwargs)
    wnd.go()






    
class ProgressBar:

  def __init__(self, conn):
    """ Create progress bar controller, remember connector """
    self.conn  = conn
    self.cur   = 0
    self.limit = 100

  def set(self, cur, limit):
    """ Initialize current position and maximal value """
    self.cur   = cur
    self.limit = limit
    self.notify()

  def get(self):
    """ Get current and maximal positions """
    return (self.cur, self.limit)

  def tick(self):
    """ Increment current position """
    self.cur = self.cur + 1
    self.notify()

  def notify(self):
    """ Notify GUI widget on change. Check if thread should be finished. """
    self.conn.put_message([ThreadsConnector.MESSAGE_PROGRESS, None])
    self.conn.ack()

    






class ActionWindow(tkSimpleDialog.Dialog):

    def __init__(self, parent, title, text):
        """ Create dialog, remember interface objects """
    # Postpone parent's init bacause it starts modal dialog immediately
    #tkSimpleDialog.Dialog.__init__(self, parent, title)
        self.aw_parent = parent
        self.aw_title  = title
        self.aw_text   = text

    def setConnector(self, conn):
        """ Remember a thread connector """
        self.conn = conn

    def setProgressBar(self, progress):
        """ Remember a progress bar controller """
        self.progress_ctrl = progress

    def go(self):
        """ Create and start dialog """
        tkSimpleDialog.Dialog.__init__(self, self.aw_parent, self.aw_title)

    def wait_window(self, wnd):
        """ Customize appearence of window, setup periodic call and call parent's wait_window """
        self.fixWindowLayout()
        tkSimpleDialog.Dialog.wait_window(self, wnd)

    def destroy(self):
        """ Terminate periodic process and call parent's destroy """
        tkSimpleDialog.Dialog.destroy(self)


    def onCalculationsExitMessage(self, text):
        """ Visualize that calculations are finished """
        self.status_label.configure(text=text)
        self.progress_bar.update_progress(100,100)
        self.button_cancel.configure(state=Tkinter.DISABLED)
        self.button_ok.configure(state=Tkinter.NORMAL)
        self.bind('<Escape>', self.cancel)

    def onProgress(self):
        """ Visualize progress of calculations """
        (cur, limit) = self.progress_ctrl.get()
        self.progress_bar.update_progress(cur, limit)

    def body(self, master):
        """ Pack body of window """
        Tkinter.Label(master, text=self.aw_text, anchor=Tkinter.NW, justify=Tkinter.LEFT).pack(fill=Tkinter.X)
        self.progress_bar = LoadingBar(master)
        self.status_label = Tkinter.Label(master, text='Task is in progress', anchor=Tkinter.NW, justify=Tkinter.LEFT)
        self.status_label.pack(fill=Tkinter.X)


    def buttonbox(self):
        """ Pack buttons """
        tkSimpleDialog.Dialog.buttonbox(self)
        # Get buttons by accessing children of last packed frame
        (self.button_ok, self.button_cancel) = self.pack_slaves()[-1].pack_slaves()
        self.button_ok.configure(state=Tkinter.DISABLED)
        self.bind('<Escape>', lambda e: 'break')

    def fixWindowLayout(self):
        """ Make window content resizable, set minimal sizes of window to avoid disappearing of GUI elements """
        # [0] is a wrapping frame for the window body
        self.pack_slaves()[0].pack_configure(fill=Tkinter.BOTH, expand=1)
        self.update_idletasks()
        reqheight = self.winfo_reqheight()
        reqwidth  = self.button_ok.winfo_reqwidth() + self.button_cancel.winfo_reqwidth()
        self.minsize(reqwidth + 10, reqheight + 10)

    def ok(self, event=None):
        """ Handle 'ok' button. Can be called only after end of calculations """
        if not(self.conn.isRunning()):
          tkSimpleDialog.Dialog.ok(self)

    def cancel(self, event=None):
        """ Handle 'cancel' button and window close """
        if not(self.conn.isRunning()):
          tkSimpleDialog.Dialog.cancel(self)
          return                                               # return
        if tkMessageBox.askyesno(title='Cancelling operation', message='Cancel operation?', parent=self):
          self.conn.cancel()





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
  root.after(40,IncrememtProgress)
  root.mainloop()
  
