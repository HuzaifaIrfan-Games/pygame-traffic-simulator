

from configuration_four import nodes, traffic_signals, zoom, steps_per_update


if __name__ == '__main__':

    from Map_Configurator import Map_Configurator

    configurator = Map_Configurator(nodes,traffic_signals)

    configurator.run(zoom,steps_per_update)
