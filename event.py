import csv
import re

path = r'C:\Users\LM\Dropbox2\Dropbox\Event_Data\comparison\pittevent2_raw.csv'
path2 = r'C:\Users\LM\Dropbox2\Dropbox\Event_Data\comparison\Pittsburghevents2_new.csv'
cnt_list = [[0 for x in range(5)] for x in range(200)]

with open(path, newline='') as csvfile:
    line = csv.reader(csvfile, delimiter=',')
    
    i = 0
    j = 0
    index = 0
    index1 = 0
    index2 = 0
    iaddr = 0
    
    for rows in line:
        row = ','.join(rows)
        row = row.replace(',', '')        
        
#         area = re.search('(Oakland|Lawrenceville|Bloomfield|Shadyside)', row)
        area = re.search('(Shadyside|Squirrel Hill)', row)
        if area:
            cnt_list[i][0] = area.group(0)
            index = area.span()[1] 
        
        continues = re.search('([Cc]ontinues [Tt]hrough|[Tt]hrough)\s(March|April|May|June|July|August)\s\d\d', row)
        if continues:
            cnt_list[i][2] = continues.group(0)
            index1 = continues.span()[0]
            
        if index1 == 0:        
            date = re.search('(March|April)\s\w\w', row)
            if date and cnt_list[i][2]==0:
                cnt_list[i][2] = date.group(0)
                index1 = date.span()[0]
                
        
        m = re.search('\d{3}[-]\d{3}[-]\d{4}', row)
        if m:                 
            cnt_list[i][3] = m.group(0)
            index2 = m.span()[1] +1   
            if index1 == 0:
                index1 = m.span()[0]            
        
        cnt_list[i][1] = row[index:index1]               

        addr = re.search('\d{3,4}', row[index2:])
        
        if addr:
            iaddr = addr.span()[0] + index2              
            cnt_list[i][4] = row[iaddr:]+ '. PA'
        else:
            cnt_list[i][4] = row[index2:] + '. PA'
        
        index = 0
        index1 = 0
        index2 = 0
        iaddr = 0
        print (cnt_list[i]) 
        
        i += 1


with open(path2, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')   
    for k in cnt_list:
        writer.writerow(k)