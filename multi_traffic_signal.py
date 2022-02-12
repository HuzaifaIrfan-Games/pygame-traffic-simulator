import numpy as np
from trafficSimulator import *

sim = Simulation()

# Play with these

# resolution of curve roads
n = 1
# distance from center and each other
a = 2
# radius of curve and addition to length
b = 12
# length of roads
l = 100

# Nodes
WEST_TAIL_START = (-b-l, a+10)
WEST_HEAD_START =	(-b-l, -a+10)

SOUTH_TAIL_START = (a-30, b+l)
SOUTH_HEAD_START = (-a-30, b+l)

NORTH_TAIL_START = (-a-30, -b-l)
NORTH_HEAD_START = (a-30, -b-l)

J1_CENTER = (0,0)


WEST_HEAD_J1 = (-b, a)
WEST_TAIL_J1 =	(-b, -a)

SOUTH_HEAD_J1 = (a, b)
SOUTH_TAIL_J1 = (-a, b)

EAST_HEAD_J1 = (b, -a)
EAST_TAIL_J1 = (b, a)

NORTH_HEAD_J1 = (-a, -b)
NORTH_TAIL_J1 = (a, -b)

EAST_TAIL_J2  = (b+l+20, -a)
EAST_HEAD_J2 = (b+l+20, a)

J2_CENTER = (b+l+20+8*a, 0)


NORTH_EAST_TAIL_J2  = (a + J2_CENTER[0], -b)
NORTH_EAST_HEAD_J2 = (-a + J2_CENTER[0], -b)

SOUTH_EAST_TAIL_J2  = (-a + J2_CENTER[0], b)
SOUTH_EAST_HEAD_J2 = (a + J2_CENTER[0], b)


NORTH_EAST_TAIL_START  = (-a + J2_CENTER[0], -b-l)
NORTH_EAST_HEAD_START = (a + J2_CENTER[0], -b-l)

SOUTH_EAST_TAIL_START  = (a + J2_CENTER[0], b+l)
SOUTH_EAST_HEAD_START = (-a + J2_CENTER[0], b+l)



# Roads
WEST_START_J1 = (WEST_TAIL_START, WEST_HEAD_J1)
SOUTH_START_J1 = (SOUTH_TAIL_START, SOUTH_HEAD_J1)
EAST_J2_J1 = (EAST_TAIL_J2, EAST_HEAD_J1)
NORTH_START_J1 = (NORTH_TAIL_START, NORTH_HEAD_J1)

WEST_J1_START = (WEST_TAIL_J1, WEST_HEAD_START)
SOUTH_J1_START = (SOUTH_TAIL_J1, SOUTH_HEAD_START)
EAST_J1_J2 = (EAST_TAIL_J1, EAST_HEAD_J2)
NORTH_J1_START = (NORTH_TAIL_J1, NORTH_HEAD_START)


NORTH_EAST_J2_START = (NORTH_EAST_TAIL_J2, NORTH_EAST_HEAD_START)
NORTH_EAST_START_J2 = (NORTH_EAST_TAIL_START, NORTH_EAST_HEAD_J2)

SOUTH_EAST_J2_START = (SOUTH_EAST_TAIL_J2, SOUTH_EAST_HEAD_START)
SOUTH_EAST_START_J2 = (SOUTH_EAST_TAIL_START, SOUTH_EAST_HEAD_J2)



# junction 1

WEST_STRAIGHT_J1 = (WEST_HEAD_J1, EAST_TAIL_J1)
SOUTH_STRAIGHT_J1 = (SOUTH_HEAD_J1, NORTH_TAIL_J1)
EAST_STRAIGHT_J1 = (EAST_HEAD_J1, WEST_TAIL_J1)
NORTH_STRAIGHT_J1 = (NORTH_HEAD_J1, SOUTH_TAIL_J1)

WEST_SOUTH_TURN_J1 = turn_road(WEST_HEAD_J1, SOUTH_TAIL_J1, TURN_RIGHT, n)
WEST_NORTH_TURN_J1 = turn_road(WEST_HEAD_J1, NORTH_TAIL_J1, TURN_LEFT, n)

SOUTH_EAST_TURN_J1 = turn_road(SOUTH_HEAD_J1, EAST_TAIL_J1, TURN_RIGHT, n)
SOUTH_WEST_TURN_J1 = turn_road(SOUTH_HEAD_J1, WEST_TAIL_J1, TURN_LEFT, n)

EAST_NORTH_TURN_J1 = turn_road(EAST_HEAD_J1, NORTH_TAIL_J1, TURN_RIGHT, n)
EAST_SOUTH_TURN_J1 = turn_road(EAST_HEAD_J1, SOUTH_TAIL_J1, TURN_LEFT, n)

