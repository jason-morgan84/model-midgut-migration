This project uses a 2D off-lattice centre-based model to model the migration of the _Drosophila_ posterior embryonic midgut, based on the findings in Campbell et al (2015). 

Requirements
------------
Python
Matplotlib

Simulation
----------

For each cell in each simulation tick, the model finds the neighbouring cells, calculates the forces applied to the cell (both cell extrinsic forces from its neighbours and cell intrinsic forces from itself), then calculates acceleration, velocity and the new position of the cell.
The force acting on a cell, _i_, can be calculated from:
•	The sum of all migrationary forces (_M_) between the cell, _i_, and each neighbour, _j_.
•	The sum of all forces due to adhesion (_A_) between the cell and each neighbour, modelled as a close range attractive force.
•	The sum of all repulsive forces due to proximity (_P_) between the cell and each neighbour. This acts as a means of collision avoidance.
•	Cell intrinsic forces (_I_) acting on the cell, i, if any are present. This defines where the cell would ‘want’ to go in the absence of other forces.
•	The drag on a cell (_D_) – this acts to limit the maximum speed at which the cell can move.

<img width="423" height="74" alt="image" src="https://github.com/user-attachments/assets/cc31f5c9-85d4-4cb2-8bce-7cec6533b0cd" />

References
----------
Campbell, K., Casanova, J. A role for E-cadherin in ensuring cohesive migration of a heterogeneous population of non-epithelial cells. Nat Commun 6, 7998 (2015). https://doi.org/10.1038/ncomms8998

