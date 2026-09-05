from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator 
from qiskit.visualization import plot_histogram 
import matplotlib.pyplot as plt 

def error_check(circuit):
    if not isinstance(circuit, QuantumCircuit):
        raise TypeError("Expected a QuantumCircuit object.")
    if circuit.num_qubits < 2:
        raise ValueError("Quantum circuit must have at least 2 qubits.")
    return True

def build_bell_state(circuit, state):
    error_check(circuit)

    circuit.initialize([1, 0, 0, 0], [0, 1])

    if state == "phi+":
        circuit.h(0)
        circuit.cx(0, 1)

    elif state == "phi-":
        circuit.h(0)
        circuit.z(0)
        circuit.cx(0, 1)

    elif state == "psi+":
        circuit.h(0)
        circuit.cx(0, 1)
        circuit.x(1)

    elif state == "psi-":
        circuit.h(0)
        circuit.z(0)
        circuit.x(1)
        circuit.cx(0, 1)

    else:
        raise ValueError("Unsupported state. Use 'phi+', 'phi-', 'psi+', or 'psi-'.")
    return circuit

def decode_and_measure_bell_state(circuit):
    error_check(circuit)

    circuit.cx(0, 1)
    circuit.h(0)

    measured_circuit = circuit.measure_all(inplace=False)

    return measured_circuit

def main():
    my_circuit = QuantumCircuit(2)

    # Change argument to each of the bell states in the form "phi+", "phi-", "psi+", or "psi-" to run the corresponding state preparation/measurement
    state = "phi+"
    my_circuit = build_bell_state(my_circuit, state)
    final_circuit = decode_and_measure_bell_state(my_circuit)

    print(f"Prepared Bell State: {state}")

    print("Full Quantum Circuit (Preparation + Decoding + Measurement):")
    print(final_circuit.draw('text'))
    print()

    simulator = AerSimulator()

    job = simulator.run(final_circuit, shots=1024)

    result = job.result()
    counts = result.get_counts(final_circuit)

    print("Measurement Results (Classical Bits):")
    print(counts)

    plot_histogram(counts, title="Measurement Outcomes").show()

    plt.show(block=False)
    plt.pause(5)         
    plt.close()       

if __name__ == "__main__":
    main()