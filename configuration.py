
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
        'index': 0,
        'pos': (-a,
                +b+l),
        'ending_node': False,
        'starting_node': True,
        'vehicle_rate':15,
        'next': [8]
    },
    {
        'index': 1,
        'pos': (+b+l,
                +a),
        'ending_node': False,
        'starting_node': True,
        'vehicle_rate':6,
        'next': [9]
    },
    {
        'index': 2,
        'pos': (-b-l,
                -a),
        'ending_node': False,
        'starting_node': True,
        'vehicle_rate':10,
        'next': [10]
    },
    {
        'index': 3,
        'pos': (+a,
                -b-l),
        'ending_node': False,
        'starting_node': True,
        'vehicle_rate':8,
        'next': [11]
    },



    # Ending Nodes always head and have no nexts
    {
        'index': 4,
        'pos': (+a,
                +b+l),
        'ending_node': True,
        'starting_node': False,
        'next': []
    },
    {
        'index': 5,
        'pos': (+b+l,
                -a),
        'ending_node': True,
        'starting_node': False,
        'next': []
    },
    {
        'index': 6,
        'pos': (-b-l,
                +a),
        'ending_node': True,
        'starting_node': False,
        'next': []
    },
    {
        'index': 7,
        'pos': (-a,
                -b-l),
        'ending_node': True,
        'starting_node': False,
        'next': []
    },

    # Junction Nodes

    # starting head multiple nexts

    {
        'index': 8,
        'pos': (-a,
                +b),
        'ending_node': False,
        'starting_node': False,
        'next': [13, 14, 15]
    },
    {
        'index': 9,
        'pos': (+b,
                +a),
        'ending_node': False,
        'starting_node': False,
        'next': [12, 14, 15]
    },

    {
        'index': 10,
        'pos': (-b,
                -a),
        'ending_node': False,
        'starting_node': False,
        'next': [12, 13, 15]
    },
    {
        'index': 11,
        'pos': (+a,
                -b),
        'ending_node': False,
        'starting_node': False,
        'next': [12, 13, 14]
    },



    # ending tail only one nexts

    {
        'index': 12,
        'pos': (+a,
                +b),
        'ending_node': False,
        'starting_node': False,
        'next': [4]
    },
    {
        'index': 13,
        'pos': (+b,
                -a),
        'ending_node': False,
        'starting_node': False,
        'next': [5]
    },

    {
        'index': 14,
        'pos': (-b,
                +a),
        'ending_node': False,
        'starting_node': False,
        'next': [6]
    },
    {
        'index': 15,
        'pos': (-a, -b),
        'ending_node': False,
        'starting_node': False,
        'next': [7]
    },




]




traffic_signals=[
    {'nodes_indexs':[[8],[9],[10],[11]]}
]