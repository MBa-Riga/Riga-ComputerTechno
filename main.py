# to do : modif le format .csv en autre chose ?

# Description : Computer Technologies in Telecommunications : Homework of the week 3

#lib declaration :
import numpy as np
import re #for regular expression
import pandas as pd
import datacleaner
import matplotlib as plt
from clean_data_ping import clean_ping #for the manual cleaning


# declaration of the name of the file we will work on, it should be in the same repository that the main, or should be the absolute path
filename = 'data1_ping.csv'


# Beginning of the main :
print("We will work on the file ",filename," \n")
file = open(filename, 'r')
fresh_data = file.read()
print(filename," file contains : \n")
#print(fresh_data)
file.close()

############ CLEAN DATA ################
choose = 1 #var to choose how you want to clean your data : 0 both ways, 1 manually, 2 with librairies

# 1) Do it manually (it's suppose that we already know the form of the data, so we create a special cleaning code just for these type of data, it's not the perfect solutions but it permits to discover want we need and touch the future problems and dificulties)
if choose == 0 or choose == 1:
    filename_cleandata=clean_ping(filename)

    print("Now we will work on the new file with cleaned data",file,"\n")
    file = open(filename_cleandata, 'r')
    datacleaned = file.read()
    print(file, " file contains : \n")
    print(datacleaned)
    file.close()


# 2) Do it with librairies : panda, datacleaner ...
if choose == 0 or choose == 2:
#   Put the data in a type of panda framework
    df = pd.read_csv('data1_ping.csv', error_bad_lines=False) #the second argument permit to skip the line when unexpected fields detected
#    print(df)
# -> problem here because the file is not parse as I want (due to the shape of the data) : read_csv read data in columns and my file has data in rows
# solution to try is to transpose data ? and before split them with '   '


#   Checking how the data are interpreted
    df_type = df.dtypes
    print("type is ",df_type,"\n")
    df_info = df.info()
    print("info :\n",df_info,"\n")

#   Checking Null Values
    x = df.isnull().sum()
    print ("The number of null value is ",x,"\n")

#   Fill up blank Na (and junk value ?)
#    df_clean = datacleaner.autoclean(df)
#    print(df_clean)



################ ANALYZE DATA ##################### maybe compare it to the end of the csv file ?
# what can we analyze ? Statistics ?

df_desc = df.describe()
print("description :\n",df_desc,"\n")