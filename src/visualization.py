import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # Even if unused directly, this registers the 3D projection
import numpy as np

def plot_molecule(molecule):
    """
    Plots the atoms and bonds of a molecule in 3D.
    
    Parameters:
        molecule: An object that has:
            - molecule.atoms: a list of Atom objects (with .position attribute as a NumPy array)
            - molecule.bonds: a list of Bond objects (with .atom1 and .atom2 attributes referencing Atom objects)
    """
    # Create a 3D plot
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection='3d')
    
    # Plot atoms
    xs = []
    ys = []
    zs = []
    labels = []  # optional, to display element symbols or indices
    for i, atom in enumerate(molecule.atoms):
        xs.append(atom.position[0])
        ys.append(atom.position[1])
        zs.append(atom.position[2])
        labels.append(atom.element)
    
    # Scatter plot for atoms
    scatter = ax.scatter(xs, ys, zs, s=100, c='blue', marker='o', label='Atoms')
    
    # Optionally add text labels near atoms
    for x, y, z, label in zip(xs, ys, zs, labels):
        ax.text(x, y, z, label, fontsize=10, color='black')
    
    # Plot bonds as lines connecting atoms
    for bond in molecule.bonds:
        # Get positions of the two atoms
        pos1 = bond.atom1.position
        pos2 = bond.atom2.position
        # Create lists for the line coordinates
        x_line = [pos1[0], pos2[0]]
        y_line = [pos1[1], pos2[1]]
        z_line = [pos1[2], pos2[2]]
        ax.plot(x_line, y_line, z_line, 'r-', linewidth=2, label='Bond')
    
    # Set labels for axes
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title("Molecule Visualization")
    
    # Show legend (avoid duplicate labels by using unique handles)
    handles, labels = ax.get_legend_handles_labels()
    unique = dict(zip(labels, handles))
    ax.legend(unique.values(), unique.keys())
    
    plt.show()