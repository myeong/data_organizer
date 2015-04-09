from pygeocoder import Geocoder
import csv
import time

googleGeocodeUrl = 'http://maps.googleapis.com/maps/api/geocode/json?'

path = r'C:\Users\LM\git\meetup\pitt_march_9.csv'
path2 = r'C:\Users\LM\git\meetup\pitt_march_9_new.csv'
cnt_list = [[0 for x in range(4)] for x in range(1000)]

def get_coordinates(query, from_sensor=False):
    query = query.encode('utf-8')
    results = Geocoder.geocode(query).coordinates
    return results
 
with open(path, newline='') as csvfile:
    line = csv.reader(csvfile, delimiter=',')
     
    i = 0    
    coor = []    
    
    for row in line:        
        cnt_list[i][0] = i
        cnt_list[i][1] = row[3] #venue name
         
        if row[1]=="" or row[2]=="" or row[1] == "0" or row[2] == "0":
            if row[4]!="":
                coor = get_coordinates(row[4], False)
                cnt_list[i][2] = coor[0] #lat
                cnt_list[i][3] = coor[1] #lon
                time.sleep(0.1)
                print("coded " + row[4])
            else:
                continue
        else:
            cnt_list[i][2] = row[1]; #lat        
            cnt_list[i][3] = row[2]; #lon

        i += 1
    
    print("successful")
 
 
with open(path2, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')   
    for k in cnt_list:
        writer.writerow(k)