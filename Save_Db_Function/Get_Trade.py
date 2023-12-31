import json
import requests
from pprint import pprint
import psycopg2
import datetime


def save_trade():
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
        # Pull data from Trade APIs
        payload = {}
        headers = { 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6ImFkdW5haml5ZUBnbWFpbC5jb20iLCJzdWIiOjMsImlhdCI6MTcwNDAxMTE5OSwiZXhwIjoxNzA2NjAzMTk5fQ.02RS6sqOLk8-cpZXmQeqF6fnojcXBnpTh92Rb4BpE9A'}
        trade_url = "https://vm-backend-ane5.onrender.com/trade"
        res_ = requests.request("GET",trade_url, headers=headers, data=payload)
        trade_object = res_.json()
        # print(trade_object)
            
            
        for data in trade_object['data']:
            trade_list = data
            # print(trade_list)
    
            """
            Loop Through data list and pass neccessary Info
            """
            
            for list in trade_list:
                cur.execute('SELECT * from "Trade" where "Id" = %s',[data['id']])
                trd = cur.fetchall()
                if len(trd) == 0:
                    print(data['tradeId'])
                    # ...
                    cur.execute('INSERT INTO "Trade" ("Start_Date", "End_Date", "Status", "Quantity", "Quantity_Sourced", "Quantity_Loaded", "Price_Per_Ton", "Trade_Currency", "Trade_Cost_Per_Ton", "Trade_Window", "Total_Product_Sales", "Trade_Balance", "Trade_Deposit", "Cureent_Trade_Profit", "Estimatted_Trade_Profit", "Customer_Name", "Customer_Location","Trade_Id") VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)',
                                (data['startDate'], data['endDate'], str(data['status']), data['quantity'], data['quantitySourced'], data['quantityLoaded'], data['financials']['pricePerTon'], str(data['financials']['currency']), data['financials']['tradeCostPerTon'], data['financials']['tradeWindow'], data['financials']['totalProductSales'], data['financials']['tradeBalance'], data['financials']['tradeDeposit'], data['financials']['currentTradeProfit'], data['financials']['estimatedTradeProfit'], str(data['customerName']), str(data['destinationPort']['location']),data['tradeId']))
                    conn.commit()
                    # print("Added to Trade " +data['customerName'])
   
            # close the communication with the PostgreSQL
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        print('Database connection closed.')
save_trade()