class TrafficSignal:
    def __init__(self, roads, config={}):
        # Initialize roads
        self.roads = roads
        self.cycle_length=30
        # Set default configuration
        self.set_default_config()

        self.set_individual_signal_cycle()

        
        self.update_properties(config)

        # Calculate properties
        self.init_properties()



    def update_properties(self,config):

        # print(config)
        # Update configurations
        for attr, val in config.items():
            setattr(self, attr, val)

    def set_individual_signal_cycle(self):


        individual_signals=len(self.roads)

        self.cycle=[]

        for n in range(individual_signals):

            signal_state = tuple(True if i == n else False for i in range(individual_signals))
            # print(signal_state)

            self.cycle.append(signal_state)


            

    def set_default_config(self):

        # self.cycle = [(True, False,False,False), (False, True,False,False),(False, False,True,False),(False, False,False,True)]

        self.slow_distance = 50
        self.slow_factor = 0.4
        self.stop_distance = 15

        self.current_cycle_index = 0

        self.last_t = 0

    def init_properties(self):
        for i in range(len(self.roads)):
            for road in self.roads[i]:
                road.set_traffic_signal(self, i)

    @property
    def current_cycle(self):

        return self.cycle[self.current_cycle_index]
    
    def update(self, sim):
        # self.cycle_length = 30
        k = (sim.t // self.cycle_length) % len(self.roads)
        self.current_cycle_index = int(k)
