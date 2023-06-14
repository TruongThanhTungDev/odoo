import psycopg2

def connect():
    ps_connection = psycopg2.connect(host="localhost",
                     database="acs_recruitment",
                     user="odoo",
                     password="hoa123456")
    return ps_connection
def insertCvTable(records):
    try:
        # Connect to database
        ps_connection = connect()
        # Create a new cursor object
        cursor = ps_connection.cursor()

        # Define the INSERT statement
        insert_query = "INSERT INTO recruitment (name, detail) VALUES (%s, %s)"

        # Execute the INSERT statement for each tuple in the list
        for record in records:
            cursor.execute(insert_query, record)

        # Commit the changes
        ps_connection.commit()

        print("Records Uploaded")


    except (Exception, psycopg2.Error) as error:
        print("Error while updating PostgreSQL table", error)

    finally:
        # closing database connection.
        if ps_connection:
            cursor.close()
            ps_connection.close()

def update(records):
    try:
        # Connect to database
        ps_connection = connect()
        cursor = ps_connection.cursor()

        # Update multiple records
        update_query = "UPDATE recruitment SET name = %s WHERE detail = %s"
        print(records)
        cursor.executemany(update_query, records)

        ps_connection.commit()

        print("Records Updated")

    except (Exception, psycopg2.Error) as error:
        print("Error while updating PostgreSQL table", error)

    finally:
        # closing database connection.
        if ps_connection:
            cursor.close()
            ps_connection.close()

def insertScoreTable(records):
    try:
        # Connect to database
        ps_connection = connect()
        # Create a new cursor object
        cursor = ps_connection.cursor()

        # Define the INSERT statement
        insert_query = "INSERT INTO score (name, point) VALUES (%s, %s)"

        # Execute the INSERT statement for each tuple in the list
        for record in records:
            cursor.execute(insert_query, record)

        # Commit the changes
        ps_connection.commit()

        print("Records Uploaded")


    except (Exception, psycopg2.Error) as error:
        print("Error while updating PostgreSQL table", error)

    finally:
        # closing database connection.
        if ps_connection:
            cursor.close()
            ps_connection.close()

def sortRecords(records):
    sorted_list = sorted(data, key=lambda x: x[1], reverse=True)
    return sorted_list



data = [("Le Huy", "111"), ("Truong Thanh Tung", "1111")]
# insertCvTable(data)
data_update = [("Khanh Hoa", "123"), ("Do Duy Dao", "24")]
update(data_update)
   # data_score = [("Le Huy", "20"), ("Truong Thanh Tung", "100")]
# insertScoreTable(data)