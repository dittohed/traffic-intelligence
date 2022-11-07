# Part II: picking the right tools

The aim of this part was to become familiar with and pick the tools for comparing
optimal traffic control solution characterics obtained with PSO algorithm
when using micro- and mesoscopic traffic flow simulators under the hood.

# PSO libraries
TODO: pyswarm, pyswarms, pymoo (need multi-objective optimizer?)

# Microscopic simulators
Simulators of this kind model each vehicle and it's dynamics individually. 
They provide a detailed simulation at cost of speed. 

### SUMO
https://www.eclipse.org/sumo/

TODO: general overview (files, netconvert, traffic generator, Python interface), single-core + low
RAM usage, demo, parallel simulations, shuffle

### SMARTS
https://projects.eng.unimelb.edu.au/smarts/

SMARTS (Scalable Microscopic Adaptive Road Traffic Simulator) is a flexible  microscopic traffic simulator developed at the School of Computing and Information Systems, University of Melbourne.

It's main advantage is a capability to run distributed simulations. However,
it doesn't seem to have as wide community and as detailed documentation as SUMO.

Therefore we decided to pick SUMO as the microscopic simulator.

# Mesoscopic simulators
...
