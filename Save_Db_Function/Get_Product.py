import json
import requests
from pprint import pprint
import psycopg2
import datetime


def save_products():
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
        prod_object = requests.get("http://159.65.21.91:3000/product")
        prod_object = prod_object.json()
        print(prod_object)
            
            
        for data in prod_object['data']:
            product_list = data
            # print(product_list)
    
            """
            Loop Through data list and pass neccessary Info
            """
            
            for list in product_list:
                cur.execute('SELECT * from "Products" where "Id" = %s',[data['id']])
                prod = cur.fetchall()
                if len(prod) == 0:
                    print(data['name']) 
                    cur.execute('Insert Into "Products" ("Name","Product_Id","Created_At","Updated_At") values (%s,%s,%s,%s)',([data['name'],data['productId'],data['createdAt'],data['updatedAt']]))
                    print("Added to Products " +data['name'])
                    
                conn.commit()                        
            # close the communication with the PostgreSQL
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    
        print('Database connection closed.')
save_products()