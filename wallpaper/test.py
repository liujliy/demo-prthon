import os

import psutil

x = [1, 2, 3]

def test():
    x.append(4)

test()
print(x)