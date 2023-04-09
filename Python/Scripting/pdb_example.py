#!/usr/bin/python
# This Python file uses the following encoding: utf-8

class Student:
    def __init__(self, std):
        self.count = std
    def print_std(self):
        for i in range(self.count):
            print(i)
        return
                        
if __name__ == '__main__':
    Student(5).print_std()

"""
    python3 -m cProfile pdb_example.py
    0
    1
    2
    3
    4
            12 function calls in 0.001 seconds

    Ordered by: standard name

    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
            1    0.000    0.000    0.001    0.001 pdb_example.py:4(<module>)
            1    0.000    0.000    0.000    0.000 pdb_example.py:4(Student)
            1    0.000    0.000    0.000    0.000 pdb_example.py:5(__init__)
            1    0.000    0.000    0.001    0.001 pdb_example.py:7(print_std)
            1    0.000    0.000    0.000    0.000 {built-in method builtins.__build_class__}
            1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
            5    0.001    0.000    0.001    0.000 {built-in method builtins.print}
            1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""