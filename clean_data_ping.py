# Description : do a "manual" cleaning and shaping of data

#lib declaration :
import numpy as np
import re #for regular expression


def clean_ping(filename):
    #create a new file, filename_clean, containing the cleaned filename's data

    print('hello clean \n')
    file = open(filename, 'r')
    fresh_data = file.readlines()
    row = np.size(fresh_data)
    print("le nombre de ligne est ",row,"\n")
    file.close()

    new_file = open(filename+'_clean.csv', 'w+')  # we create a new file or rewrite it if it already exists
    cleaned_data = np.zeros((row), str)

    for i in range (0,5): #modif 5 = row
        I = 0
        if (re.search('bytes from 8.8.8.8',fresh_data[i])!=None):
            d = re.split(':', fresh_data[i])
            d = re.split(' ', d[1])
            print("d", i, "= ", d)
            for k in range(1,len(d),1): #we jump the [0] because it's empty for the data we want
                DC = []
                dc = re.split('=', d[k]) #penser à supprimer la case vide d i=1 k=0 avec pop ? apres DC
                print("dc =",dc,"\n")
                for l in range (0,len(dc),1):
                    if l != '':
                        # shape or parse with ; or '    ' , try to put data in columns ?
                        '''print("dc[l] =",dc[l],"\n")
                        DC.append(l)
                print("DC = ",DC,"\n")

                if len(DC)!=0:
                    cleaned_data[I] = DC
                    I+=1 '''
        else:
            print("the row ",i," isn't a data \n")
            #other is the garbage var, to see what we delete
            other += fresh_data[i]
            other += '\n'

    new_file.write(cleaned_data)
    new_file.close()
    return (filename+'_clean.csv')