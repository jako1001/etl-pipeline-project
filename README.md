# ETL Pipeline Project

This project is a simple script that follows the Extract, Transform, Load (ETL) proccess.
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
2. Place the file you want to read in the "app/external_data" directory. Two test files are included there already.
3. Run `docker-compose build` while in the main directory
4. Once it is finished building, run `docker-compose run app ./wait-for-it.sh mysql:3306 -- python3 script.py your_file_name your_table_name`

What's this doing?

`docker-compose run app ./wait-for-it.sh mysql:3306`: This portion runs the and executes the wait-for-it
shell command to wait for the database to be initialized on port 3306.
(Big thanks to GitHub user vishnubob. You can find the command here: [wait-for-it](https://github.com/vishnubob/wait-for-it))

`-- python3 script.py`: After the database is ready, run the python script file

`your_file_name`: Change this to the name of your file in the "app/external_data" directory. Don't forget to include the file extension.

`your_table_name`: Change this to the name that you want the table to be called in the database.
