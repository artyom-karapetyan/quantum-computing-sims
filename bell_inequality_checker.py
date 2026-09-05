import numpy as np
from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator

def create_psi_minus_bell_state():
    qc = QuantumCircuit(2)
    qc.x(0) 
    qc.x(1) 
    qc.h(0) 
    qc.cx(0, 1) 
    return qc

def calculate_expectation_value(counts, shots):
    expectation_value = 0
    for outcome, count in counts.items():
        parity = -1 if outcome.count('1') % 2!= 0 else 1
        expectation_value += parity * (count / shots)
    return expectation_value

def run_chsh_test():

    alice_angles = [0, np.pi / 2]
    bob_angles = [np.pi / 4, 3 * np.pi / 4]
    

    correlations = []
    simulator = AerSimulator()
    shots = 8192

    print("Running 4 CHSH circuits...")

    for alice_angle in alice_angles:
        for bob_angle in bob_angles:
            
            chsh_circuit = create_psi_minus_bell_state()
            chsh_circuit.barrier()

            if alice_angle!= 0:
                chsh_circuit.ry(-alice_angle, 0) 
            if bob_angle!= 0:
                chsh_circuit.ry(-bob_angle, 1)   
            
            chsh_circuit.measure_all()

            t_circuit = transpile(chsh_circuit, simulator)
            result = simulator.run(t_circuit, shots=shots).result()
            counts = result.get_counts()
            
            correlation = calculate_expectation_value(counts, shots)
            correlations.append(correlation)
            
            print(f"  - Alice angle: {alice_angle/np.pi:.2f}π, Bob angle: {bob_angle/np.pi:.2f}π -> Correlation: {correlation:.4f}")

    chsh_value = correlations[0] - correlations[1] + correlations[2] + correlations[3]

    print("\n--- CHSH Test Results ---")
    print(f"E(a, b)   = {correlations[0]:.4f}")
    print(f"E(a, b')  = {correlations[1]:.4f}")
    print(f"E(a', b)  = {correlations[2]:.4f}")
    print(f"E(a', b') = {correlations[3]:.4f}")
    print("-------------------------")
    print(f"CHSH Value |S| = |{correlations[0]:.2f} - ({correlations[1]:.2f}) + {correlations[2]:.2f} + {correlations[3]:.2f}| = {abs(chsh_value):.4f}")
    print("-------------------------")

    if abs(chsh_value) > 2:
        print(f"\nViolation of Bell's Inequality Confirmed!")
        print(f"The result {abs(chsh_value):.4f} is greater than the classical limit of 2.")
        print(f"The theoretical maximum for quantum mechanics is 2√2 ≈ 2.828.")
    else:
        print("\nNo violation of Bell's Inequality was observed.")

# Run the main function
if __name__ == "__main__":
    run_chsh_test()