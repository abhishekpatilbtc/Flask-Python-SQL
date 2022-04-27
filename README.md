# Flask-Python-SQL
# README FOR REST API service with Python

1. Overview

   The REST API service has been developed using Python3, Flask and SQLite3. It allows for easy install and speedy flexible development using python. 
   SQLite has been used as datastore for data imported using CSV as large as 2GB. All REST services are in app.py
   REST API calls will return JSON. 
   
   Server URL: The server will be locally hosted at http://127.0.0.1:5000

2. Resources used

   a) Python 3.6.10
   b) Flask 2.0.3
   c) SQLite 3.31.1
   
3. Files:
   a) app.py - It contains APIs
        i. Outputs all operators associated with given company - api/company/operators?companyName=
        ii. Outputs all companies associated with given operator - api/operator/companies?operatorName=
        iii. Outputs all companies connected to given company via shared operators - api/company/companies?companyOperator=
   b) dataHandler.py - It reads csv file, creates SQLite database and schema
   c) database.db (Created Later) - This will contain all the data imported from CSV
   d) requirement.txt - It contains information on libraries and their version

4. How to run application?

   a) Create datastore using CSV by running command in the root folder using terminal ==> python dataHandler.py <filename.csv>

   b) Ensure dependencies are installed. Refer to supported versions in requirements.txt
   
   c) Using terminal, start  web server by running command in the root folder using terminal  ==> python -m flask run
  

      
5. Design Discussions
    a.) Why Python Flask?
          Below are pros to consider Flask for such projects:
            i.) Flask allowed to create Web server which where we can host backend REST API server. Documentation, community support and developer tools
            ii.) The Flask is simple, enables faster deployment and has other integrations as well.
            iii.) Flask is actively maintained and developed
            iv.) Scalability, Simplicity and useful Python libraries
    b.) Why SQLite?
            i.)  With SQLite we can store large sized csv locally with easy.
            ii.) Generally speaking, 100K hits/day should work fine with SQLite. 
            iii.) SQLite can change files into smaller size archives with lesser metadata.
            iv.) We dockertized it if need to be migrated to cloud which will allow us to scale our Micro-service
