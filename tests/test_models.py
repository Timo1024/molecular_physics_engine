import numpy as np
from src.models import Atom, Bond

def test_bond_energy():
    # Create two atoms
    atom1 = Atom("H", [0, 0, 0], mass=1.0, charge=0.0)
    atom2 = Atom("H", [1, 0, 0], mass=1.0, charge=0.0)
    
    # Set bond parameters
    r0 = 1.0
    k_b = 100.0
    
    bond = Bond(atom1, atom2, r0, k_b)
    
    # At r == r0, energy should be zero
    energy = bond.energy()
    assert np.isclose(energy, 0.0), f"Expected energy to be 0, got {energy}"

if __name__ == "__main__":
    test_bond_energy()
    print("All tests passed!")