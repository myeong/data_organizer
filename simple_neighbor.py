from pygeocoder import Geocoder
import csv
import time
import re
from pygeolib import GeocoderError

googleGeocodeUrl = 'http://maps.googleapis.com/maps/api/geocode/json?'

# path = r'C:\Users\LM\Dropbox2\Dropbox\Event_Data\comparison\final_physical.csv'
# path2 = r'C:\Users\LM\Dropbox2\Dropbox\Event_Data\comparison\final_physical_coor.csv'
path = r'C:\Users\LM\Dropbox2\Dropbox\Event_Data\comparison\total_phy_addr.csv'
path2 = r'C:\Users\LM\Dropbox2\Dropbox\Event_Data\comparison\total_phy_coor_rest.csv'
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
        cnt_list[i][0] = row[0]
        cnt_list[i][1] = 0
         
        try:
            coor = get_coordinates(re.escape(row[1]), False)
        except GeocoderError:
            i += 1
            continue
        
        cnt_list[i][2] = coor[0] #lat
        cnt_list[i][3] = coor[1] #lon
        time.sleep(0.1)         # added time interval due to the constraints for bursting queries
        print(str(i) + ": coded " + row[1] + ' ' + str(coor[0]) + ',' + str(coor[1]))
 
        i += 1
     
    print("successful")
 
 
with open(path2, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')   
    for k in cnt_list:
        writer.writerow(k)