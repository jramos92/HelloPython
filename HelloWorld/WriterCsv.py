'''
Created on 5 feb. 2020

@author: jramosm
'''
import csv
with open( "C:\\Users\\jramosm\\Downloads\\eggs.csv", 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=' ',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow(['Spam'] * 5 + ['Baked Beans'])
    spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])