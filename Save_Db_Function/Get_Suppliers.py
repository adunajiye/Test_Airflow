import json
import requests
from pprint import pprint
import psycopg2
import datetime


def save_suppliers():
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
        # Pull data from Suppliers APIs
        payload = {}
        headers = { 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6ImFkdW5haml5ZUBnbWFpbC5jb20iLCJzdWIiOjMsImlhdCI6MTcwNDAxMTE5OSwiZXhwIjoxNzA2NjAzMTk5fQ.02RS6sqOLk8-cpZXmQeqF6fnojcXBnpTh92Rb4BpE9A'}
        suppliers_url = "https://vm-backend-ane5.onrender.com/supplier"
        res_ = requests.request("GET",suppliers_url, headers=headers, data=payload)
        supp_object = res_.json()
        # print(supp_object)
            
            
        for data in supp_object['data']:
            supplier_list = data
            # print(product_list)
    
            """
            Loop Through data list and pass neccessary Info
            """
            
            for list in supplier_list:
                cur.execute('SELECT * from "Suppliers" where "Id" = %s',[data['id']])
                supplier = cur.fetchall()
                if len(supplier) == 0:
                    print(data['name']) 
                    cur.execute('Insert Into "Suppliers" ("Name","Contact_Phone","Contact_Name","Address","Remarks","Created_At","Updated_At") values (%s,%s,%s,%s,%s,%s,%s)',([data['name'],data['contact_phone'],data['contact_name'],data['address'],data['remarks'],data['createdAt'],data['updatedAt']]))
                    print("Added to Ports " + data['name'])
                
                conn.commit()
                # print(list['name'])
                        
            # close the communication with the PostgreSQL
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        print('Database connection closed.')
save_suppliers()