import numpy as np

def harmonic_bond_energy(r, r0, k_b):
    """
    Calculate the harmonic bond energy.
    
    Parameters:
        r (float): Current bond length.
        r0 (float): Equilibrium bond length.
        k_b (float): Bond force constant.
        
    Returns:
        float: Energy of the bond.
    """
    return 0.5 * k_b * (r - r0) ** 2

def harmonic_bond_force(r, r0, k_b):
    """
    Calculate the derivative (force) for the harmonic bond potential.
    
    Parameters:
        r (float): Current bond length.
        r0 (float): Equilibrium bond length.
        k_b (float): Bond force constant.
        
    Returns:
        float: The force magnitude acting to restore the bond length.
    """
    return -k_b * (r - r0)