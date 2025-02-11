import numpy as np
from models import Molecule, Atom, Bond
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # Registers the 3D projection
from matplotlib.animation import FuncAnimation

def integrate(molecule, dt):
    """
    A basic integration step using the Euler method.
    This example only updates positions based on current velocities.
    A proper simulation would calculate forces, update velocities, etc.
    
    Parameters:
        molecule (Molecule): The molecule to be simulated.
        dt (float): Timestep for integration.
    """
    # For a more realistic simulation, compute forces and update velocities accordingly.
    for atom in molecule.atoms:
        atom.position += atom.velocity * dt

def run_simulation(molecule, num_steps=100, dt=0.001):
    """
    Run a basic simulation loop.
    
    Parameters:
        molecule (Molecule): The molecule to simulate.
        num_steps (int): Number of simulation steps.
        dt (float): Timestep for integration.
    """
    for step in range(num_steps):
        # Here, you would calculate forces on each atom and update velocities.
        # For now, we'll just update positions.
        integrate(molecule, dt)
        if step % 10 == 0:
            print(f"Step {step}, Total Energy: {molecule.total_energy():.4f}")

def compute_forces(molecule):
    """Compute and assign forces on each atom due to bonds."""
    # Reset forces on all atoms
    for atom in molecule.atoms:
        atom.force = np.zeros(3)
    
    # For each bond, compute the force and distribute it to the two atoms
    for bond in molecule.bonds:
        pos1 = bond.atom1.position
        pos2 = bond.atom2.position
        r_vec = pos1 - pos2
        r = np.linalg.norm(r_vec)
        if r == 0:
            continue  # Avoid division by zero
        # Force magnitude (steepest descent update: move opposite to gradient)
        force_magnitude = -bond.k_b * (r - bond.r0)
        # Force vector along the bond direction
        force_vec = force_magnitude * (r_vec / r)
        bond.atom1.force += force_vec
        bond.atom2.force -= force_vec

def minimization_step(molecule, gamma):
    """
    Perform one energy minimization step using a steepest descent update.
    
    Parameters:
        molecule: The Molecule instance.
        gamma: The step size (learning rate).
    """
    compute_forces(molecule)
    for atom in molecule.atoms:
        # Update positions: note that force is already -gradient
        atom.position += gamma * (atom.force / atom.mass)

def animate_minimization(molecule, num_steps=500, gamma=0.001):
    """
    Animate the energy minimization of the molecule.
    
    Parameters:
        molecule: The Molecule instance.
        num_steps: Total number of minimization steps.
        gamma: Step size for each minimization step.
    """
    # Create a new figure with a 3D axis
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection='3d')
    
    # Set fixed axis limits (adjust as needed)
    ax.set_xlim(-2, 2)
    ax.set_ylim(-2, 2)
    ax.set_zlim(-2, 2)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title("Energy Minimization Animation")
    
    def update(frame):
        # Perform one minimization step
        minimization_step(molecule, gamma)
        
        # Clear the axis and redraw the molecule
        ax.cla()  # Clear the axis
        ax.set_xlim(-2, 2)
        ax.set_ylim(-2, 2)
        ax.set_zlim(-2, 2)
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        ax.set_title(f"Step {frame}")
        
        # Plot atoms
        xs = [atom.position[0] for atom in molecule.atoms]
        ys = [atom.position[1] for atom in molecule.atoms]
        zs = [atom.position[2] for atom in molecule.atoms]
        ax.scatter(xs, ys, zs, s=100, c='blue', marker='o')
        
        # Plot bonds as lines
        for bond in molecule.bonds:
            pos1 = bond.atom1.position
            pos2 = bond.atom2.position
            ax.plot([pos1[0], pos2[0]],
                    [pos1[1], pos2[1]],
                    [pos1[2], pos2[2]], 'r-', linewidth=2)
    
    # Create the animation
    anim = FuncAnimation(fig, update, frames=num_steps, interval=50, repeat=False)
    plt.show()

if __name__ == "__main__":
    # Simple test setup
    # Create two atoms connected by a bond
    atom1 = Atom("H", [0, 0, 0], mass=1.0, charge=0.0)
    atom2 = Atom("H", [0.7, 0, 0], mass=1.0, charge=0.0)
    
    molecule = Molecule()
    molecule.add_atom(atom1)
    molecule.add_atom(atom2)
    
    # Create a bond between the two atoms with an equilibrium distance of 0.74 and a force constant of 450
    bond = Bond(atom1, atom2, r0=0.74, k_b=450.0)
    molecule.add_bond(bond)
    
    # Run the simulation
    run_simulation(molecule)