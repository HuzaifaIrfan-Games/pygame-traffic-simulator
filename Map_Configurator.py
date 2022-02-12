import enum
import numpy as np
from trafficSimulator import *
from itertools import groupby
 



class Map_Configurator:
    def __init__(self,nodes_conf, traffic_signals_conf):

        self.sim = Simulation()

        self.nodes=nodes_conf
        self.traffic_signals_conf= traffic_signals_conf

        self.roads = []
        self.paths = []
        self.vehicle_generators=[]
        self.traffic_signals=[]


        self.road_generator()
        self.road_creator()

        self.road_next_generator()
        


        self.paths_gen()
        self.create_signal()
        
        # self.create_all_starting_node_vehicle_generators()
        self.create_independent_node_vehicle_generators()

        self.sim.create_simulation_control(self.vehicle_generators,self.traffic_signals)
               
        # self.sim.create_vehicle_generator_control(self.vehicle_generators) 

        # self.sim.create_traffic_signal_control(self.traffic_signals)


        # print(self.vehicle_generators)



    def get_node_from_node_name(self, node_name):

        for i, anode in enumerate(self.nodes):
            if anode['node_name'] == node_name:
                return anode




    def create_all_starting_node_vehicle_generators(self):

        # print(paths)
        vehicle_paths=[]

        for apath in self.paths:
            vehicle_paths.append([3, {'path': apath}])

        avehicle_generator=self.sim.create_gen({
            'vehicle_rate': 15,
            'vehicles':vehicle_paths}
            )

        self.vehicle_generators.append(avehicle_generator)

        


        


        


    def create_independent_node_vehicle_generators(self):
        # sort list
        # essential for grouping
        # self.paths.sort()
        
        
        # using lambda + itertools.groupby() + partition()
        # group similar substrings
        grouped_paths = [list(i) for j, i in groupby(self.paths,
                    lambda a: a[0])]

        # print(grouped_paths)
        


        for grouped_path in grouped_paths:
            # print(paths)
            vehicle_paths=[]

            for apath in grouped_path:
                vehicle_paths.append([1, {'path': apath}])

            # print(vehicle_paths)

            sim_road_index=grouped_path[0][0]
            # print(sim_road_index)

            vehicle_rate=self.get_vehicle_rate_from_starting_node(sim_road_index)
            

            avehicle_generator = self.sim.create_gen({
                'vehicle_rate': vehicle_rate,
                'vehicles':vehicle_paths}
                )

            self.vehicle_generators.append(avehicle_generator)


    def get_vehicle_rate_from_starting_node(self,sim_road_index):
        for aroad in self.roads:
            if aroad['sim_road_index'] == sim_road_index:
                tail_node=aroad['tail_node']
                # print(tail_node)

                if tail_node['vehicle_rate']:
                    return tail_node['vehicle_rate']

                return 1





    def road_generator(self):

        for i, anode in enumerate(self.nodes):

            if not anode['ending_node']:

                for j, next_node_name in enumerate(anode['next']):
                    next_node = self.get_node_from_node_name(next_node_name)

                    # tail
                    pos1 = anode['position']

                    # head
                    pos2 = next_node['position']

                    aroad = {
                        'sim_road_index': None,
                        'tail': pos1,
                        'tail_index': anode['node_name'],
                        'tail_node': anode,
                        'starting_node': anode['starting_node'],
                        'head': pos2,
                        'head_index': next_node['node_name'],
                        'head_node': next_node,
                        'ending_node': next_node['ending_node'],
                        'next':[]
                    }
                    # print(anode['starting_node'])

                    self.roads.append(aroad)



    def road_creator(self):

        for aroad in self.roads:
            head = aroad['head']
            tail = aroad['tail']
            road_position = (tail, head)

            aroad['sim_road_index'] = self.sim.create_road(*road_position)



        # print(len(roads))


    def road_next_generator(self):

        for i, aroad in enumerate(self.roads):
            # print('-----------------------------' ,i)
            
            for j, broad in enumerate(self.roads):
                # print('---------' ,j)
                aroad_head_index=aroad['head_node']
                broad_tail_index=broad['tail_node']

                # print(aroad_head_index)
                # print(broad_tail_index)

                if aroad_head_index == broad_tail_index:
                    aroad['next'].append(j)
            
            # print(aroad['next'])


        # print(roads)

        



        

        # [
        #     {
        #         'sim_road_index': None,
        #         'road_index': None,
        #     },
        # ]

                        # aroad = {
                        #     'sim_road_index': None,
                        #     'head': pos1,
                        #     'head_index': i,
                        #     'head_node': anode,
                        #     'ending_node': anode['ending_node'],
                        #     'tail': pos2,
                        #     'tail_index': j,
                        #     'tail_node': next_node,
                        #     'starting_node': next_node['starting_node']
                                                    # 'next':[]
                        # }


            

    def paths_gen(self):

        for i, aroad in enumerate(self.roads):
            # print(aroad['starting_node'])

            

            if aroad['starting_node']:
                # print('aroad starting')


                prev_path=[aroad['sim_road_index']]


                def recursion_path_gen(prev_road, prev_path):
                    for j, broad_index in enumerate(prev_road['next']):
                        # print(broad_index)
                        broad=self.roads[broad_index]
                        apath = prev_path.copy()
                        # print(apath)

                        apath.append(broad['sim_road_index'])

                        if broad['ending_node']:
                            self.paths.append(apath)
                            break
                        else:
                            recursion_path_gen(broad, apath)
                
                recursion_path_gen(aroad, prev_path)
                            




    def get_road_from_node(self,anode):

        for aroad in self.roads:
            # print(aroad['head_node'])
            # print(anode)
            if aroad['head_node'] == anode:
                return aroad
                



    def create_signal(self):
        for atraffic_signal_conf in self.traffic_signals_conf:
            nodes_names = atraffic_signal_conf['nodes_names']
            roads_indexs=[]
            for independent_light_node_name in nodes_names:
                independent_light_road_index=[]
                for light_node_name in independent_light_node_name:

                    anode = self.get_node_from_node_name(light_node_name)
                    aroad=self.get_road_from_node(anode)
                    independent_light_road_index.append(aroad['sim_road_index'])

                roads_indexs.append(independent_light_road_index)

            # print(roads_indexs)
            atraffic_signal=self.sim.create_signal(roads_indexs)

            if atraffic_signal_conf.get('cycle_length'):

                atraffic_signal.update_properties({'cycle_length':atraffic_signal_conf['cycle_length']})
            
            if atraffic_signal_conf.get('manual'):
                atraffic_signal.set_to_manual()

            # atraffic_signal.current_cycle_index = 1

            # print(atraffic_signal.current_cycle)

            self.traffic_signals.append(atraffic_signal)







    def run(self,zoom,steps_per_update):
        # Start simulation
        win = Window(self.sim)
        win.zoom = zoom
        win.run(steps_per_update=steps_per_update)

