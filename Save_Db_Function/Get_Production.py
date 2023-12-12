import json
import requests
from pprint import pprint
import psycopg2
import datetime


def save_production():
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
        Production_object = requests.get("https://vm-backend-ane5.onrender.com/production")
        Production_object  = Production_object .json()
        print(Production_object)
            
            
        for data in Production_object['data']:
            production_list = data
            # print(port_list)
    
            """
            Loop Through data list and pass neccessary Info
            """
            for list in production_list:
                cur.execute('SELECT * from "Production" where "Id" = %s',[data['id']])
                sorts = cur.fetchall()
                if len(sorts) == 0:
                    print(data['name']) 
                    cur.execute('Insert Into "Production" ("Production_Id", "Date","Product_Type","Quantiy_Before_Prod","Quantiy_After_Prod","Created_At","Updated_At","Comments","Production_Type") values (%s,%s,%s,%s,%s,%s,%s,%s,%s)',([data['productionId'],data['date'],data['productType'],data['quantityBeforeProduction'],data['quantityAfterProduction'],data['createdAt'],data['updatedAt'],data['comments']['comment'],data['comments']['type']]))
                    print("Added to Production " + data['productionId'])
            conn.commit()    
            # close the communication with the PostgreSQL
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        print('Database connection closed.')
save_production()