import csv
import pgeocode
import numpy as np
#declare lists
list_row = []

list_code_postale = []
list_longitude = []
list_latitude = []

#------------Add information to the lists-----------------------#

with open('carte_colourcode.csv','r') as csv_file:
    read_file = csv.reader(csv_file,delimiter=',')
    #write_file = csv.writer(csv_file,delimiter='')
    for row in read_file:
        list_row.append(row)

for i in range(len(list_row)):
    #print(list_row[i][2])
    list_code_postale.append(list_row[i][2])

list_code_postale.pop(0)

#get the longitude and latitude of your data
nomi = pgeocode.Nominatim('fr')
total = nomi.query_postal_code("75013")
#print(total.longitude)
#print(total.latitude)

#latitude then longitude

for i in range(len(list_code_postale)):
  #print(list_code_postale[i])
  curr = nomi.query_postal_code(list_code_postale[i])
  list_longitude.append(curr.longitude)
  list_latitude.append(curr.latitude)

#print("length",len(list_latitude))
#print("test",list_latitude[566])



for i in range(len(list_latitude)):
    if(np.isnan(list_latitude[i]) or np.isnan(list_longitude[i]) ):
        #print("enter")
        list_latitude[i] = 48.8566
        list_longitude[i] = 2.3522
    #print("longitude:",list_longitude[i])
    
for i in range(len(list_latitude)): 
    print(list_longitude[i])

  

