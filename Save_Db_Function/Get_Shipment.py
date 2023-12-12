import json
import requests
from pprint import pprint
import psycopg2
import datetime


def save_shipments():
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
        ship_op_object_poly = requests.get("https://vm-backend-ane5.onrender.com/shipment?company=Polyforte")
        ship_op_object_poly = ship_op_object_poly.json()
        print(ship_op_object_poly)
        
        ship_op_object_safari = requests.get("https://vm-backend-ane5.onrender.com/shipment?company=Safari Polymers")
        ship_op_object_safari = ship_op_object_safari.json()
        print(ship_op_object_safari)

        for data in ship_op_object_safari['data']:
            ship_op_list_safari = data
            # print(port_list)
            
        for data in ship_op_object_poly['data']:
            sort_op_list_poly = data
            # print(port_list)
    
            """
            Loop Through data list and pass neccessary Info
            """
            for list in data:
                cur.execute('SELECT * from "Shipment" where "Id" = %s',[data['id']])
                ship_op_safari = cur.fetchall()
                if len(ship_op_safari) == 0:
                    print(data['subShipments']['id']) 
                    cur.execute('Insert Into "Shipment" ("Shipment_Id","Date","Company_Name","Product_Type","Product_Quantity", "Created_At","Updated_At","SubShipment_Id") values (%s,%s,%s,%s,%s,%s,%s,%s)',([data['shipmentId'],data['date'],data['company'],data['productType'],data['productQuantity'],data['updatedAt'],data['subShipments']['id']]))
                    print("Added Safari to Shipment " + data['name'])
                    
            for list in data:
                cur.execute('SELECT * from "Shipment" where "Id" = %s',[data['id']])
                ship_op = cur.fetchall()
                if len(ship_op) == 0:
                    print(data['subShipments']['id']) 
                    cur.execute('Insert Into "Shipment" ("Shipment_Id","Date","Company_Name","Product_Type","Product_Quantity", "Created_At","Updated_At","SubShipment_Id") values (%s,%s,%s,%s,%s,%s,%s,%s)',([data['shipmentId'],data['date'],data['company'],data['productType'],data['productQuantity'],data['updatedAt'],data['subShipments']['id']]))
                    print("Added Safari to Shipment " + data['name'])
            
            conn.commit()    
            # close the communication with the PostgreSQL
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')
save_shipments()