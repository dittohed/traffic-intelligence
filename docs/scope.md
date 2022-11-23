# Part III: specyfing goals and scope of the project

### MESO

MESO is a a mesoscopic simulation model which uses the same input data as the main SUMO model.

Sadly, it doesn't support `traci` and therefore doesn't allow for controlling
traffic lights and reading demand statistics such as queue length.

### Solution draft

* A real-time system for managing traffic lights using sensors data (induction
loops or preferably cameras).
* An algorithm that disregards a specific junction topology - it picks
a phase for which $score$ is maximized, e.g.: $score = v_{mean} + \alpha t_{mean}$, 
where each phase must be active for at least $n$ seconds within every $N$ second-long cycle. Phases don't have to be activated in a specified order. The expression can be extended with metrics' polynomials or other 
metrics.
* The goal of PSO would be find optimal coefficients used in $score$.
* Each particle could run a whole simulation or correspond
to a single junction within a single simulation (up to a dozen of parameters
to find).
* Alternatively, each junction might have a separate set of coefficients (up
to a few thousand parameters to find).

**WARNING!** Such approach is feasible only if MATSim can handle calcuting
metrics such as $t_{mean}$. If MATSim isn't capable of determining such metrics,
the solution to be compared across the simulators surely will be suboptimal. The alternative is to have a fixed
lights schedule (decision variables being times for each phase for each junction - up to a few thousand parameters to find).

### Scale

The first step could be optimizing a traffic lights schedule for a chosen
area of Cracow with up to a dozen of junctions. If it works, then full-scale
simulation can be run.

### Optimizers

* plain PSO;
* local PSO (with neighbours being junctions with similar throughput and 
topology);
* APSO (if we can afford to run it).

### Solutions comparison

After finding the best parameters within each simulation, the system should
be run using SUMO simulator as it's more complex and reflects real conditions
better. Metrics: mean queue length, mean waiting time (speed being 0), mean speed, mean throughput.