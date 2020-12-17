"""This is first quantum computin program
Author   : Sibasish Brahma

Created date : 21st Aug, 2020

Modified date :

Description: Creating a first quantum circuit
"""

import cirq

circuit = cirq.Circuit()

(q0,q1) = cirq.LineQubit.range(2)

circuit.append([cirq.H(q0),cirq.CNOT(q0,q1)])
circuit.append([cirq.measure(q0),cirq.measure(q1)])

sim = cirq.Simulator()
results = sim.run(circuit, repetitions = 10 )
print(results)

device = cirq.google.Bristlecone
circuit2 = cirq.Circuit(device=device)
a0,a1 = cirq.GridQubit(5,5) , cirq.GridQubit(5,6)
b0,b1 = cirq.GridQubit(6,5) , cirq.GridQubit(6,6)

circuit2.append([cirq.CZ(a0,a1) , cirq.CZ(b0,b1)])

print(circuit2)



#print(circuit)


