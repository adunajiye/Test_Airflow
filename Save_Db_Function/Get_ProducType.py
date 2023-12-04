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
        prodt_object = requests.get("http://159.65.21.91:3000/product-type")
        prodt_object = prodt_object.json()
        print(prodt_object)
            
            
        for data in prodt_object['data']:
            product_type_list = data
            # print(product_type_list)
    
            """
            Loop Through data list and pass neccessary Info
            """
            for list in product_type_list:
                cur.execute('SELECT * from "Product_Type" where "Id" = %s',[data['id']])
                prodt = cur.fetchall()
                if len(prodt) == 0:
                    print(data['name']) 
                    cur.execute('Insert Into "Product_Type" ("Name","Created_At","Updated_At") values (%s,%s,%s)',([data['name'],data['createdAt'],data['updatedAt']]))
                    conn.commit()
                    print("Added to Products " +data['name'])
                else:
                    len(prodt) == True
                print("Product_Type Exists")
                # print(list['name'])
                
                
                
                        
            # close the communication with the PostgreSQL
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')
save_productype()