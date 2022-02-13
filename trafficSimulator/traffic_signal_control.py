



import tkinter as tk
from tkinter import *
from turtle import position

from functools import partial


class TrafficSignalControl(tk.Toplevel):

    def __init__(self,parent,traffic_signals):
        super().__init__(parent)

        self.traffic_signals=traffic_signals

        self.input_vars=[]

        # for atraffic_signals in traffic_signals:
        #     print(atraffic_signals.cycle_length)


        self.title("Traffic Signal Control")
        self.geometry('400x400')
        # embed = tk.Frame(self.root, width = 500, height = 500) #creates embed frame for pygame window
        # embed.grid(columnspan = (600), rowspan = 500) # Adds grid
        # embed.pack(side = LEFT) #packs window to the left

        frame=self



        # def set_vehicle_rate():
            # inp = inputtxt.get(1.0, "end-1c")
            # lbl.config(text = "Provided Input: "+inp)
        
        # TextBox Creation

        for i, atraffic_signals in enumerate(self.traffic_signals):
            # print(atraffic_signals)

            v = tk.StringVar()
            v.set(f'{atraffic_signals.cycle_length}')

            lbl = tk.Label(frame, text = f"{i}")
            lbl.pack()

            input_box = tk.Entry(frame, textvariable=v,
                            width = 20)
            
            input_box.pack()

            self.input_vars.append(v)


        def set_cycle_length():
            for input_var, atraffic_signals in zip(self.input_vars,self.traffic_signals):
                cycle_length=int(input_var.get())
                atraffic_signals.update_cycle_length(cycle_length)
                
        
        # Button Creation
        set_cycle_lengthButton = tk.Button(frame,
                                text = "Set Cycle Length", 
                                command = set_cycle_length)
        set_cycle_lengthButton.pack()

        def set_all_off(i=0):
            self.traffic_signals[i].set_cycle_index(0)

        def set_all_on(i=0):
            self.traffic_signals[i].set_cycle_index(1)

        def set_to_auto(i=0):
            self.traffic_signals[i].set_to_auto()
    

        for i, atraffic_signals in enumerate(self.traffic_signals):

            lbl = tk.Label(frame, text = f"{i}")
            lbl.pack()   

            f1 = tk.Frame(frame)          

            set_all_offButton = tk.Button(f1,
                                text = "Set All Off", 
                                command = partial(set_all_off, i))
            set_all_offButton.pack(side = LEFT)

            set_all_onButton = tk.Button(f1,
                                text = "Set All On", 
                                command = partial(set_all_on, i))
            set_all_onButton.pack(side = LEFT)


            set_to_autoButton = tk.Button(f1,
                                text = "Set To Auto", 
                                command = partial(set_to_auto, i))
            print(i)
            set_to_autoButton.pack(side = LEFT)

            f1.pack()


        # self.root.update()

    # def update(self):

    #     self.root.update()
