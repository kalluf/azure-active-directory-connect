
library(RODBC)
library(httr)
#credentials
User 	<- 'your.name@yourcompany.com'                          	
Password <- 'passw0rd'                                           
#Azure SQL Server
Server   <- 'myserver.azuresynapse.net'  
Database <- 'databank'                                 	
Driver   <- 'ODBC Driver 17 for SQL Server'                  	
Password <- URLencode(password)

# Connection string
conn_string <- paste0("Driver={ODBC Driver 17 for SQL Server};Server=tcp:", Server, ";Database=", Database, ";Uid=", User, ";Pwd=", Password, ";Encrypt=yes;TrustServerCertificate=no;Authentication=ActiveDirectoryPassword;PORT=1433;")
conn <- odbcDriverConnect(conn_string)


result <- sqlQuery(conn,"SELECT * FROM SALES_TBL; ")

#Close odbc Connection
odbcClose(conn)  



