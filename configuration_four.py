
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
        'node_name': 0,
        'position': (-a,
                +b+l),
        'ending_node': False,
        'starting_node': True,
        'vehicle_rate':15,
        'next': [8]
    },
    {
        'node_name': 1,
        'position': (+b+l,
                +a),
        'ending_node': False,
        'starting_node': True,
        'vehicle_rate':6,
        'next': [9]
    },
    {
        'node_name': 2,
        'position': (-b-l,
                -a),
        'ending_node': False,
        'starting_node': True,
        'vehicle_rate':10,
        'next': [10]
    },
    {
        'node_name': 3,
        'position': (+a,
                -b-l),
        'ending_node': False,
        'starting_node': True,
        'vehicle_rate':8,
        'next': [11]
    },



    # Ending Nodes always head and have no nexts
    {
        'node_name': 4,
        'position': (+a,
                +b+l),
        'ending_node': True,
        'starting_node': False,
        'next': []
    },
    {
        'node_name': 5,
        'position': (+b+l,
                -a),
        'ending_node': True,
        'starting_node': False,
        'next': []
    },
    {
        'node_name': 6,
        'position': (-b-l,
                +a),
        'ending_node': True,
        'starting_node': False,
        'next': []
    },
    {
        'node_name': 7,
        'position': (-a,
                -b-l),
        'ending_node': True,
        'starting_node': False,
        'next': []
    },

    # Junction Nodes

    # starting head multiple nexts

    {
        'node_name': 8,
        'position': (-a,
                +b),
        'ending_node': False,
        'starting_node': False,
        'next': [13, 14, 15]
    },
    {
        'node_name': 9,
        'position': (+b,
                +a),
        'ending_node': False,
        'starting_node': False,
        'next': [12, 14, 15]
    },

    {
        'node_name': 10,
        'position': (-b,
                -a),
        'ending_node': False,
        'starting_node': False,
        'next': [12, 13, 15]
    },
    {
        'node_name': 11,
        'position': (+a,
                -b),
        'ending_node': False,
        'starting_node': False,
        'next': [12, 13, 14]
    },



    # ending tail only one nexts

    {
        'node_name': 12,
        'position': (+a,
                +b),
        'ending_node': False,
        'starting_node': False,
        'next': [4]
    },
    {
        'node_name': 13,
        'position': (+b,
                -a),
        'ending_node': False,
        'starting_node': False,
        'next': [5]
    },

    {
        'node_name': 14,
        'position': (-b,
                +a),
        'ending_node': False,
        'starting_node': False,
        'next': [6]
    },
    {
        'node_name': 15,
        'position': (-a, -b),
        'ending_node': False,
        'starting_node': False,
        'next': [7]
    },


]


traffic_signals=[
    {'nodes_indexs':[[8],[10],[11],[9]]}
]