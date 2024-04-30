import psycopg2
import csv

# Function to connect to the PostgreSQL database
def connect_to_db():
    try:
        conn = psycopg2.connect(
            dbname="postgres",
            user="postgres",
            password="1234",
            host="127.0.0.1",
            port="5432"
        )
        return conn
    except psycopg2.Error as e:
        print("Unable to connect to the database:", e)

# Function to create the phonebook table if it doesn't exist
def create_table_if_not_exists(conn):
    try:
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS phonebook (
                id SERIAL PRIMARY KEY,
                name VARCHAR(100),
                phone VARCHAR(20)
            )
        """)
        conn.commit()
        cur.close()
    except psycopg2.Error as e:
        print("Error creating table:", e)

# Function to add a contact to the phone book
def add_contact(conn, name, phone):
    try:
        cur = conn.cursor()
        cur.execute("INSERT INTO phonebook (name, phone) VALUES (%s, %s)", (name, phone))
        conn.commit()
        print("Contact added successfully.")
        cur.close()
    except psycopg2.Error as e:
        print("Error adding contact:", e)

# Function to delete a contact by phone number
def delete_contact(conn, phone):
    try:
        cur = conn.cursor()
        cur.execute("DELETE FROM phonebook WHERE phone = %s", (phone,))
        conn.commit()
        if cur.rowcount > 0:
            print("Contact deleted successfully.")
        else:
            print("Contact not found.")
        cur.close()
    except psycopg2.Error as e:
        print("Error deleting contact:", e)

# Function to update a contact's name
def update_contact_name(conn, phone, new_name):
    try:
        cur = conn.cursor()
        cur.execute("UPDATE phonebook SET name = %s WHERE phone = %s", (new_name, phone))
        conn.commit()
        if cur.rowcount > 0:
            print("Contact name updated successfully.")
        else:
            print("Contact not found.")
        cur.close()
    except psycopg2.Error as e:
        print("Error updating contact name:", e)

# Function to update a contact's phone number
def update_contact_phone(conn, old_phone, new_phone):
    try:
        cur = conn.cursor()
        cur.execute("UPDATE phonebook SET phone = %s WHERE phone = %s", (new_phone, old_phone))
        conn.commit()
        if cur.rowcount > 0:
            print("Contact phone number updated successfully.")
        else:
            print("Contact not found.")
        cur.close()
    except psycopg2.Error as e:
        print("Error updating contact phone number:", e)

# Function to display all contacts in the phone book
def display_contacts(conn):
    try:
        cur = conn.cursor()
        cur.execute("SELECT * FROM phonebook")
        contacts = cur.fetchall()
        if not contacts:
            print("Phone book is empty.")
        else:
            print("Phone book contacts:")
            for contact in contacts:
                print(f"Name: {contact[1]}, Phone: {contact[2]}")
        cur.close()
    except psycopg2.Error as e:
        print("Error displaying contacts:", e)

# Function to import contacts from a CSV file
def import_contacts_from_csv(conn, csv_file):
    try:
        with open(csv_file, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header
            for row in reader:
                name, phone = row
                add_contact(conn, name, phone)
    except FileNotFoundError:
        print("CSV file not found.")
    except Exception as e:
        print("Error importing contacts from CSV:", e)

# Main function to interact with the phone book
def main():
    conn = connect_to_db()
    if conn:
        create_table_if_not_exists(conn)
        while True:
            print("\nPhone Book Menu:")
            print("1. Add Contact")
            print("2. Delete Contact")
            print("3. Update Contact Name")
            print("4. Update Contact Phone Number")
            print("5. Display Contacts")
            print("6. Import Contacts from CSV")
            print("7. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                name = input("Enter name: ")
                phone = input("Enter phone number: ")
                add_contact(conn, name, phone)
            elif choice == "2":
                phone = input("Enter phone number to delete: ")
                delete_contact(conn, phone)
            elif choice == "3":
                phone = input("Enter phone number to update name: ")
                new_name = input("Enter new name: ")
                try:
                    cur = conn.cursor()
                    cur.execute("UPDATE phonebook SET name = %s WHERE phone = %s", (new_name, phone))
                    conn.commit()  # Commit the changes to the database
                    if cur.rowcount > 0:
                        print("Contact name updated successfully.")
                    else:
                        print("Contact not found.")
                    cur.close()
                except psycopg2.Error as e:
                    print("Error updating contact name:", e)
            elif choice == "4":
                phone = input("Enter phone number to update: ")
                new_phone = input("Enter new phone number: ")
                try:
                    cur = conn.cursor()
                    cur.execute("UPDATE phonebook SET phone = %s WHERE phone = %s", (new_phone, phone))
                    conn.commit()  # Commit the changes to the database
                    if cur.rowcount > 0:
                        print("Contact phone number updated successfully.")
                    else:
                        print("Contact not found.")
                    cur.close()
                except psycopg2.Error as e:
                    print("Error updating contact phone number:", e)
            elif choice == "5":
                display_contacts(conn)
            elif choice == "6":
                csv_file = input("Enter the CSV file path: ")
                import_contacts_from_csv(conn, csv_file)
            elif choice == "7":
                break
            else:
                print("Invalid choice. Please try again.")

        conn.close()

# Call the main function directly
main()