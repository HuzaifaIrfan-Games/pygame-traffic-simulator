



import tkinter as tk
from tkinter import *


class VehicleGeneratorControl:

    def __init__(self,vehicle_generators):

        self.vehicle_generators=vehicle_generators

        self.input_vars=[]

        # for avehicle_generators in vehicle_generators:
        #     print(avehicle_generators.vehicle_rate)

        self.root = tk.Tk()
        self.root.title("Vehicle Generator Control")
        self.root.geometry('400x400')
        # embed = tk.Frame(self.root, width = 500, height = 500) #creates embed frame for pygame window
        # embed.grid(columnspan = (600), rowspan = 500) # Adds grid
        # embed.pack(side = LEFT) #packs window to the left

        frame=self.root



        # def set_vehicle_rate():
            # inp = inputtxt.get(1.0, "end-1c")
            # lbl.config(text = "Provided Input: "+inp)
        
        # TextBox Creation

        for i, avehicle_generator in enumerate(self.vehicle_generators):

            v = tk.StringVar()
            v.set(f'{avehicle_generator.vehicle_rate}')

            lbl = tk.Label(frame, text = f"{i}")
            lbl.pack()

            input_box = tk.Entry(frame, textvariable=v,
                            width = 20)
            
            input_box.pack()

            self.input_vars.append(v)


        def set_vehicle_rate():
            for input_var, avehicle_generator in zip(self.input_vars,self.vehicle_generators):
                vehicle_rate=int(input_var.get())
                avehicle_generator.update_vehicle_rate(vehicle_rate)
                
        
        # Button Creation
        set_vehicle_rateButton = tk.Button(frame,
                                text = "Set Vehicle Rates", 
                                command = set_vehicle_rate)
        set_vehicle_rateButton.pack()
        


        self.root.update()

    def update(self):

        self.root.update()
