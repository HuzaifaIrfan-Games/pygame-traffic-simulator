
# resolution of curve roads
n = 1
# distance from center and each other
a = 2
# radius of curve and addition to length
b = 12
# length of roads
l = 100


nodes = [

    # starting Nodes always tail and have one nexts

    {
        'node_name': 'south_start_tail_1',
        'position': (-a,
                +b+l),
        'ending_node': False,
        'starting_node': True,
        'vehicle_rate':15,
        'next': ['south_j1_head_1']
    },
    {
        'node_name': 'east_start_tail_1',
        'position': (+b+l,
                +a),
        'ending_node': False,
        'starting_node': True,
        'vehicle_rate':6,
        'next': ['east_j1_head_1']
    },
    {
        'node_name': 'west_start_tail_1',
        'position': (-b-l,
                -a),
        'ending_node': False,
        'starting_node': True,
        'vehicle_rate':10,
        'next': ['west_j1_head_1']
    },
    {
        'node_name': 'north_start_tail_1',
        'position': (+a,
                -b-l),
        'ending_node': False,
        'starting_node': True,
        'vehicle_rate':8,
        'next': ['north_j1_head_1']
    },



    # Ending Nodes always head and have no nexts
    {
        'node_name': 'south_start_head_1',
        'position': (+a,
                +b+l),
        'ending_node': True,
        'starting_node': False,
        'next': []
    },
    {
        'node_name': 'east_start_head_1',
        'position': (+b+l,
                -a),
        'ending_node': True,
        'starting_node': False,
        'next': []
    },
    {
        'node_name': 'west_start_head_1',
        'position': (-b-l,
                +a),
        'ending_node': True,
        'starting_node': False,
        'next': []
    },
    {
        'node_name': 'north_start_head_1',
        'position': (-a,
                -b-l),
        'ending_node': True,
        'starting_node': False,
        'next': []
    },

    # Junction Nodes

    # starting head multiple nexts

    {
        'node_name': 'south_j1_head_1',
        'position': (-a,
                +b),
        'ending_node': False,
        'starting_node': False,
        'next': ['east_j1_tail_1','west_j1_tail_1','north_j1_tail_1']
    },
    {
        'node_name': 'east_j1_head_1',
        'position': (+b,
                +a),
        'ending_node': False,
        'starting_node': False,
        'next': ['south_j1_tail_1','west_j1_tail_1','north_j1_tail_1']
    },

    {
        'node_name': 'west_j1_head_1',
        'position': (-b,
                -a),
        'ending_node': False,
        'starting_node': False,
        'next': ['south_j1_tail_1','east_j1_tail_1','north_j1_tail_1']
    },
    {
        'node_name': 'north_j1_head_1',
        'position': (+a,
                -b),
        'ending_node': False,
        'starting_node': False,
        'next': ['south_j1_tail_1','east_j1_tail_1','west_j1_tail_1']
    },



    # ending tail only one nexts

    {
        'node_name': 'south_j1_tail_1',
        'position': (+a,
                +b),
        'ending_node': False,
        'starting_node': False,
        'next': ['south_start_head_1']
    },
    {
        'node_name': 'east_j1_tail_1',
        'position': (+b,
                -a),
        'ending_node': False,
        'starting_node': False,
        'next': ['east_start_head_1']
    },

    {
        'node_name': 'west_j1_tail_1',
        'position': (-b,
                +a),
        'ending_node': False,
        'starting_node': False,
        'next': ['west_start_head_1']
    },
    {
        'node_name': 'north_j1_tail_1',
        'position': (-a, -b),
        'ending_node': False,
        'starting_node': False,
        'next': ['north_start_head_1']
    },


]


traffic_signals=[
    {'nodes_names':[['south_j1_head_1'],['west_j1_head_1'],['north_j1_head_1'],['east_j1_head_1']],'manual':False}
]

zoom=4
steps_per_update=10



if __name__ == '__main__':

    from trafficSimulator import Map_Configurator

    configurator = Map_Configurator(nodes,traffic_signals)

    configurator.run(zoom,steps_per_update)