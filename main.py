import mysql.connector

# Replace these values with your MySQL server information
host = "127.0.0.1"
user = "root"
password = "nensi"
database = "adbms"
import csv

# try:
#     # Create a connection to the MySQL server
#     connection = mysql.connector.connect(
#         host=host,
#         user=user,
#         password=password,
#         database=database
#     )

#     if connection.is_connected():
#         print("Connected to MySQL database")

#         # Create a cursor object to interact with the database
#         cursor = connection.cursor()

#         # Open and read the CSV file
#         with open('train_file.csv', 'r') as file:
#             csv_reader = csv.reader(file)
#             next(csv_reader)  # Skip the header row if it exists

#             # Iterate through each row in the CSV and insert into the table
#             for row in csv_reader:
#                 insert_query = """
#                     INSERT INTO business_license (
#                         ID, LICENSE_ID, ACCOUNT_NUMBER, SITE_NUMBER,
#                         LEGAL_NAME, DOING_BUSINESS_AS_NAME, ADDRESS,
#                         CITY, STATE, ZIP_CODE, WARD, PRECINCT,
#                         WARD_PRECINCT, POLICE_DISTRICT, LICENSE_CODE,
#                         LICENSE_DESCRIPTION, LICENSE_NUMBER, APPLICATION_TYPE,
#                         APPLICATION_CREATED_DATE, APPLICATION_REQUIREMENTS_COMPLETE,
#                         PAYMENT_DATE, CONDITIONAL_APPROVAL, LICENSE_TERM_START_DATE,
#                         LICENSE_TERM_EXPIRATION_DATE, LICENSE_APPROVED_FOR_ISSUANCE,
#                         DATE_ISSUED, LICENSE_STATUS_CHANGE_DATE, SSA,
#                         LATITUDE, LONGITUDE, LOCATION, LICENSE_STATUS
#                     ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
#                 """

#         # Commit the changes and close the cursor
#         connection.commit()
#         cursor.close()

# except mysql.connector.Error as error:
#     print(f"Error: {error}")
# finally:
#     # Close the connection
#     if 'connection' in locals() and connection.is_connected():
#         connection.close()
#         print("MySQL connection is closed")

# # Data to insert
# data_to_insert = [
#     ("35342-20020816", 1256593, 32811, 1),
#     ("1358463-20051116", 1639294, 262311, 29)
# ]

# try:
#     # Create a connection to the MySQL server
#     connection = mysql.connector.connect(
#         host=host,
#         user=user,
#         password=password,
#         database=database
#     )

#     if connection.is_connected():
#         print("Connected to MySQL database")

#         # Create a cursor object to interact with the database
#         cursor = connection.cursor()

#         # Define the SQL INSERT statement using backticks for column names with spaces or special characters
#         insert_query = "INSERT INTO business_license_main (ID, `LICENSE ID`, `ACCOUNT NUMBER`, `SITE NUMBER`) VALUES (%s, %s, %s, %s)"

#         # Execute the INSERT statement for each data row
#         for row in data_to_insert:
#             cursor.execute(insert_query, row)

#         # Commit the changes to the database
#         connection.commit()
#         print("Data inserted successfully")

# except mysql.connector.Error as error:
#     print(f"Error: {error}")
# finally:
#     # Close the cursor and connection
#     if 'cursor' in locals():
#         cursor.close()
#     if 'connection' in locals() and connection.is_connected():
#         connection.close()
#         print("MySQL connection is closed")




csv_file = "filtered_output_file.csv"

try:
    # Create a connection to the MySQL server
    connection = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )

    if connection.is_connected():
        print("Connected to MySQL database")

        # Create a cursor object to interact with the database
        cursor = connection.cursor()

        # Open and read the CSV file
        with open(csv_file, 'r', newline='') as file:
            csv_reader = csv.reader(file)
            next(csv_reader)  # Skip the header row if it exists

            # Define the SQL INSERT statement
            insert_query = """
                INSERT INTO business_license_main (ID, `LICENSE ID`, `ACCOUNT NUMBER`, `SITE NUMBER`)
                VALUES (%s, %s, %s, %s)
            """

            # Iterate through each row in the CSV and insert into the database
            for row in csv_reader:
                cursor.execute(insert_query, row)

            # Commit the changes to the database
            connection.commit()
            print("Data inserted successfully")

except mysql.connector.Error as error:
    print(f"Error: {error}")
finally:
    # Close the cursor and connection
    if 'cursor' in locals():
        cursor.close()
    if 'connection' in locals() and connection.is_connected():
        connection.close()
        print("MySQL connection is closed")