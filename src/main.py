from models import Atom, Bond, Molecule
from visualization import plot_molecule

def main():
    print("Starting the Molecular Physics Engine Visualization Test")
    
    # Create a simple molecule: two hydrogen atoms with a bond between them
    atom1 = Atom("H", [0, 0, 0], mass=1.0, charge=0.0)
    atom2 = Atom("H", [0.74, 0, 0], mass=1.0, charge=0.0)
    
    molecule = Molecule()
    molecule.add_atom(atom1)
    molecule.add_atom(atom2)
    
    # Define a bond (using an equilibrium bond length of 0.74 angstroms and a force constant)
    bond = Bond(atom1, atom2, r0=0.74, k_b=450.0)
    molecule.add_bond(bond)
    
    # Visualize the molecule
    plot_molecule(molecule)

if __name__ == '__main__':
    main()