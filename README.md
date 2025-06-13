# Database-dump-tool-for-mac

Steps to build the app on your local machine.

### Pre-requisite
1. Python must be installed on your machine.
2. Postgres and pg_dump should be installed. Please set the required environment variables.
3. MySql and mysqldump should be installed. Please set the required environment variables.

### Step to install the App.
1. Clone the repo.
```
https://github.com/suraj-nova/Database-dump-tool-for-mac
```
2. Create a virtual env (Optional)
```
python3 -m venv .venv
```
3. Execute the below command.
```
pip install -r requirements.txt

pyinstaller --windowed --onefile db_dump_tool.py
```
4. This will create a dist folder in your current location.
5. Go to dist folder and double click on the db_dump_tool.app
6. This will Open the app on your screen.
7. Provide the details and Voila!! You will see the dump file generated at the provided location.