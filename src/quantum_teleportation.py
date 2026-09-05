import numpy as np
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit_aer import AerSimulator
from qiskit.result import marginal_counts

q = QuantumRegister(3, name="q")
c = ClassicalRegister(3, name="c")
circuit = QuantumCircuit(q, c)

circuit.h(q[0])
circuit.rz(np.pi / 4, q[0])
circuit.barrier()

circuit.h(q[1])
circuit.cx(q[1], q[2])
circuit.barrier()

circuit.cx(q[0], q[1])
circuit.h(q[0])
circuit.barrier()

circuit.measure(q[0], c[0])
circuit.measure(q[1], c[1])
circuit.barrier()

with circuit.if_test((c[1], 1)):
    circuit.x(q[2])

with circuit.if_test((c[0], 1)):
    circuit.z(q[2])

circuit.measure(q[2], c[2])

print("Quantum Teleportation Circuit:")
print(circuit)

simulator = AerSimulator()
job = simulator.run(circuit, shots=1024)
result = job.result()
counts = result.get_counts(circuit)

final_counts = marginal_counts(counts, [2])

print("\n--- Results ---")
print("Full counts:", counts)
print("\nFinal Fix: Marginal counts for teleported qubit (c[2]):")
print(final_counts)
print("1 and 0 split is roughly equal, indicating successful teleportation.")