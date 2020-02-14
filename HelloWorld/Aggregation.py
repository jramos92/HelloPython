'''
Created on 31 ene. 2020

@author: jramosm
'''

import operator

output = dict()
container =  [[u'unicode_text', 5, 395, 2, 0, 2],
              [u'unicode_text', 235, 5, 3, 3, 10],
              [u'other_unicode_text', 3, 65, 28, 16, 52],
              [u'unicode_text', 95, 5, 8, 7, 38]]

for sublist in container:
    try:
        output[sublist[0]] = map(operator.add, output[sublist[0]], sublist[1:])
    except KeyError:
        output[sublist[0]] = sublist[1:]