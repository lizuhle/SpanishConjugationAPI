import mysql.connector

def run_sql_script(filename, connection):
    with open(filename, 'r') as file:
        sql_script = file.read()

    cursor = connection.cursor()
    for statement in sql_script.split(';'):
        statement = statement.strip()
        if statement:
            cursor.execute(statement)
    connection.commit()
    cursor.close()

def main():
    config = {
        'user': 'liz',
        'password': 'Spanconj123!',
        'host': 'localhost',
        'port': '3306',
        'database': 'spanishconj'
    }
    connection = mysql.connector.connect(**config)
    run_sql_script('init.sql', connection)
    connection.close()

if __name__ == '__main__':
    main()
