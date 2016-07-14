import string
import numpy as np
import pandas as pd
import heapq

VOTES = "/Users/roycohen/Documents/linear algebra HW/UN_voting_data.txt"

A=pd.read_table(VOTES, skipinitialspace=True, index_col=0, sep=' ', header=None)
AT=A.transpose()
M=AT.dot(A)
Mtag=A.dot(AT)
