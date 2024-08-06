import subprocess

# Path to your SQLite executable
sqlite_executable = '/home/syed0011/Timestamp/sqlite3.exe'

# Function to execute SQL commands
def execute_sql_command(sql_command):
    with subprocess.Popen([sqlite_executable, 'test.db'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True) as proc:
        proc.stdin.write(sql_command)
        proc.stdin.close()

# Create table1
execute_sql_command('''
    CREATE TABLE table1 (
        id INTEGER PRIMARY KEY,
        name TEXT,
        age INTEGER
    );
''')

# Create table2
execute_sql_command('''
    CREATE TABLE table2 (
        id INTEGER PRIMARY KEY,
        address TEXT,
        phone TEXT
    );
''')

# Insert 10000 records into table1
for i in range(1, 10001):
    name = f'Name{i}'
    age = i % 100
    execute_sql_command(f"INSERT INTO table1 (name, age) VALUES ('{name}', {age});")

# Insert 10000 records into table2
for i in range(1, 10001):
    address = f'Address{i}'
    phone = f'Phone{i}'
    execute_sql_command(f"INSERT INTO table2 (address, phone) VALUES ('{address}', '{phone}');")
