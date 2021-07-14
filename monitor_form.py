""" STANDAR LIBRARY IMPORTS """
import tkinter as tk
from tkinter import  Toplevel

class MonitorComunication():
    def __init__(self, rootMain):        
        self.root = Toplevel()
        self.root.title('TEST SERIAL MONITOR')      
        window_width =  self.root.winfo_reqwidth()
        window_height =  self.root.winfo_reqheight()
        position_right = int(self.root.winfo_screenwidth()/2 - window_width/2)
        position_down = int(self.root.winfo_screenheight()/2 - window_height/2)
        self.root.geometry("+{}+{}".format(position_right-270, position_down+100))# Positions the window in the center of the page.
        self.txt_monitor = tk.Text(self.root, wrap='none', undo=1 ,width=100, height=10)
        self.txt_monitor.pack(side= tk.BOTTOM, fill= 'both', expand='TRUE')
        self.root.protocol("WM_DELETE_WINDOW", self.hideForm)       

    def show(self):
        self.showForm()

    def showForm(self):
        self.root.deiconify()

    def hideForm(self):
        self.root.withdraw()
if __name__ == "__main__":
    root = tk.Tk()

