# Darwinian-Testing
A genetic algorithm written in Python for generating test cases to test software and embedded systems

# Summary

This project was created for generation and evaluation of test cases using machine learning techniques. The algorithm of choice is the genetic algorithm.

The genetic algorithm mimics Charles Darwin’s theory of evolution for creating and evaluating solutions; a key in the process is the so called ’fitness score’ of the solutions. Solutions of higher fitness are more likely to be selected for procreation of new solutions through cross-over of parameter values. Mutations can also occur, the benefit of which is an increased reachability of the solutions.

This algorithm uses a roulette wheel selection algorithm for selecting parent solutions. The selection algorithm is biased towards higher fitness solutions, while not excluding solutions of lower fitness.

# Use

In order to utilize the algorithm for generating test cases, it is necessary that the user makes smaller adjustments the code to fit his or her specific problem.

A script that reads the problem specific data and extracts the data to a matrix of parameter values is required. Each column of the matrix should correspond to one parameter, and each row should correspond to a state or point in time.

Also, a script which either is a model of the system under test, or a connection to a physical system under test is required. The script should return a test verdict (pass/fail) for each test case.
