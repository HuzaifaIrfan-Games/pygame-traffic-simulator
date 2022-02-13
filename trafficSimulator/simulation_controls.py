



import imp
import tkinter as tk
from tkinter import *
from tkinter import ttk

from .traffic_signal_control import TrafficSignalControl
from .vehicle_generator_control import VehicleGeneratorControl


class SimulationControl(tk.Tk):

    def __init__(self,vehicle_generators,traffic_signals):
        super().__init__()

        self.title("Simulation Control")
        self.geometry('400x400')
        # embed = tk.Frame(self.root, width = 500, height = 500) #creates embed frame for pygame window
        # embed.grid(columnspan = (600), rowspan = 500) # Adds grid
        # embed.pack(side = LEFT) #packs window to the left

        frame=self


        def open_vehicle_generator_control():
            window = VehicleGeneratorControl(self,vehicle_generators)
            # window.grab_set()

        def open_traffic_signal_control():
            window = TrafficSignalControl(self,traffic_signals)
            # window.grab_set()

        def close_simulatiom_control():
            self.destroy()
        
        ttk.Button(self,
        text='Open a Vehicle Generator Control',
        command=open_vehicle_generator_control).pack(expand=True)

        ttk.Button(self,
        text='Open a Traffic Signal Control',
        command=open_traffic_signal_control).pack(expand=True)

        ttk.Button(self,
        text='Exit',
        command=close_simulatiom_control).pack(expand=True)


        # self.update()
