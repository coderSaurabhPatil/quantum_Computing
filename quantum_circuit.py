from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

#create a quntum circuit with 3 qubits and 3 classical bits

qc = QuantumCircuit(3,3)

#applay pauli-x gate 
qc.x(0)



#applay pauli-y gate
qc.y(1)

#apply Pauli-z gate
qc.z(2)

#apply Hadamard get to the first qubit (to create superpostion)
qc.h(0)

#apply Cnot gate (control: qubit 0, target: qubit 1)
qc.cx(0,1)

#Apply Toffoli Gate (control: qubit 0 and 1, target:qubit 2)
qc.ccx(0,1,2)

#measure the qubits and store the result in classical bits
# Measure the qubits and store the results in classical bits
qc.measure([0, 1, 2], [0, 1, 2])

# Draw the circuit
print("Quantum Circuit:")
print(qc.draw())

# Execute the circuit on a simulator
# Initialize the global Aer simulator
simulator = AerSimulator()
result = simulator.run(qc, shots=1024).result()  # Using run directly on the simulator

# Get the results
counts = result.get_counts(qc)

# Print the results
print("\nMeasurement results:")
print(counts)

# Plot the results
plot_histogram(counts).show()

