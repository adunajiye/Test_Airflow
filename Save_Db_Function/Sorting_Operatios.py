import json
import requests
from pprint import pprint
import psycopg2
import datetime


def save_sorts_operations():
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
        sort_op_object_poly = requests.get("https://vm-backend-ane5.onrender.com/sorting-operation?company=Polyforte")
        sort_op_object_poly = sort_op_object_poly.json()
        print(sort_op_object_poly)
        
        sort_op_object_safari = requests.get("https://vm-backend-ane5.onrender.com/sorting-operation?company=Safari Polymers")
        sort_op_object_safari = sort_op_object_safari.json()
        print(sort_op_object_safari)

        for data in sort_op_object_safari['data']:
            sort_op_list_safari = data
            # print(port_list)
            
        for data in sort_op_object_poly['data']:
            sort_op_list_poly = data
            # print(port_list)
    
            """
            Loop Through data list and pass neccessary Info
            """
            for list in data:
                cur.execute('SELECT * from "SortingOperations" where "Id" = %s',[data['id']])
                sorts_op_safari = cur.fetchall()
                if len(sorts_op_safari) == 0:
                    print(data['name']) 
                    cur.execute('Insert Into "SortingOperations" ("Sorting_Id","Date","Currency","Company_Name","Exchange_Rate", "Created_At","Updated_At","Quantity_Sorted","Amount_Paid","Amount_Paid_USD") values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',([data['sortingId'],data['date'],data['currency'],data['company'],data['exchnageRate'],data['createdAt'],data['updatedAt'],data['quantitySorted'],data['amountPaid'],data['amountPaidInUsd']]))
                    print("Added Safari to SortingOpearations " + data['name'])
                    
            for list in sort_op_list_poly:
                cur.execute('SELECT * from "SortingOperations" where "Id" = %s',[data['id']])
                sorts_op = cur.fetchall()
                if len(sorts_op) == 0:
                    print(data['name']) 
                    cur.execute('Insert Into "SortingOperations" ("Sorting_Id","Date","Currency","Company_Name","Exchange_Rate", "Created_At","Updated_At","Quantity_Sorted","Amount_Paid","Amount_Paid_USD") values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',([data['sortingId'],data['date'],data['currency'],data['company'],data['exchnageRate'],data['createdAt'],data['updatedAt'],data['quantitySorted'],data['amountPaid'],data['amountPaidInUsd']]))
                    print("Added Ployforte to SortingOpearations " + data['name'])
            conn.commit()    
            # close the communication with the PostgreSQL
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')
save_sorts_operations()