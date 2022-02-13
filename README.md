# Pygame Traffic Simulator

### Create nodes in conf file in the following pattern as in examples files
Use you own descriptive node names and positions of nodes and connect them with next list of each node.

If the node is a starting node vehicles will start from there.
if node is ending node vehicles will end there.

All paths from starting nodes and ending nodes are generated automatically.

And vehicle generation settings for each starting nodes can be controlled from simulation control


```json

nodes = [
    {
        'node_name': 'south_start_tail_1',
        'position': (x1, y1),
        'ending_node': False,
        'starting_node': True,
        'vehicle_rate':15,
        'next': ['south_j1_head_1']
    },
]

```




### Create traffic signals in conf file in the following pattern as in examples files using node_name as traffic light position


```json

traffic_signals=[
    {'nodes_names':[['south_j1_head_1'],['west_j1_head_1'],['north_j1_head_1'],['east_j1_head_1']],'manual':False}
]

```

Traffic Signal Settings can be controlled from simulation control.


#### Forked from https://github.com/BilHim/trafficSimulator