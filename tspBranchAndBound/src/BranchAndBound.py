#Bibliotecas que não estiverem disponíveis na versão padrão do python devem ser baixadas
#no terminal, digite pip install - (nome_da_lib)
#exemplo: pip install pandas

import pandas as pd
import numpy as np
from scipy.spatial import distance_matrix
import math
from decimal import Decimal

# Open input file
infile = open('att48.tsp', 'r')

# Read instance header
Name = infile.readline().strip().split()[1] # NAME
FileType = infile.readline().strip().split()[1] # TYPE
Comment = infile.readline().strip().split()[1] # COMMENT
Dimension = infile.readline().strip().split()[2] # DIMENSION
EdgeWeightType = infile.readline().strip().split()[1] # EDGE_WEIGHT_TYPE
infile.readline()

# Read node list
nodelist = []
N = int(Dimension)
for i in range(0, N):
    x,y = infile.readline().strip().split()[1:]
    nodelist.append([float(x), float(y)])

print(nodelist)

A = np.array(nodelist)

print(A)

B = pd.DataFrame(distance_matrix(A, A))

print(B)

for i in B:
    for j in B:
        if j==i:
            B[i][j] = Decimal('Infinity')

print(B)
# Close input file
infile.close()