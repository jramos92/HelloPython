'''
Created on 17 ene. 2020

@author: jramosm
'''

# class RevealAccess(object):
#     """A data descriptor that sets and returns values
#        normally and prints a message logging their access.
#     """
# 
#     def __init__(self, initval=None, name='var'):
#         self.val = initval
#         self.name = name
# 
#     def __get__(self, obj, objtype):
#         print('Retrieving', self.name)
#         return self.val
# 
#     def __set__(self, obj, val):
#         print('Updating', self.name)
#         self.val = val
#         
#         
# class MyClass(object):            
#     x = RevealAccess(10, 'var "x"')
#     y = 5        
#     
#     m = MyClass()
# #     m.x
# #     m.x = 20
#     m.x
#     m.y

from urllib.request import urlopen
with urlopen('http://www.google.es') as response:
    for line in response:
        line = line.decode('utf-8')  # Decoding the binary data to text.
        if 'EST' in line or 'EDT' in line:  # look for Eastern Time
            print(line)



import smtplib
server = smtplib.SMTP('localhost')
server.sendmail('soothsayer@example.org', 'jcaesar@example.org',
"""To: jcaesar@example.org
From: soothsayer@example.org

Beware the Ides of March.
""")
server.quit()