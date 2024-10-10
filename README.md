# pythonSQLite-REST_101
How to begin creating small applications with python that integrates with both REST API and SQLite


### TO Begin you probably want to add imports:
```txt
from flask import Flask, render_template, request, redirect
import sqlite3
```
>[!Warning]
Make sure you have these SQLite and Flask installed in your project in order to start doing this
If you are not sure you have flask in your project , go to your project structure or packages and see if you have flask and all its dependencies.

## APP.py
Your configuration in your app.py is very important. It will change depending on your controllers and what you want to call your DB


>[!Note]
Make sure you add this in the top of your file:  ```app = Flask(__name__)```


### Connecting to a Database

If having trouble connectiong to your SQLite database go to the following file in the repository: **dbConnecter.py**




## Working on the Front-End
When working on the front-end it is okay to build in in vs code. It is almost recommended that you do this so your code is much cleaner. 

## Running the Project

All you need to run the project is to run the following command:
```txt
python <file-name>.py
# for example if you script is called main.py your command would be:
python main.py
```
You will then obtain a link that you may click to see your front-end


