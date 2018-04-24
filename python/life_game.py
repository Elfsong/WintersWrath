#coding: utf-8

import time
import numpy as np
import subprocess

class LifeSpace:
    def __init__(self, name, israndom, size_x, size_y):
        self.name = name
        self.israndom = israndom
        self.size = (size_x, size_y)
        self.iter_times = 0
        self.Z = Z = np.random.randint(0, 2, self.size)
        
    def iterate(self):
        # Count neighbours
        N = (self.Z[0:-2, 0:-2] + self.Z[0:-2, 1:-1] + self.Z[0:-2, 2:] +
             self.Z[1:-1, 0:-2]                      + self.Z[1:-1, 2:] +
             self.Z[2:  , 0:-2] + self.Z[2:  , 1:-1] + self.Z[2:  , 2:])

        # Apply rules
        birth = (N == 3) & (self.Z[1:-1, 1:-1] == 0)
        survive = ((N == 2) | (N == 3)) & (self.Z[1:-1, 1:-1] == 1)
        self.Z[...] = 0
        self.Z[1:-1, 1:-1][birth | survive] = 1

        # Iterate update
        self.iter_times += 1
    
    def get_Z_status(self):
        print("--"*(self.size[0]/2) + str(self.iter_times)  + "--"*(self.size[0]/2))
        line = ''
        for i in self.Z: 
            for j in i: line += "■" if j == 1 else "□"
            print line
            line = ''
                

    def process(self, iter_time):
        for i in range(iter_time): 
            self.iterate()
            self.get_Z_status()
            time.sleep(0.3)
            subprocess.call("clear")

if __name__ == "__main__":
    newspace = LifeSpace("Elf", True, 15, 30)
    newspace.process(1000)
