

from Map_Configurator import Map_Configurator

from configuration import nodes,traffic_signals

configurator = Map_Configurator(nodes,traffic_signals)

configurator.run()