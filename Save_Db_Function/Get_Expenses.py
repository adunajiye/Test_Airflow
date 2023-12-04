import json
import requests
from pprint import pprint
import psycopg2
import datetime


def save_expensetype():
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
        expense_object = requests.get("http://159.65.21.91:3000/expense")
        expense_object = expense_object.json()
        print(expense_object)
            
            
        # for data in expense_object['data']:
        #     expense_list = data
        #     # print(product_list)
    
        #     """
        #     Loop Through data list and pass neccessary Info
        #     """
            
        #     for list in expense_list:
        #         cur.execute('SELECT * from "Expenses_Type" where "Id" = %s',[data['id']])
        #         prod = cur.fetchall()
        #         if len(prod) == 0:
        #             print(data['name']) 
        #             cur.execute('Insert Into "Expenses_Type" ("Name","Created_At","Updated_At") values (%s,%s,%s)',([data['name'],data['createdAt'],data['updatedAt']]))
        #             conn.commit()
                # print(list['name'])
                
                
                
                        
            # close the communication with the PostgreSQL
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')
save_expensetype()