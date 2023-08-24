#DSA queue
class DSA_queue:
    def __init__(self, size = 100):
    # constructors
        self.queue = np.array([" "] * size, dtype = object) 
        self.count = 0
    #getters