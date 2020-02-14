'''
Created on 11 feb. 2020

@author: jramosm
'''



from Bio import SeqIO

sizes = [len(rec) for rec in SeqIO.parse("C:\\Users\\jramosm\\Downloads\\ls_orchid.fasta", "fasta")]

import pylab

pylab.hist(sizes, bins=20)
pylab.title(
    "%i orchid sequences\nLengths %i to %i" % (len(sizes), min(sizes), max(sizes))
)
pylab.xlabel("Sequence length (bp)")
pylab.ylabel("Count")
pylab.show()