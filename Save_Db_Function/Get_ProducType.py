import json
import requests
from pprint import pprint
import psycopg2
import datetime


def save_productype():
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
        payload = {}
        headers = { 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6ImFkdW5haml5ZUBnbWFpbC5jb20iLCJzdWIiOjMsImlhdCI6MTcwNDAxMTE5OSwiZXhwIjoxNzA2NjAzMTk5fQ.02RS6sqOLk8-cpZXmQeqF6fnojcXBnpTh92Rb4BpE9A'}
        prodt_url = "https://vm-backend-ane5.onrender.com/product-type"
        res_ = requests.request("GET",prodt_url, headers=headers, data=payload)
        prodt_object = res_.json()
        # print(prodt_object)
            
            
        # for data in prodt_object['data']:
        #     product_type_list = data
        #     # print(product_type_list)
    
        #     """
        #     Loop Through data list and pass neccessary Info
        #     """
        #     for list in product_type_list:
        #         cur.execute('SELECT * from "Product_Type" where "Id" = %s',[data['id']])
        #         prodt = cur.fetchall()
        #         if len(prodt) == 0:
        #             print(data['name']) 
        #             cur.execute('Insert Into "Product_Type" ("Name","Created_At","Updated_At") values (%s,%s,%s)',([data['name'],data['createdAt'],data['updatedAt']]))
        #             conn.commit()
        #             print("Added to Products " +data['name'])
        #         # print(list['name'])
                    
        #     # close the communication with the PostgreSQL
        # cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        print('Database connection closed.')
save_productype()