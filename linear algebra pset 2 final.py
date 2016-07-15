import string
import numpy as np
import pandas as pd
import heapq

VOTES = "/Users/roycohen/Documents/linear algebra HW/UN_voting_data.txt"

A=pd.read_table(VOTES, skipinitialspace=True, index_col=0, sep=' ', header=None)
AT=A.transpose()
M=AT.dot(A)
Mtag=A.dot(AT)

##Q1
Mtag_stack=Mtag.stack().nsmallest(1)

print 'The two countries most opposed on voting are: ' + str(Mtag_stack.index[0][0])+ ' and ' +str(Mtag_stack.index[0][1])
print

##Q2
print 'The ten countries most opposed countries on voting are:'
Mtag_stack=Mtag.stack().nsmallest(20)
for i in range (0,20):
    if i%2==0:
       print str(Mtag_stack.index[i][0])+ ' and ' +str(Mtag_stack.index[i][1])
       
print

##Q3
mostAgreeableDot=0
mostAgreeableCountries=[]
r=0
for index in Mtag:
    c=0
    for col in Mtag.index:
       c+=1 
       if r<206 and c<206:
          value=Mtag.get_value(r,c,takeable=True)
          if index!=col and value>mostAgreeableDot:
             mostAgreeableCountries=[]
             mostAgreeableCountries.append(index)
             mostAgreeableCountries.append(col)
  
    r+=1
print 'The two countries in the greatest agreement are: ' + str(mostAgreeableCountries[0]) + ' and '+ str(mostAgreeableCountries[1])
print

Mtag_stack1=Mtag.stack().nsmallest(2)