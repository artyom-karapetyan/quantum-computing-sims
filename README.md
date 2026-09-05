# Simulation of Quantum Protocols learnt during Oxford Quantum Club

Implementations of quantum information protocols using Python, Qiskit, and NumPy:
- Superdense Coding
- Quantum Teleportation
- Bell's Inequality
- GHZ test

## How to run

Create and activate a virtual environment, then install the required packages:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install qiskit qiskit-aer numpy matplotlib
```

Run any simulation from the repository root:

```bash
python src/quantum_dense_coding.py
python src/quantum_teleportation.py
python src/bell_inequality_checker.py
python src/ghz_test.py
```

## Resources

The resources folder contains useful materials for this project. All materials are credited to Alexander Lvovsky's *Quantum Physics: An Introduction Based on Photons* book (Springer, 2018), except for the trigonometry cheat sheet.