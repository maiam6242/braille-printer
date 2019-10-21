import numpy as np
symbols = {'A' : np.array([1,0][0,0][0,0]),
           'B' : np.array([1,0][1,0][0,0]),
           'C' : np.array([1,1][0,0][0,0]),
           'D' : np.array([1,1][0,1][0,0]),
           'E' : np.array([1,0][0,1][0,0]),
           'F' : np.array([1,1][1,0][0,0]),
           'G' : np.array([1,1][1,1][0,0]),
           'H' : np.array([1,0][1,1][0,0]),
           'I' : np.array([0,1][1,0][0,0]),
           'J' : np.array([0,1][1,1][0,0]),
           'K' : np.array([1,0][0,0][1,0]),
           'L' : np.array([1,0][1,0][1,0]),
           'M' : np.array([1,1][0,0][1,0]),
           'N' : np.array([1,1][0,1][1,0]),
           'O' : np.array([1,0][0,1][1,0]),
           'P' : np.array([1,1][1,0][1,0]),
           'Q' : np.array([1,1][1,1][1,0]),
           'R' : np.array([1,0][1,1][1,0]),
           'S' : np.array([0,1][1,0][1,0]),
           'T' : np.array([0,1][1,1][1,0]),
           'U' : np.array([1,0][0,0][1,1]),
           'V' : np.array([1,0][1,0][1,1]),
           'W' : np.array([0,1][1,1][0,1]),
           'X' : np.array([1,1][0,0][1,1]),
           'Y' : np.array([1,1][0,1][1,1]),
           'Z' : np.array([1,0][0,1][1,1]),
           '1' : np.array([0,1,1,0][0,1,0,0]
           [1,1,0,0]),
           '2' : np.array([0,1,1,0][0,1,1,0]
           [1,1,0,0]),
           '3' : np.array([0,1,1,1][0,1,0,0]
           [1,1,0,0]),
           '4' : np.array([0,1,1,1][0,1,0,1]
           [1,1,0,0]),
           '5' : np.array([0,1,1,0][0,1,0,1]
           [1,1,0,0]),
           '6' : np.array([0,1,1,1][0,1,1,0]
           [1,1,0,0]),
           '7' : np.array([0,1,1,1][0,1,1,1]
           [1,1,0,0]),
           '8' : np.array([0,1,1,0][0,1,1,1]
           [1,1,0,0]),
           '9' : np.array([0,1,0,1][0,1,1,0]
           [1,1,0,0]),
           '0' : np.array([0,1,0,1][0,1,1,1]
           [1,1,0,0]),
           ' ' : np.array([0,0][0,0][0,0]),
           ',' : np.array([0,0][1,0][0,0]),
           ';' : np.array([0,0][1,0][1,0]),
           ':' : np.array([0,0][1,1][0,0]),
           '.' : np.array([0,0][1,1][0,1]),
           '!' : np.array([0,0][1,1][1,0]),
           "'" : np.array([0,0][0,0][1,0]),
           '-' : np.array([0,0][0,0][1,1]),
           '?' : np.array([0,0][1,0][1,1]),
           '#' : np.array([0,1][0,1][1,1]),
           '(' : np.array([0,0][1,1][1,1]),
           ')' : np.array([0,0][1,1][1,1]),
           'opening "' : np.array([0,0][1,0][1,1]),
           'closing "' : np.array([0,0][0,1][1,1]),
           'cap letter' : np.array([0,0][0,0][0,1]),
           'cap word' : np.array([0,0,0,0][0,0,0,0]
           [0,1,0,1]),
           '_' : np.array([0,1,0,0][0,0,0,0]
           [0,1,1,1]),
           '[' : np.array([0,1,1,0][0,0,1,0]
           [0,1,0,1]),
           ']' : np.array([0,1,0,1][0,0,0,1]
           [0,1,1,0]),
           '*' : np.array([0,0,0,0][0,1,0,1]
           [0,0,1,0]),
           '$' : np.array([0,1,0,1][0,0,1,0]
           [0,0,1,0])
           }

