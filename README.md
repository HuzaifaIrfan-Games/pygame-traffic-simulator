# Pygame Traffic Simulator

<!-- •[Link](#)

<hr>

![overview](overview.drawio.png)

-->

## 🎬 Demo

[▶️![Demo](https://img.youtube.com/vi/y-DzLQIqBr4/maxresdefault.jpg)](https://www.youtube.com/watch?v=y-DzLQIqBr4)



## Nov 28, 2021 Fork from https://github.com/BilHim/trafficSimulator

# 🚀 Usage

### Map Configuration Class

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


# 📝 Documentation

# 📚 References



# 🤝🏻 Connect with Me

[![GitHub](https://img.shields.io/badge/Github-%23222.svg?style=for-the-badge&logo=github&logoColor=white)](https://github.com/HuzaifaIrfan/)
[![Website](https://img.shields.io/badge/Website-%23222.svg?style=for-the-badge&logo=google-chrome&logoColor==%234285F4)](https://www.huzaifairfan.com)

# 📜 License

Licensed under the GPL3 License, Copyright 2025 Huzaifa Irfan. [LICENSE](LICENSE)

Last Updated on 2022-02-13