NORTH_WEST_TURN_J1 = turn_road(NORTH_HEAD_J1, WEST_TAIL_J1, TURN_RIGHT, n)
NORTH_EAST_TURN_J1 = turn_road(NORTH_HEAD_J1, EAST_TAIL_J1, TURN_LEFT, n)


# junction 2

SOUTH_EAST_STRAIGHT_J2 = (SOUTH_EAST_HEAD_J2, NORTH_EAST_TAIL_J2)
NORTH_EAST_STRAIGHT_J2 = (NORTH_EAST_HEAD_J2, SOUTH_EAST_TAIL_J2)

EAST_SOUTH_EAST_TURN_J2 = turn_road(EAST_HEAD_J2, SOUTH_EAST_TAIL_J2, TURN_RIGHT, n)
EAST_NORTH_EAST_TURN_J2 = turn_road(EAST_HEAD_J2, NORTH_EAST_TAIL_J2, TURN_LEFT, n)

SOUTH_EAST_EAST_TURN_J2 = turn_road(SOUTH_EAST_HEAD_J2, EAST_TAIL_J2, TURN_LEFT, n)
NORTH_EAST_EAST_TURN_J2 = turn_road(NORTH_EAST_HEAD_J2, EAST_TAIL_J2, TURN_RIGHT, n)




sim.create_roads([

#START J1 0-2
    WEST_START_J1,
    SOUTH_START_J1,
    NORTH_START_J1,

#START J2 3-4
    NORTH_EAST_START_J2,
    SOUTH_EAST_START_J2,

#END J1 5-7
    WEST_J1_START,
    SOUTH_J1_START,
    NORTH_J1_START,

#END J2 8-9
    NORTH_EAST_J2_START,
    SOUTH_EAST_J2_START,
    
#CENTER J1 J2 10-11
    EAST_J1_J2,
    EAST_J2_J1,




    WEST_STRAIGHT_J1,
    SOUTH_STRAIGHT_J1,
    EAST_STRAIGHT_J1,
    NORTH_STRAIGHT_J1, 

    NORTH_EAST_STRAIGHT_J2,
    SOUTH_EAST_STRAIGHT_J2,



# 18 18+n
    *WEST_NORTH_TURN_J1,
    *WEST_SOUTH_TURN_J1,


# 18+2n 18+3n
    *NORTH_WEST_TURN_J1,
    *NORTH_EAST_TURN_J1,


# 18+4n 18+5n
    *EAST_NORTH_TURN_J1,
    *EAST_SOUTH_TURN_J1,

# 18+6n 18+7n
    *SOUTH_WEST_TURN_J1,
    *SOUTH_EAST_TURN_J1,

# 18+8n 18+9n 
    *EAST_NORTH_EAST_TURN_J2,
    *EAST_SOUTH_EAST_TURN_J2,


# 18+10n 18+11n
    *NORTH_EAST_EAST_TURN_J2,
    *SOUTH_EAST_EAST_TURN_J2,



])

def road(a): return range(a, a+n)

sim.create_gen({
'vehicle_rate': 10,
'vehicles':[
    # 0-2 IN J1 PATH
    # W S N
    # 3-4 IN J2 PATH
    # NE SE
    # 5-7 OUT J1 PATH
    # W S N
    # 8-9 OUT J2 PATH
    # NE SE
    # 10-11 CENTER J1 J2
    # J1 J2
    # J2 J1

    # STRAIGHT 
    # W - E 12
    # S - N 13
    # E - W 14
    # N - S 15
    # SE - NE 16
    # NE -SE 17

     [3, {'path': [0, 12, 10, *road(18+8*n), 8]}],
    [3, {'path': [0, 12, 10, *road(18+9*n), 9]}],
    

   [3, {'path': [1, *road(18+7*n), 10, *road(18+8*n), 8]}],
    [3, {'path': [2, *road(18+3*n), 10, *road(18+9*n), 9]}],
    

    [3, {'path': [1, 13, 7]}],
     [3, {'path': [2, 15, 6]}],
     [3, {'path': [3, 16, 9]}],
     [3, {'path': [4, 17, 8]}],




]})


# sim.create_gen({
# 'vehicle_rate': 10,
# 'vehicles':[


# ]})

# sim.create_gen({
# 'vehicle_rate': 10,
# 'vehicles':[
#     [3, {'path': [2, 10, 4]}],
#     [1, {'path': [2, *road(12+4*n), 7]}],
#     [1, {'path': [2, *road(12+5*n), 5]}]

 
# ]})

# sim.create_gen({
# 'vehicle_rate': 10,
# 'vehicles':[
#     [3, {'path': [3, 11, 5]}],
#     [1, {'path': [3, *road(12+6*n), 4]}],
#     [1, {'path': [3, *road(12+7*n), 6]}]
# ]})



sim.create_signal([[0],[1],[11],[2]])

sim.create_signal([[3],[4],[10]])




# Start simulation
win = Window(sim)
win.zoom = 10
win.run(steps_per_update=10)