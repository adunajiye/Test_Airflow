import json
import requests
from pprint import pprint
import psycopg2
import datetime


def save_subtrade():
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
        subtrade_object = requests.get("http://159.65.21.91:3000/sub-trade")
        subtrade_object = subtrade_object.json()
        # print(subtrade_object)
        """
         Loop Through data list and pass neccessary Info
        """
        for data in subtrade_object['data']:
            subtrade_List = data
            count = 1
           
            # Assuming data is a dictionary, not a list
            cur.execute('SELECT * from "SubTrade" where "Id" = %s', [data['id']])
            subt = cur.fetchall()
            for comments in data['comments']:
                print(comments['comment'])
                
            if len(subt) == 0:
                for expenses_item in data['expenses']:
                    print(expenses_item['amount'])
                    # print(expenses_item['amountInForeignCurrency'])
                    # print(expenses_item['remarks'])
                    cur.execute('Insert Into "SubTrade" ("Cost","Expenses_Amount","SourceTrading","Created_At","Updated_At","Remarks","Comments","ForeignCurrnecy","Quantity") values (%s,%s,%s,%s,%s,%s,%s,%s,%s)',
                                (data['cost'],expenses_item['amount'],data['sourcingStatus'],data['createdAt'],data['updatedAt'],expenses_item['remarks'],comments['comment'],expenses_item['amountInForeignCurrency'],data['quantity']))
                conn.commit()
                
            # close the communication with the PostgreSQL
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        print('Database connection closed.')
save_subtrade()