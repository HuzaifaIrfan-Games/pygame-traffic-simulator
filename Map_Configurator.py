import enum
import numpy as np
from trafficSimulator import *
from itertools import groupby
 



class Map_Configurator:
    def __init__(self,nodes, traffic_signals):

        self.sim = Simulation()

        self.nodes=nodes
        self.traffic_signals= traffic_signals

        self.roads = []
        self.paths = []
        self.vehicle_generators=[]


        self.road_generator()
        self.road_creator()

        self.road_next_generator()
        


        self.paths_gen()
        self.create_signal()
        
        # self.create_all_starting_node_vehicle_generators()
        self.create_independent_node_vehicle_generators()





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

                for j, next_node_index in enumerate(anode['next']):
                    next_node = self.nodes[next_node_index]

                    # tail
                    pos1 = anode['pos']

                    # head
                    pos2 = next_node['pos']

                    aroad = {
                        'sim_road_index': None,
                        'tail': pos1,
                        'tail_index': i,
                        'tail_node': anode,
                        'starting_node': anode['starting_node'],
                        'head': pos2,
                        'head_index': j,
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
                            





    


    def create_signal(self):
        for atraffic_signal in self.traffic_signals:
            nodes_indexs = atraffic_signal['nodes_indexs']
            roads_indexs=[]
            for independent_light_node_index in nodes_indexs:
                independent_light_road_index=[]
                for light_node_index in independent_light_node_index:
                    anode = self.nodes[light_node_index]
                    
                    for aroad in self.roads:
                        # print(aroad['head_node'])
                        # print(anode)
                        if aroad['head_node'] == anode:
                            independent_light_road_index.append(aroad['sim_road_index'])
                            break


                roads_indexs.append(independent_light_road_index)

            print(roads_indexs)

            self.sim.create_signal(roads_indexs)







    def run(self):
        # Start simulation
        win = Window(self.sim)
        win.zoom = 10
        win.run(steps_per_update=10)

