
#Connect to Azure databases that require Authentication=ActiveDirectoryPassword using Python

import pyodbc
import pandas as pd
import matplotlib.pyplot as plt
 
#Credentials
username = 'name@yourcompany.com'
password = '{s3cr3t_pa22W0rd}' #use the curly bracket in case your password has special characters  
 
#Server,Database and Driver
server = 'myincredibleserver.azure.net'
database = 'databank'
#Make sure the driver is installed in your machine
driver= '{ODBC Driver 17 for SQL Server}'
 
conn = pyodbc.connect('DRIVER='+driver+';SERVER=tcp:'+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+password+';Authentication=ActiveDirectoryPassword')
 
#SQL Query place your SQL code between the triple quotation marks """
result = pd.read_sql("""SELECT * FROM SALES_TBL;""",conn)
 
#Insert Query into Pandas Dataframe, from this point you are in Pandas territory
df = pd.DataFrame(result)