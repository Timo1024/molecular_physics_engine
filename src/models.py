import numpy as np

class Atom:
    def __init__(self, element, position, mass, charge):
        self.element = element
        self.position = np.array(position, dtype=float)
        self.velocity = np.zeros_like(self.position)  # Initialize velocity to zero
        self.mass = mass
        self.charge = charge

    def __repr__(self):
        return f"Atom({self.element}, pos={self.position}, mass={self.mass}, charge={self.charge})"

class Bond:
    def __init__(self, atom1, atom2, r0, k_b):
        self.atom1 = atom1  # This could be the index or a reference to an Atom object
        self.atom2 = atom2
        self.r0 = r0  # Equilibrium bond length
        self.k_b = k_b  # Force constant

    def current_distance(self):
        return np.linalg.norm(self.atom1.position - self.atom2.position)

    def energy(self):
        # Harmonic bond potential: V = 1/2 * k_b * (r - r0)^2
        r = self.current_distance()
        return 0.5 * self.k_b * (r - self.r0) ** 2

class Molecule:
    def __init__(self):
        self.atoms = []
        self.bonds = []
        # You can also add lists for angles, dihedrals, etc.

    def add_atom(self, atom):
        self.atoms.append(atom)

    def add_bond(self, bond):
        self.bonds.append(bond)

    def total_energy(self):
        energy = 0.0
        for bond in self.bonds:
            energy += bond.energy()
        # Later add contributions from angles, dihedrals, nonbonded interactions, etc.
        return energy