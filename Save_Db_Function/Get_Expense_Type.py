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
        payload = {}
        headers = { 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6ImFkdW5haml5ZUBnbWFpbC5jb20iLCJzdWIiOjMsImlhdCI6MTcwNDAxMTE5OSwiZXhwIjoxNzA2NjAzMTk5fQ.02RS6sqOLk8-cpZXmQeqF6fnojcXBnpTh92Rb4BpE9A'}
        expense_type_url = "https://vm-backend-ane5.onrender.com/expense-type"
        res_ = requests.request("GET",expense_type_url, headers=headers, data=payload)
        expense_object = res_.json()
        # print(expense_object)
            
            
        for data in expense_object['data']:
            expense_list = data
            # print(expense_list)
    
            """
            Loop Through data list and pass neccessary Info
            """
            
            for list in expense_list:
                cur.execute('SELECT * from "Expenses_Type" where "Id" = %s',[data['id']])
                prod = cur.fetchall()
                if len(prod) == 0:
                    # print(data['name'])
                    cur.execute('Insert Into "Expenses_Type" ("Name","Created_At","Updated_At") values (%s,%s,%s)',([data['name'],data['createdAt'],data['updatedAt']]))
                    conn.commit()
                    print("Added to Expense_Type_db " +data['name'])
                      
            # close the communication with the PostgreSQL
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        print('Database connection closed.')
save_expensetype()