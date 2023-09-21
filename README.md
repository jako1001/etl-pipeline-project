# ETL Pipeline Project

This project is a simple script that automates the Extract, Transform, Load (ETL) proccess.
This script can read user data from strucutured .CSV files with headers and unstructured .txt files
that contain phone numbers and emails. Once the data has been read it will be transformed into a
DataFrame and inserted into a MySQL database automatically.

### Technologies Used:

- Python
- Docker
- MySQL

### Currently Supports:

- Structured .csv Files (with headers)
- Unstructured .txt files containing phone numbers and emails

### How to use this script

Using this script is simple.

1. Clone the repository
2. Place the file you want to read in the "app/external_data" directory. Two test files are included there already
3. While in the top level directory run the command `make run file=your_file_name table=your_table_name`. Don't forget
   the file extenstion for the file name
4. Run `docker-compose down` whenever you are done running the script

### What's this doing?

Inside the makefile you can see the command `docker-compose run app ./wait-for-it.sh mysql:3306 -- python3 script.py ${file} ${table}`

`docker-compose run app ./wait-for-it.sh mysql:3306`: This portion runs docker and the wait-for-it
shell command to wait for the database to be initialized on port 3306

(Big thanks to GitHub user vishnubob for the database awaiting script. You can find the file here: [wait-for-it](https://github.com/vishnubob/wait-for-it))

`-- python3 script.py`: After the database is ready, run the python script file

`${file}`: User inputted file name and extenstion of the file in the app/external_data directory

`${table}`: User inputted table name for the table you want to create in the MySQL database

### For tests

1. Run `docker-compose up -d`
2. Run `pytest`
