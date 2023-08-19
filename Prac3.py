#بسم الله الرحمن الرحيم
import numpy as np

#DSA stack
class DSA_stack:
    def __init__(self, size = 100):
    #constructors
        self.stack = np.array([" "] * size, dtype = object)
        