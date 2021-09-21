#penser a tout ecrire en anglais
# passer le .csv en .xls ? (car txt pas adapté)

#lib declaration :
import numpy as np
import re #for regular expression
import pandas as pd #!= panda
import datacleaner
import matplotlib as plt


# declaration of the name of the file we will work on, it should be in the same repository that the main, or should be the absolute path
filename = 'data1_ping.csv'


# Beginning of the main :
print("We will work on the file ",filename," \n")
file = open(filename, 'r')
fresh_data = file.read()
print(filename," file contains : \n")
print(fresh_data)
file.close()

#clean_ping(filename) #clean manually

#datacleaner data1_ping.csv -o data_clean.csv

df = pd.read_csv('data1_ping.csv', error_bad_lines=False) #the second argument permit to skip the line when unexpected fields detected
print(df)

#df = df.shape  # Shape of the dataset
print("\n")
#print(df)

x = df.isnull().sum()  #Checking Null Values
print ("the number of null value is ",x,"\n") # pb : car PING ... 0, tittle ?
dftype = df.dtypes
print(dftype,"\n")

#il peut y avoir des null (blancs/manquant) ou des junks

#clean_df = datacleaner.autoclean(df)
#print(clean_df)



# Analyze :
desc = df.describe()
print(desc,"\n")


'''print("Now we will work on the new file data_clean \n")
file = open(data_clean.txt, 'r')
datacleaned = file.read()
print(file," file contains : \n")
print(datacleaned)
file.close()'''

