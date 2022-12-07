# Part IV: prototype v1

### Same scenario across SUMO and MATSim

* Importing from MATSim to SUMO is not an option due to a simplified representation
of the network used by MATSim.
* Importing from SUMO to MATSim seems promising - network can be imported
seamlessly using a ready-to-use tool, demand and traffic lights have to be parsed manually.
* Worst case scenario: importing the network directly to each simulator from OSM
(simplified geometry in MATSim), utilizing random traffic generators with the same parameters.

### Configuration conversion

See the [corresponding directory](../demos/matsim/single_intersection).

Done:
* Converting the network to MATSim results in routes conversion but lanes information is missing
* Population was parsed using a Python script. Vehicles do not start from the desired position.
* Traffic lights were parsed using a Python script. Due to missing lanes information the simulation can not be run.

To do:
* Lanes conversion is in progess.
* Run a simulation with config converted from SUMO with working traffic lights.

### Gathering metrics and controller prototype

**SUMO**

See the [corresponding directory](../demos/sumo/src).

Done:
* `.net.xml` file is parsed to determine junction to be controlled, possible
phases and corresponding lane-to-lane connections.
* For each simulation step, for each junction, all the phases are evaluated,
then controller picks a phase with a maximum score.

To do:
* Implement more states (metrics) utilized to make a decision.
* Calculate score using parametrized polynomials.
* Extend the controller (constraints, interim yellow signals).

