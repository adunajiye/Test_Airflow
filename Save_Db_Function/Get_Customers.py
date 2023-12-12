import json
import requests
from pprint import pprint
import psycopg2
import datetime


def save_customers():
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
        res_object = requests.get("http://159.65.21.91:3000/customer")
        res_object = res_object.json()
        # print(res_object)
            
            
        for data in res_object['data']:
            customer_list = data
            # print(customer_list)
    
            """
            Loop Through data list and pass neccessary Info
            """
            for list in customer_list:
                cur.execute('SELECT * from "Customers" where "Id" = %s',[data['id']])
                customers = cur.fetchall()
                if len(customers) == 0:
                    print(data['name']) 
                    cur.execute('Insert Into "Customers" ("Name", "Location","Customer_Id","Contact_Information","Docs_Required","Created_at","Updated_at") values (%s,%s,%s,%s,%s,%s,%s)',([data['name'],str(data['location']),data['customerId'],data['contactInformation'],data['docsRequired'],data['createdAt'],data['updatedAt']]))
                    conn.commit()
                    
                
            
            # close the communication with the PostgreSQL
                    cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')
save_customers()