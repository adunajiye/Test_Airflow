import json
import requests
from pprint import pprint
import psycopg2
import datetime


def save_inventory():
    print('Connecting to the PostgreSQL database...')
    try:
        conn = psycopg2.connect(
            host= "db-postgresql-lon1-10501-do-user-15128192-0.c.db.ondigitalocean.com",
            database= "defaultdb",
            user= "doadmin",
            password= "AVNS_18bVhfxQtTTBCXwY6Lw",
            port=25060
        )
        cur = conn.cursor() 
        # Pull data from Dodois
        Inv_object = requests.get("https://vm-backend-ane5.onrender.com/inventory")
        Inv_object  = Inv_object .json()
        print(Inv_object)
            
            
        for data in Inv_object['data']:
            inventory_list = data
            # print(port_list)
    
            """
            Loop Through data list and pass neccessary Info
            """
            for list in inventory_list:
                cur.execute('SELECT * from "Inventory" where "Id" = %s',[data['id']])
                inv = cur.fetchall()
                if len(inv) == 0:
                    print(data['name']) 
                    cur.execute('Insert Into "Inventory" ("Inventory_Id", "Date","Product_Type","Product_Quantity","Amount_Payabale","Weight_Slip_Url","Created_At","Updated_At","Comments","Comment_Type") values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',([data['inventoryId'],data['date'],data['productType'],data['productQuantity'],data['amountPayable'],data['weightSlipUrl'],data['createdAt'],data['updatedAt'],data['comments']['comment'],data['comments']['type']]))
                    print("Added to Inventory " + data['inventoryId'])
            conn.commit()    
            # close the communication with the PostgreSQL
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        print('Database connection closed.')
save_inventory()