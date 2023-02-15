# azure-active-directory-connect
Information about connectiong to Azure/Synapse using Python and R
 
When establishing a connection to an Azure/Synapse database in Python or R, there are various authentication methods available, as documented in Microsoft's official list found at https://learn.microsoft.com/en-us/sql/connect/jdbc/connecting-using-azure-active-directory-authentication

This repository aims to provide guidance for connecting to an Azure SQL database in Python or R when utilizing the ActiveDirectoryPassword authentication method. In this context, the user's Azure Active Directory credentials are passed to the database connector, alongside the "authentication=ActiveDirectoryPassword" option, to enable secure authentication and access.

To establish the connection, the "pyodbc.connect()" method is employed with a connection string that specifies the necessary connection details, such as the database driver, server name, port, database name, username, password, and authentication type. The authentication type is an essential parameter that must be correctly defined to ensure successful connectivity to the Azure SQL database.
