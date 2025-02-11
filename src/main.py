from models import Atom, Bond, Molecule
from visualization import plot_molecule
from simulation import animate_minimization

def main():
    print("Starting the Energy Minimization and Animation Test")
    
    # Create a molecule with two atoms placed away from equilibrium
    atom1 = Atom("H", [0, 0, 0], mass=1.0, charge=0.0)
    # Place the second atom at an initial distance that is not the equilibrium distance.
    atom2 = Atom("H", [1.5, 0, 0], mass=1.0, charge=0.0)
    
    molecule = Molecule()
    molecule.add_atom(atom1)
    molecule.add_atom(atom2)
    
    # Define a bond with an equilibrium distance of 0.74 and a force constant
    bond = Bond(atom1, atom2, r0=0.74, k_b=450.0)
    molecule.add_bond(bond)
    
    # Run the minimization animation.
    # The atoms should gradually move toward the equilibrium distance.
    animate_minimization(molecule, num_steps=500, gamma=0.0001)

if __name__ == '__main__':
    main()