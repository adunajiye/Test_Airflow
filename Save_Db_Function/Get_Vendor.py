import json
import requests
from pprint import pprint
import psycopg2
import datetime


def save_vendor():
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
        Vendor_object = requests.get("https://vm-backend-ane5.onrender.com/vendor")
        Vendor_object  = Vendor_object .json()
        print(Vendor_object)
            
            
        for data in Vendor_object['data']:
            vendor_list = data
            # print(port_list)
    
            """
            Loop Through data list and pass neccessary Info
            """
            for list in vendor_list:
                cur.execute('SELECT * from "Vendor" where "Id" = %s',[data['id']])
                ven = cur.fetchall()
                # len(ven) == 0
                print(data['name']) 
                cur.execute('Insert Into "Vendor" ("Name,"Created_At","Updated_At") values (%s,%s,%s)',([data['name'],data['createdAt'],data['updatedAt']]))
                print("Added to Vendor" + data['name'])
            conn.commit()    
            # close the communication with the PostgreSQL
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        print('Database connection closed.')
save_vendor()