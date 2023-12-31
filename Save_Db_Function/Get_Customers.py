import json
import requests
from pprint import pprint
import psycopg2
import datetime
# from Save_Db_Function.Login import Login


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
        
        # Pull data from Customers
        # session_id = Login()
        payload = {}
        headers = { 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6ImFkdW5haml5ZUBnbWFpbC5jb20iLCJzdWIiOjMsImlhdCI6MTcwNDAxMTE5OSwiZXhwIjoxNzA2NjAzMTk5fQ.02RS6sqOLk8-cpZXmQeqF6fnojcXBnpTh92Rb4BpE9A'}
        customer_url = "https://vm-backend-ane5.onrender.com/customer"
        res_ = requests.request("GET",customer_url, headers=headers, data=payload)
        res_object = res_.json()
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
        print('Database connection closed.')
save_customers()