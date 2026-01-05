import numpy as np
def stat ():
    #importing data
    data = np.loadtxt ("populations.txt", skiprows = 1)
    
    #Createing hare
    hare = data[:,1]
    
    #Finding the min year of hare with np.argmin
    min_hare_index = np.argmin(hare)
    
    min_year_hare = data[min_hare_index, 0]
    
    lynx_avg = np.mean(data[:, 2])
    
    species_sum = np.sum(data[:, 1:], axis=1)
    
    new_data = np.column_stack((data, species_sum))
    
    mask = new_data[:, 3] < 40000
    new_data[mask, 3] = 0
    
    return data, hare, min_year_hare, lynx_avg, new_data
