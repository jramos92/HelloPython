'''
Created on 4 feb. 2020

@author: jramosm
'''


try:
    print(1 / 0)
except Exception as exc:
    raise RuntimeError("Something bad happened") from exc