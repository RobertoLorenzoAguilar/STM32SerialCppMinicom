from tkinter import *
from tkinter import ttk
from monitor_form   import MonitorComunication
import tkinter as tk
import tkinter.messagebox
import tkinter.font as tkFont
import tkinter.messagebox
""" THIRD LIBRARY IMPORTS """
from threading import Thread
import serial
import serial.tools.list_ports
import time
import re

class SerialGUI(ttk.Frame):

    def __init__(self, isapp=True, name='dataloader'):
        self.sock = None
        self.sender = None
        self.receiver = None
        self.txt_receive = tk.Text
        self.val_row = None
        ttk.Frame.__init__(self, name=name)
        self.pack(expand=Y, fill=BOTH)
        self.master.title('TEST SERIAL')        
        self.master.geometry("500x200")
        self.isapp = isapp
        self.tool_main_bar()
        self.serial_section()
        self.open_form_monitor()      
        self.btn_font = tkFont.Font(family="Helvetica", size=12, weight='bold')

    '''FRAME SECTIONS'''
    def tool_main_bar(self):
        demoPanel = Frame(self)
        demoPanel.config(bg="white")
        demoPanel.pack(side=TOP, fill=BOTH)
        shortcut_bar = Frame(demoPanel,  height=50,  bg="white")
        shortcut_bar.pack(side='left')
        # label signal
        label_signal_icon = PhotoImage(file='images/{}.png'.format("serial"))    
        label_signal = Label(shortcut_bar, image=label_signal_icon, bg="white")
        label_signal.image = label_signal_icon
        label_signal.pack(side='left')
        lbl_tool= Label(shortcut_bar, text="Connected to:",  bg="white")
        lbl_tool.config(fg="gray")
        lbl_tool.config(font=("Arial",12))
        lbl_tool.pack(side='left')
        lbl_tool= Label(shortcut_bar, text="SERIAL",  bg="white")
        lbl_tool.config(font=("Arial",12))
        lbl_tool.pack(side='left')
        #events
        label_signal.bind("<Button-1>", self.open_form_monitor)           
    
    def serial_section(self):
        serial_panel = Frame(self)
        serial_panel.config()
        serial_panel.pack(side=TOP, fill=BOTH)
        shortcut_bar = Frame(serial_panel,  height=50)
        shortcut_bar.pack(side='left')
        '''SERIAL CONECTION PATH'''
        self.com_choose_frame=Frame(shortcut_bar)
        self.com_choose_frame.pack(side="top")
        self.com_label=Label(self.com_choose_frame,text='COMx: ')
        self.com_label.grid(row=0,column=0,sticky=E)
        self.baudrate_label=Label(self.com_choose_frame,text='Baudrate: ')
        self.baudrate_label.grid(row=1,column=0,sticky=E,pady=10)
        self.com_choose=StringVar()
        self.com_choose_combo=ttk.Combobox(self.com_choose_frame,width=30,textvariable=self.com_choose)
        self.com_choose_combo['state']='readonly'
        self.com_choose_combo.grid(row=0,column=1,padx=15)
        self.com_choose_combo['values']=self.com_name_get()
        self.baudrate_value=StringVar(value='9600')
        self.baudrate_choose_combo=ttk.Combobox(self.com_choose_frame,width=30,textvariable=self.baudrate_value)
        self.baudrate_choose_combo['values']=('9600','115200')
        self.baudrate_choose_combo['state']='readonly'
        self.baudrate_choose_combo.grid(row=1,column=1,padx=15)
        self.connect_button=Button(self.com_choose_frame,text='Connect',bg='lightblue',width=10, command=self.com_connect)
        self.connect_button.grid(row=0,column=2,padx=15)
        self.cancel_button=Button(self.com_choose_frame,text='Cancel',bg='lightblue',width=10, command=self.com_cancel)
        self.cancel_button.grid(row=1,column=2,padx=15)

        """CALCULATE SECTION"""
        self.numb_label=Label(self.com_choose_frame,text='Number 0 - 9: ')
        self.numb_label.grid(row=2,column=0,sticky=E)            
        self.txt_number= tk.Entry(self.com_choose_frame,width=33)        
        self.txt_number.grid(row=2,column=1, pady=10)
        self.numb_result_label=Label(self.com_choose_frame,text='Result square: ')
        self.numb_result_label.grid(row=3,column=0,sticky=E)
        self.txt_number_result= tk.Entry(self.com_choose_frame,width=33)        
        self.txt_number_result.grid(row=3,column=1)
        self.calculate_button=Button(self.com_choose_frame,text='Calculate',width=10, command = self.send_number_to_calculate)
        self.calculate_button.grid(row=3,column=2,padx=15)       
   
    ''' WIDGETS EVENTS '''
    def send_number_to_calculate(self):        
        self.start_receiving()
        str_to_send= self.txt_number.get()
        str_show = "R --> "+ str_to_send
        enter_ascii= chr(13) #received message
        encode_str =str_to_send.encode()
        self.ser.write(encode_str)
        self.ser.write(enter_ascii.encode())
        self.txt_receive.txt_monitor.insert(END, str_show + 'Config\n')             
        
   
    comConfingmonitor = None
    def open_form_monitor(self, event=None):
        if self.comConfingmonitor!=None:
            self.comConfingmonitor.showForm()
        else:
            self.comConfingmonitor= MonitorComunication(self.master)
            self.comConfingmonitor.showForm()
            self.txt_receive = self.comConfingmonitor
            self.txt_receive.txt_monitor.delete(1.0, 'end')
        print(self.comConfingmonitor)   
    def com_cancel(self):
        self.stop_receiving()
        self.txt_receive.txt_monitor.delete('1.0','end')
        try:
            self.ser.close()
            tkinter.messagebox.showinfo("Conection closed",time.ctime(time.time())+" Succesfull")
        except:
            tkinter.messagebox.showerror("Connected", 'Something was wrong')
    
    def com_connect(self):
        self.ser_name=str(self.com_choose.get())
        self.ser_baudrate=str(self.baudrate_value.get())
        try:
            self.ser=serial.Serial(self.ser_name)
            self.ser.baudrate=self.ser_baudrate
            self.ser.timeout=0.5
            tkinter.messagebox.showinfo("Connected",time.ctime(time.time())+" Succesfull")
            self.start_receiving()
            self.txt_receive.txt_monitor.insert(END,time.ctime(time.time())+'\t\t'+'Serial port opened successfully'+'\n')
        except:
            tkinter.messagebox.showerror("Connected", 'Something was wrong')

    def com_name_get(self):
        self.port_list=list(serial.tools.list_ports.comports())
        self.com_port_names=[]
        self.pattern=re.compile(r'[(](.*?)[)]',re.S)
        if len(self.port_list)>0:
            for i in range(len(self.port_list)):
                self.com_name=re.findall(self.pattern,str(self.port_list[i]))
                self.com_port_names.append(self.com_name)
        return self.com_port_names 

    def start_receiving(self):
        self.connect_button.config(state='disabled')
        self.cancel_button.config(state='normal')
        if self.receiver == None:
            self.receiver = Receiver(self.txt_receive.txt_monitor,self.txt_number_result, self.ser) 
        else:
            self.receiver.stop()
            self.receiver = Receiver(self.txt_receive.txt_monitor,self.txt_number_result, self.ser) 

        self.receiver.start()
    
    ''' COMMON EVENTS '''
    #----Stop the receiver
    def stop_receiving(self):
        self.connect_button.config(state='normal')
        self.cancel_button.config(state='disabled')
        self.receiver.stop()
        self.receiver.join()
        self.receiver = None             
    
