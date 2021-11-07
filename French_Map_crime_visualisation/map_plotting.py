import gmplot
import csv
import pgeocode

list_latitude = []
list_longitude = []
list_typelieu = []

#create the Base Map
gmap = gmplot.GoogleMapPlotter(46.2276,2.2137,6)
gmap.apikey = "AIzaSyBCM3UyXqoHNROPX50pxU5eFE3h95Bv-50"

with open('for_map_plotting.csv','r') as file:
  read_file = csv.reader(file,delimiter=',')
  for row in read_file:
    list_latitude.append(row[3])
    list_longitude.append(row[4])
    list_typelieu.append(row[1])

list_latitude.pop(0)
list_longitude.pop(0)
list_typelieu.pop(0)


def colour_code(typelieu):
  colour = 'b'
  if typelieu == 'BQ':
    colour = 'blue'
  elif typelieu == 'BT':
    colour = 'green'
  elif typelieu == 'SM':
    colour = 'red' 
  elif typelieu == 'SU':
    colour = 'orange'
  elif typelieu == 'AC':
    colour = 'pink'
  elif typelieu == 'BJ':
    colour = 'purple'
  elif typelieu == 'PH':
    colour = 'black'
  else:
    colour = 'white'
  return colour

print("colour code:",colour_code('BQ'))
for i in range(len(list_latitude)):
  curr_colour = colour_code(list_typelieu[i])
  list_latitude[i] = float(list_latitude[i])
  list_longitude[i] = float(list_longitude[i])
  gmap.marker(list_latitude[i],list_longitude[i],curr_colour, size = 40, marker = False )

gmap.draw("/Users/mariegouilliard/Desktop/Nukkai/Braquage/Csv_pgadmin/mapthree.html")