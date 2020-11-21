import psycopg2

# establish db connection
connection = psycopg2.connect('postgres://uncaught:@localhost:5432/demo')

# get a reference
cursor = connection.cursor()

# excute a query
cursor.execute('select * from stuff')

# get results
records = cursor.fetchall()
for record in records:
  print(record)