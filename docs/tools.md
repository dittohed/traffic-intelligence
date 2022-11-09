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

SUMO (Simulation of Urban MObility) is an open source, microscopic traffic simulation package 
developed by the German Aerospace Center and community users.

It's been developed since 2001, has a detailed documentation and gathered 
a wide community.

**Tools**

SUMO package consists of multiple tools, some of them being:

* `netedit` - a graphical tool for building and editing networks + specyfing
traffic (demand);
* `sumo-gui` - a graphical tool for running and visualizing simulation live;
* `sumo` - a non-graphical counterpart of sumo-gui;
* `netconvert` - a command-line tool for converting OSM to SUMO networks; 
* `traci` - a Python library for running, investigating and controlling
simulations;
* random traffic generator - a command-line tool for generating random traffic
given input network.

**Files defining a simulation**

3 files has to be provided in order to run a simulation using Python:

* `*.net.xml` file - defines the network topology (lanes, roads, junctions) along with
auxiliary attributes (e.g. speed limits, traffic light phases);
* `*.rou.xml` file - defines the traffic (a sequence of vehicle where each one
has it's corresponding spawn time and a route);
* `*.sumocfg` file - simply zips `*.net.xml` and `*.rou.xml` files.

**Performance**

According to the documentation, SUMO simulation runs on a single core and there's
no support for multi-node parallelization yet. However, it's possible to control
multiple simulations from a single script using traci.

RAM usage for Cracow simulation with a reasonable traffic is relatively low 
(~1.2GB for almost 60,000 vehicles) and can be seamlessly run using cheap Intel CPU.

It seeems that what constitutes a bottleneck is the random traffic generation 
(followed by routes verification). A simple solution for running multiple, random
simulations in an efficient manner would be to generate one bigger `*.rou.xml` file
in advance, then sample from it.

**Demo**

See the [corresponding directory](../demos/sumo/).

### SMARTS
https://projects.eng.unimelb.edu.au/smarts/

SMARTS (Scalable Microscopic Adaptive Road Traffic Simulator) is a flexible microscopic traffic simulator developed at the School of Computing and Information Systems, University of Melbourne.

It's main advantage is a capability to run distributed simulations. However,
it doesn't seem to have as wide community and as detailed documentation as SUMO.

### Decision
As we're already slightly familiar with SUMO (which has a broader community and
more detailed documentation), we decided to pick SUMO as the microscopic simulator.

# Mesoscopic simulators
Mesoscopic modeling is at an intermediate level of detail between macroscopic and microscopic simulation models.
Compared with macroscopic models, mesoscopic models can simulate more details of individual vehicles’ movements
and produce more accurate simulation results. Compared with microscopic models, mesoscopic models can provide
significant savings in modeling time and efforts, especially when analyzing large area networks, without unduly
compromising the accuracy of results.
Mesoscopic simulation has many advantages such as requiring less effort for network building and calibration than microscopic
simulation and generating more detailed simulation results in terms of traffic conditions than macroscopic simulation.

| **Simulator** | **Speed** | **OSM support** | **Community & docs** |
|---------------|:---------:|:---------------:|:--------------------:|
| MATSim        |     ✓     |        ✓        |           ✓          |
| Mezzo         |     ✓     |        ✕        |           ✕          |
| Metropolis    |     ✕     |        ✓        |           ✕          |
| Meso (SUMO)   |     ✕     |        ✓        |           ✓          |

### MATSim
https://www.matsim.org/

MATSim (Multi-Agent Transport Simulation) is an open-source framework for implementing large-scale agent-based transport simulations.
MATSim, was developed jointly at TU Berlin, ETH Zurich, and the Senozon Company. It is an agent-based model.
It is capable of simulating vehicles and public transport in large detail, and can also simulate pedestrians or cyclists.
MATSim is able to simulate large scenarios with several million agents. Moreover, the simulation processing time is very fast.
It is a mesoscopic simulation tool.

**Input Files**
Minimally, MATSim needs the files:
* config.xml, containing the configuration options for MATSim
* network.xml, with the description of the (road) network
* population.xml, providing information about travel demand, i.e., list of agents and their daily plans, can be generated from scripts.

**Performance**
TBD

### Meso (SUMO)
https://sumo.dlr.de/docs/Simulation/Meso.html

Starting with version 0.26.0 the mesoscopic model is available in the sumo distribution (MESO has been developed alongside SUMO since 2002 but was not publicly available). MESO refers to a mesoscopic simulation model which uses the same input data as the main sumo model. It computes vehicle movements with queues and runs up to 100 times faster than the microscopic model of sumo.

### Mezzo
https://www.kth.se/ctr/research/model-development/mezzo-mesoscopic-traffic-simulator-1.726113

Mezzo is a discrete-event traffic simulation model that simulates road traffic on the level of individual vehicles, but with an aggregated behaviour on links. The model is especially designed to simulate large networks


### Decision
We decided to pick MAtSim as our mesoscopic simulator. It is very fast and well suited for large network simulations.
It supports OSM, which was an important criterium. It also has a detailed documentation and a large community.
Meso (SUMO) was also considered, thanks to its community, but a deeper research showed that it is probably
slower than MATSim.
