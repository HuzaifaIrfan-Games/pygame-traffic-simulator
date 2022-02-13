
# resolution of curve roads
n = 1
# distance from center and each other
a = 2
# radius of curve and addition to length
b = 12
# length of roads
l = 150

j2_position=+b+l+8*a


nodes = [

    # starting Nodes always tail and have one nexts

    #
    #south tail
    {
        'node_name': 0,
        'position': (-a,
                +b+l),
        'ending_node': False,
        'starting_node': True,
        'vehicle_rate':5,
        'next': [8]
    },

    #east tail  #j2
    {
        'node_name': 1,
        'position': (+b+l,
                +a),
        'ending_node': False,
        'starting_node': False,
        'vehicle_rate':6,
        'next': [9]
    },
        #west tail
    {
        'node_name': 2,
        'position': (-b-l,
                -a),
        'ending_node': False,
        'starting_node': True,
        'vehicle_rate':4,
        'next': [10]
    },

        #north tail
    {
        'node_name': 3,
        'position': (+a,
                -b-l),
        'ending_node': False,
        'starting_node': True,
        'vehicle_rate':5,
        'next': [11]
    },



    # Ending Nodes always head and have no nexts

    #south head
    {
        'node_name': 4,
        'position': (+a,
                +b+l),
        'ending_node': True,
        'starting_node': False,
        'next': []
    },
        #east head  #j2
    {
        'node_name': 5,
        'position': (+b+l,
                -a),
        'ending_node': False,
        'starting_node': False,
        'next': [20,23]
    },
    #west head
    {
        'node_name': 6,
        'position': (-b-l,
                +a),
        'ending_node': True,
        'starting_node': False,
        'next': []
    },
    #north head
    {
        'node_name': 7,
        'position': (-a,
                -b-l),
        'ending_node': True,
        'starting_node': False,
        'next': []
    },

    # Junction Nodes J1

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





    #junction 2



        #east north tail
    {
        'node_name': 17,
        'position': (+a+j2_position,
                -b-l),
        'ending_node': False,
        'starting_node': True,
        'vehicle_rate':4,
        'next': [21]
    },

        #east north head
    {
        'node_name': 16,
        'position': (-a+j2_position,
                -b-l),
        'ending_node': True,
        'starting_node': False,
        'next': []
    },


        #east south tail
    {
        'node_name': 18,
        'position': (-a+j2_position,
                +b+l),
        'ending_node': False,
        'starting_node': True,
        'vehicle_rate':4,
        'next': [22]
    },

        #east south head
    {
        'node_name': 19,
        'position': (+a+j2_position,
                +b+l),
        'ending_node': True,
        'starting_node': False,
        'next': []
    },



     # Junction Nodes J2

    # starting head multiple nexts

    {
        'node_name': 22,
        'position': (-a+j2_position,
                +b),
        'ending_node': False,
        'starting_node': False,
        'next': [20,1]
    },



    {
        'node_name': 21,
        'position': (+a+j2_position,
                -b),
        'ending_node': False,
        'starting_node': False,
        'next': [23,1]
    },



    # ending tail only one nexts

    {
        'node_name': 23,
        'position': (+a+j2_position,
                +b),
        'ending_node': False,
        'starting_node': False,
        'next': [19]
    },

    {
        'node_name': 20,
        'position': (-a+j2_position, -b),
        'ending_node': False,
        'starting_node': False,
        'next': [16]
    },



]


traffic_signals=[
    {'nodes_names':[[8],[10],[11],[9]],'cycle_length':30},
    {'nodes_names':[[5],[22],[21]],'cycle_length':30}
]


zoom=10
steps_per_update=10

if __name__ == '__main__':

    from Map_Configurator import Map_Configurator

    configurator = Map_Configurator(nodes,traffic_signals)

    configurator.run(zoom,steps_per_update)
