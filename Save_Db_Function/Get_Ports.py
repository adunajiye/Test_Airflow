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
        # Pull data from Ports
        payload = {}
        headers = { 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6ImFkdW5haml5ZUBnbWFpbC5jb20iLCJzdWIiOjMsImlhdCI6MTcwNDAxMTE5OSwiZXhwIjoxNzA2NjAzMTk5fQ.02RS6sqOLk8-cpZXmQeqF6fnojcXBnpTh92Rb4BpE9A'}
        ports_url = "https://vm-backend-ane5.onrender.com/port"
        res_ = requests.request("GET",ports_url, headers=headers, data=payload)
        port_object = res_.json()
        # print(port_object)
            
            
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