import matplotlib.pyplot as plt
import numpy as np


def variancefunc(dataacum):
    
    mmm = []
    for j in range(9):
        
        mm = []
        for t in range(48):
            
            listacum = []
            for i in range(100):

                if dataacum[j, t, i] != 0:
                    listacum.append(dataacum[j, t, i])
            m = np.mean(listacum)
            mm.append(m)

        mmm.append(mm)

    varianceall = []
    for j in range(9):
        
        variance = []
        for t in range(48):
            
            acum = []
            for i in range(100):
                
                if dataacum[j, t, i] != 0:
                    acum.append((dataacum[j, t, i] - mmm[j][t])**2)

            mean = sum(acum)/len(acum)
            variance.append(mean)

        g = sum(variance)/len(variance)
        varianceall.append(g)
    return varianceall