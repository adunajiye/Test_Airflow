import json
import requests
from pprint import pprint
import psycopg2
import datetime


def save_ports():
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
        port_object = requests.get("http://159.65.21.91:3000/port")
        port_object = port_object.json()
        print(port_object)
            
            
        for data in port_object['data']:
            port_list = data
            # print(port_list)
    
            """
            Loop Through data list and pass neccessary Info
            """
            for list in port_list:
                cur.execute('SELECT * from "Ports" where "Id" = %s',[data['id']])
                ports = cur.fetchall()
                if len(ports) == 0:
                    print(data['name']) 
                    cur.execute('Insert Into "Ports" ("Name", "Location","Created_At","Updated_At") values (%s,%s,%s,%s)',([data['name'],str(data['location']),data['createdAt'],data['updatedAt']]))
                    print("Added to Ports " + data['name'])
                
                conn.commit()    
            # close the communication with the PostgreSQL
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    
        print('Database connection closed.')
save_ports()