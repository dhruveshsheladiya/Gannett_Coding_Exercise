# Gannett_Coding_Exercise
Readme {API}- PART-1

I have designed my API in Flask-Python framework and used SQLite Database.

Installation Instruction:

1. First of All we need Python installed in our machine 2.7 or higher or 3.6 or higher.

2. Make sure We have Installed pip for our Python. PIP is package management system in python

3. you can check if pip installed in your machine by "pip --version" command. if machine doesn't recognize pip then check environmental path variable or check your Python version

4. Now clone the submitted git-repository or Download the zip file and unzip it to one directory.

5. Using cmd or Terminal go to that Directory and type ls. you will see multiple files like produce.db, app.py etc.

6. Now we need to create basic virtual environment for Python2.7 and install the packages after it's activation.

7. Give command "virtualenv venv"

8. Give command "source venv/bin/activate" this command will run for Unix or MacOS. For windows you need to run activate.bat to activate virtual environment.

9. Give Command "pip install flask flask-jsonpify flask-sqlalchemy flask-restful"

10. Give command "pip freeze"

11. Now we need to connect to the Database. you can connect by "sqlite3 produce.db". If you don't have SQLite installed then Download Sqlite Precompiled binaries from http://www.sqlite.org/download.html

12. Now we are all set to run Our API

13. run API by "Python app.py". You will see message that Server running on 127.0.0.1:8000

14. on "127.0.0.1:8000" you can access API and get the Elements from Database
	E.g. "127.0.0.1:8000/produceInventory" you can access Entire Table of Product Inventory
	E.g. "127.0.0.1:8000/produceInventory/A12T-4GH7-QPL9-3N4M" will show you product detail whose id is A12T-4GH7-QPL9-3N4M
	
15. This API won't support POST, PUT and DELETE method because we have assigned to implement GET method
