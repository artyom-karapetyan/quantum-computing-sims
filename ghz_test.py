import numpy as np
from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator

def create_ghz_circuit():
    qc = QuantumCircuit(3, 3)
    qc.h(0)     
    qc.cx(0, 1) 
    qc.cx(0, 2)
    qc.barrier()
    return qc

def get_expectation_value(counts, shots):
    expectation = 0
    for result, count in counts.items():
        parity = result.count('1') % 2
        
        if parity == 0:
            expectation += count
        else:
            expectation -= count
            
    return expectation / shots

if __name__ == '__main__':
    measurements = ['XXX', 'XYY', 'YXY', 'YYX']
    
    simulator = AerSimulator()
    shots = 8192 
    
    print("Running GHZ Nonlocality Test...")
    print("-" * 35)

    experimental_results = {}

    for m_setting in measurements:
        ghz_circuit = create_ghz_circuit()
     
        for i, basis in enumerate(m_setting):
            if basis == 'X':
                ghz_circuit.h(i)
            elif basis == 'Y':
                ghz_circuit.sdg(i)
                ghz_circuit.h(i)
        
        ghz_circuit.measure(range(3), range(3))
        
        t_circuit = transpile(ghz_circuit, simulator)

        job = simulator.run(t_circuit, shots=shots)
        result = job.result()
        counts = result.get_counts(t_circuit)
        
        exp_val = get_expectation_value(counts, shots)
        experimental_results[m_setting] = exp_val
        
        print(f"Measurement: {m_setting}  |  Expectation Value: {exp_val:.4f}")

    print("-" * 35)
    
    ghz_product = 1
    for val in experimental_results.values():
        ghz_product *= val
        
    print(f"Product of all expectation values: {ghz_product:.4f}\n")
    
    
    print("--- Conclusion ---")
    print("Local Realism predicts the product of the measurement outcomes to be: +1.0")
    print(f"Quantum Mechanics predicts the product to be: -1.0")
    print(f"Our simulated experiment yielded a result of ~ {ghz_product:.4f}.")
    print("\n The result contradicts local realism and confirms the quantum prediction.")