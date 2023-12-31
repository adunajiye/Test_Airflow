import json
import requests
from pprint import pprint
import psycopg2
import datetime


def save_sorts_summary():
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
        # Pull data from Sortings
        payload = {}
        headers = { 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6ImFkdW5haml5ZUBnbWFpbC5jb20iLCJzdWIiOjMsImlhdCI6MTcwNDAxMTE5OSwiZXhwIjoxNzA2NjAzMTk5fQ.02RS6sqOLk8-cpZXmQeqF6fnojcXBnpTh92Rb4BpE9A'}
        sorting_url = "https://vm-backend-ane5.onrender.com/sorting"
        res_ = requests.request("GET",sorting_url, headers=headers, data=payload)
        sort_object = res_.json()
        # print(sort_object)
            
            
        for data in sort_object['data']:
            sort_list = data
            # print(port_list)
    
            """
            Loop Through data list and pass neccessary Info
            """
            for list in sort_list:
                cur.execute('SELECT * from "Summary_Sortings" where "Id" = %s',[data['id']])
                sorts = cur.fetchall()
                if len(sorts) == 0:
                    print(data['name']) 
                    cur.execute('Insert Into "Summary_Sortings" ("Quantity_Sourced", "Amount_Paid","Amount_Paid_USD","Company_Name","Created_At","Updated_At","Sorters_Quanity_Sorted") values (%s,%s,%s,%s,%s,%s)',([data['quantitySorted'],data['amountPaid'],data['amountPaidInUsd'],data['company'],data['createdAt'],data['updatedAt']]))
                    print("Added to Summary_Sortings " + data['name'])
                
            conn.commit()    
            # close the communication with the PostgreSQL
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        print('Database connection closed.')
save_sorts_summary()