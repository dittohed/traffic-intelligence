# Part III: specyfing goals and the scope of the project

### Mesoscopic simulator

...

### Solution draft

* a real-time system for managing traffic lights using sensors data (induction
loops or preferably cameras); 
* an algorithm that disregards a specific junction topology - it picks
a phase for which $score$ is maximized, e.g.: 

$score = v_{mean} + \alpha t_{mean}$

Where each phase must be active for at least $n$ seconds every $N$ seconds. Phases
don't have to be activated in a specified order.

* $score$ expression can be extended with metrics' polynomials or other 
metrics;
* the goal of PSO would be find optimal coefficients used in $score$;
* each particle could run a whole simulation or correspond
to a single junction within a single simulation (up to a dozen of parameters
to find);
* alternatively, each junction might have a separate set of coefficients (up
to a few thousand parameters to find).

**WARNING!** Such approach is feasible only if MATSim can handle calcuting
metrics such as $t_{mean}$. If MATSim isn't capable of determining such metrics,
the solution surely will be suboptimal. Then the alternative is to have a fixed
lights schedule (decision variables being times for each phase for each junction 
- up to a few thousand parameters to find).

### Scale

The first step could be optimizing a traffic lights schedule for a chosen
area of Cracow with up to a dozen of junctions. If it works, then full-scale
simulation can be run.

### Solutions comparison

After finding the best parameters within each simulation, the system should
be run using SUMO simulator as it's more complex and reflects real conditions
better. Metrics: mean queue length, mean waiting time (speed being 0), mean speed, mean throughput.