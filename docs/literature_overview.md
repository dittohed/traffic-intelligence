# List of useful terms
- *compatible streams* - two compatible streams of cars can safely cross the intersection simultaneously.
- *stage / phase* - traffic light signals allowing a predefined compatible traffic streams to cross the intersection simultaneously.
- *signal cycle* - one repetition of the basic series of stages.
- *cycle time* - duration of a cycle.
- *integreen time* - time inserted between consecutive stages to avoid interference between antagonistic streams.
- *split* - the ratio of green and red lights within one cycle (for each light).
- *offset* - a delay between the starting times of green periods of two neighboring traffic lights along the same traffic route.

# Papers
### A Review on Swarm Intelligence and Evolutionary Algorithms for Solving the Traffic Signal Control Problem (2020)
* problem formulation and parameters

| **Network**             | **Intersection**        | **Roundabouts**         | **Lights**         |
|-------------------------|-------------------------|-------------------------|--------------------|
| Vehicle Flow            | Vehicle Delays          | Travel Time Delay       | Queue Length       |
| Traffic Throughput Rate | Stop-and-Wait Times     | Cycle Times             | Green Times        |
| Queue Lenght            | Vehicle Stops           | Vehicle Time Delay      | Mean Travel Time   |
| Stop-and-Wait Times     | Traffic Throughput Rate | Traffic Throughput Rate | Cycle Time         |
| Congestion in Links     | Travel Time             | Roundabout Size         | Vehicle Stops      |
| Travel Time             | Queue Lenght            |                         | Vehicle Stop Times |
| Vehicle Delay           | Vehicle Capacity        |                         |                    |

* algorithms inspired by nature has been applied for solving the TSC problem for 2 decades;
* evaluation (fitness function calculation) is done using a simulation;
* genetic algorithms are most prevalent among evolutionary algorithms;
* for evolutionary algorithms: green times vector for each phase are the most popular decision variables, the most picked objective to minimize is the time delay (either as a single objective or within multiple objectives), some modifications of standard GA are used (NSGA which modifies the selection operator), differential evolution and genetic programming methods are used as well.
* swarm algorithms do not require any prior information about the search space characteristics
* particle swarm optimization is most prevalent among swarm intelligence algorithms;
* a significant number of papers present PSO algorithms which exhibit a faster convergence rate and less total delay than GA algorithms;
* the majority of reported PSO approaches optimize the average delay or total travelling time;
* ant colony optimization algorithms are less popular than particle swarm optimization and tend to optimize the total throughput

### Signal Timing Determination Using Genetic Algorithms (1992)
* a foundational paper on applying GA for traffic signal control;
* GA always follow the same rules, only chromosome coding and fitness function are problem-dependent;
* defines a typical workflow (having some traffic statistics: initialize a population -> run the GA loop, use simulation for evaluating the members);
* GA can serve as a dynamic system given that it's run repeatedly.

### Intelligent Intersection Control for Delay Optimization: Using Meta-Heuristic Search Algorithms (2020)
* compares GA (better optimum) with DE (faster);
* uses data gathered for 2 intersections in Saudi Arabia;
* uses average delay as the objective, green splits as decision variables, some constraints for green splits and cycle time;
* simulation is run based on the flow rate (vehicles per hour).
