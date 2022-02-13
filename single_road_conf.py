
# resolution of curve roads
n = 1
# distance from center and each other
a = 2
# radius of curve and addition to length
b = 12
# length of roads
l = 100


nodes = [

    {
        'node_name': 'west_start_tail_1',
        'position': (-b-l,
                0),
        'ending_node': False,
        'starting_node': True,
        'vehicle_rate':10,
        'next': ['center_j1_node']
    },

        {
        'node_name': 'center_j1_node',
        'position': (0,
                0),
        'ending_node': False,
        'starting_node': False,
        'next': ['east_start_head_1']
    },
   
  


    # Ending Nodes always head and have no nexts

    {
        'node_name': 'east_start_head_1',
        'position': (+b+l,
                0),
        'ending_node': True,
        'starting_node': False,
        'next': []
    },
   


]


traffic_signals=[
   
]

zoom=4
steps_per_update=10



if __name__ == '__main__':

    from Map_Configurator import Map_Configurator

    configurator = Map_Configurator(nodes,traffic_signals)

    configurator.run(zoom,steps_per_update)
