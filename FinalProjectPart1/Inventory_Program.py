import csv
from datetime import datetime, date
from Asc_Date_Sort_ServiceDatesList_csv import datesorted 
from Desc_Sort_PriceList_csv import pricesorted 


manufacturerList_sorted = []
full_inventory_list = []

with open ("ManufacturerList.csv", 'r') as csv_manufacturerlist: #file_object
    manufacturerlist_csv = csv.reader (csv_manufacturerlist, skipinitialspace=True) #csv reader object
    next(manufacturerlist_csv) #skips header row in csv file "item_id, service_date"

    for i in manufacturerlist_csv:
        cleaned_item = [j.strip() for j in i if j!=''] #removes whitepsaces in csv while ignoring the last comma to prevent appending a null, 'if_damaged' field
        
        manufacturerList_sorted.append(cleaned_item)
    
    #Sorts lists of items by manufacturers asc (ex: 'Apple', 'Dell', 'Lenovo'), position 1 [['1167234', 'Apple', 'phone'],[item2_id, manufacturer, item_type],...]
    #Sorts lists of items by item_type asc (ex: 'laptop', 'phone', 'tower'), position 2 [['1167234', 'Apple', 'phone'],[item2_id, manufacturer, item_type],...]
    manufacturerList_sorted.sort(key=lambda x: (x[1], x[2])) 
    
    # manufacturerList_array [['2347800', 'Apple', 'laptop'], ['1167234', 'Apple', 'phone'], 
    # ['2390112', 'Dell', 'laptop'], ['9034210', 'Dell', 'tower'], ['7346234', 'Lenovo', 'laptop', 'damaged'], 
    # ['1009453', 'Lenovo', 'tower'], ['3001265', 'Samsung', 'phone']]
    
# print('manu sorted', manufacturerList_sorted)


# Corresponding item price with manufacturerlist using imported 'sortedprice' array
for i in manufacturerList_sorted:
    for j in pricesorted:
        for k in datesorted:
            if i[0] == j[0] and i[0] == k[0]: #if item_id matches in manufacturerList_sorted & in pricesorted
                i.insert (3, j[1]) #insert item price date into pos 3 manufactureList_sorted
                i.insert(4, k[1]) #insert item date into pos 2 manufactureList_sorted
                full_inventory_list.append(i) #append the new item list that includes ex: ['item_id', 'manufacturer', 'item_type', 'item_price']


# print('full inventory list', full_inventory_list)

def writing_full_inventory_csv():
    with open('FullInventory.csv', 'w', newline='') as full_inventory_csv:
        write_full_inventory_csv = csv.writer(full_inventory_csv)
        write_full_inventory_csv.writerows(full_inventory_list)
    print("FullInventory.csv written successfully!")


def writing_item_type_csv():
    diff_item_type = [] #storing diff item_type
    for i in full_inventory_list: #looping thru items in inventory to target i[2], which is the item_type (ex: laptop, phone)
        x_item_type_list = []
        if(i[2] not in diff_item_type): #if item_type not in item_type[], then loop thru full_inventory for that diff item_type
            diff_item_type.append(i[2]) #append new item_type ['phone','laptop'...]
            with open(f'{i[2].capitalize()}Inventory.csv', 'w', newline='') as item_type_csv: #creating {Item_type}Inventory.csv file (ex: "LaptopInventory.csv")
                write_csv_item_type = csv.writer(item_type_csv)
                for j in full_inventory_list: #for appending item records related to the item_type chosen, i[2]. Loop item_type, i[2], in full_inventory_list until it's done
                    if i[2] == j[2]: #if the item_type, i[2], == j[2] then write down tht item_type record, (j), into {item_type}Inventory.csv
                        
                        x_item_type_list.append(j[0:2]+j[3:])                        

                x_item_type_list.sort(key=lambda x: x[0]) #sorting each item record by item_id

                write_csv_item_type.writerows(x_item_type_list) #appending item record in full_inventory[] for item_type, i[2] ; j[0:2]+j[3:] is here to remove item_type. 2347800,Apple + 999,7/3/2020
                print(f'{i[2].capitalize()}Inventory.csv written successfully!')
                
                
if __name__ == "__main__":
    print('Full Inventory List:')
    writing_full_inventory_csv()
    print()
    print('Item Type Inventory List:')
    writing_item_type_csv()

# print('pricesorted', pricesorted)
# print('datesorted',datesorted)