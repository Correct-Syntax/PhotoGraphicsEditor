##XXX Not used in the program, yet...

import threading
import queue
from tkinter import *


class ThreadClient:
    """
    Launch the main part of the GUI and the worker thread. periodicCall and
    endApplication could reside in the GUI part, but putting them here
    means that you have all the thread controls in a single place.
    """
    def __init__(self, master, command, args=()):
        """
        Start the GUI and the asynchronous threads. We are in the main
        (original) thread of the application, which will later be used by
        the GUI. We spawn a new thread for the worker.
        """
        self.master = master
        self._command = command
        self._args = args

        ## Create the queue
        self.queue = queue.Queue()

        # Set up the thread to do asynchronous I/O
        # More can be made if necessary
        self.running = 1
        self.thread1 = threading.Thread(target=self.secondary_thread, args=self._args)
        self.thread1.start()

        # Start the periodic call in the GUI to check if the queue contains
        # anything
        self.periodic_call()


    def periodic_call(self):
        ## Check every 100 ms if there is something new in the queue.
        if not self.running:
            # This is the brutal stop of the system. You may want to do
            # some cleanup before actually shutting it down.
            import sys
            sys.exit(1)
        self.master.after(100, self.periodic_call)


    def secondary_thread(self):
        """
        This is where we handle the asynchronous I/O. For example, it may be
        a 'select()'.
        One important thing to remember is that the thread has to yield
        control.
        """
        while self.running:
            import time
            # To simulate asynchronous I/O, we create a random number at
            # random intervals. Replace the following 2 lines with the real
            # thing.
            time.sleep(1.0)
            self.queue.put(self._command(self._args))


    def configure(self, command):
        ## configure what the thread is doing
        self._command = command(self._args)


    def end_secondary_thread(self):
        self.running = 0
