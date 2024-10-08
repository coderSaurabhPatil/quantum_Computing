from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

# Initialize the global Aer simulator
simulator = AerSimulator()

def create_superposition_circuit():
    """Create a quantum circuit that demonstrates superposition."""
    qc = QuantumCircuit(1, 1)  # 1 qubit, 1 classical bit for measurement
    qc.h(0)  # Apply Hadamard gate to create superposition
    qc.measure(0, 0)  # Measure the qubit into the classical bit
    return qc

def run_simulation(circuit):
    """Run the given quantum circuit using the global simulator."""
    transpiled_qc = transpile(circuit, simulator)
    result = simulator.run(transpiled_qc).result()
    return result

def main():
    """Main function to run the quantum circuit."""
    qc = create_superposition_circuit()  # Create the circuit
    print(qc.draw())  # Print the circuit diagram

    # Run the simulation
    result = run_simulation(qc)

    # Get the counts and print
    counts = result.get_counts(qc)  # Get counts for the specific circuit
    print("Counts:", counts)

    # Plot the histogram of results
    plot_histogram(counts)
    plt.show()  # Show the plot

if __name__ == "__main__":
    main()  # Call the main function