''' THREATS CLASS '''
class Receiver(Thread):
    def __init__(self, txt_receive, txt_number_result, proto):
        # Call Thread constructor
        super().__init__()
        self.proto = proto
        self.keep_running = True
        self.txt_receive  = txt_receive
        self.row_val = None
        """ NEW FIELD  """
        self.txt_number_result = txt_number_result

    def stop(self):
        # Call this from another thread to stop the receiver
        self.keep_running = False

    def set_row_val(self, row_val):
        self.row_val = row_val


    def run(self):
        # This will run when you call .start method
        time.sleep(0.2)  # TODO: MAYBE NEED ADD A COUPLE OF MINUTES TO SHOW COMPLETE THE MESSAGE
        while self.keep_running:
            if self.proto.inWaiting():
                text = self.proto.readline(self.proto.inWaiting()).decode()
                if text != "\n":
                    str_pr = "S -->" + text  
                    self.txt_receive.insert(END, str_pr + '\n')                      
                    if 'A square  is:'  in text: 
                        self.txt_number_result.delete(0, 'end')
                        value_result = self.get_only_one_digit(text)
                        self.txt_number_result.insert(END, value_result)          
                    
    def get_only_one_digit(self, string):
        value = ""
        for c in string:
            if c.isdigit():
                value = value +  str(c)
        return value

if __name__ == '__main__':
    SerialGUI().mainloop()
