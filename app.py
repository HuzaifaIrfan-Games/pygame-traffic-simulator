

from Map_Configurator import Map_Configurator

from configuration_multi import nodes, traffic_signals, zoom, steps_per_update

configurator = Map_Configurator(nodes,traffic_signals)

configurator.run(zoom,steps_per_update)
