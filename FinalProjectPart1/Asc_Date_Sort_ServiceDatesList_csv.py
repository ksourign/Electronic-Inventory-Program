#Takes "ServiceDatesList.csv" (item_id, service_date) and creates a list that sorts dates least to greatest with corresponding ID 
#Ex: datesorted [['item_id','service_date'], ['item2_id', 'item2_service_date']]

import csv
from datetime import datetime, date

service_date_sorted = [] #final ServiceDatesList sorted (dates sorted asc w/ corresponding item_id)
PastServiceDate_array = []


with open ("ServiceDatesList.csv", 'r') as csv_servicedates:
    PastServiceDate_csv = csv.reader (csv_servicedates)
    next(PastServiceDate_csv) #skips header row in csv file "item_id, service_date"
    for i in PastServiceDate_csv:
        service_date_sorted.append (datetime.strptime(i[1], "%m/%d/%Y").date()) 
        # extracts and appends position 1 (service_Date) for each row of csv data [item_id (0), service_date (1)] into datesorted array,
        # while also converting from string dates into datetime objects to sort dates least to greatest
        
        # Ex:
        # # before: PastServiceDate_csv [['7346234', '9/1/2020'],['item2_id', 'item2_service_date']...]
        # # after: datesorted [datetime.date(2020, 9, 1),...]
        
        PastServiceDate_array.append(i) #appends original csv into an array to be used for corresponding sorted dates with item_id later
  

    service_date_sorted.sort () #dates sorted asc
    service_date_sorted = [[x] for x in service_date_sorted] #wrapping each price into its own list
    # Ex: datesorted [[datetime.date(2020, 5, 27)], [datetime.date(2020, 7, 2)], [datetime.date(2020, 7, 3)],...]


# looping thru datesorted to match corresponding item_id in PastServiceDate_array
    for i in service_date_sorted:
        for j in PastServiceDate_array:
            if i[0] == datetime.strptime(j[1], "%m/%d/%Y").date(): #comparing sorted date objects with date objects of PastServiceDate_array (original csv)
                i[0] = j[1] 
                #date object of sorted date, i[0], becomes the service_date, j[1]
                # before: datesorted [[datetime.date(2020, 5, 27)],...]
                # after: datesorted [['5/27/2020'], ['date2']...]

                i.insert(0, j[0])  
                # inserts corresponding item_id, j[0], to the start, (0), of the datesorted to match original csv
                # before: datesorted [['5/27/2020'],...]
                # after: datesorted [['9034210', '5/27/2020'],...]


if __name__ == "__main__": #only run this code if executing this file directly
    print(service_date_sorted)











