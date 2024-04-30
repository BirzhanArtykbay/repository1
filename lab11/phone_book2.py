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
        cur.execute("SELECT COUNT(*) FROM phonebook WHERE name = %s", (name,))
        count = cur.fetchone()[0]
        if count > 0:
            cur.execute("UPDATE phonebook SET phone = %s WHERE name = %s", (phone, name))
        else:
            cur.execute("INSERT INTO phonebook (name, phone) VALUES (%s, %s)", (name, phone))
        conn.commit()
        print("User inserted/updated successfully.")
    except psycopg2.Error as e:
        print("Error adding/updating user:", e)

# Procedure to insert many new users and check correctness of phone numbers
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
def insert_many_users(conn, names, phones):
    try:
        cur = conn.cursor()
        invalid_data = []
        for name, phone in zip(names, phones):
            if len(phone) != 10:
                invalid_data.append((name, phone))
            else:
                cur.execute("INSERT INTO phonebook (name, phone) VALUES (%s, %s)", (name, phone))
        conn.commit()
        if invalid_data:
            print("Invalid phone numbers:", invalid_data)
        else:
            print("All users inserted successfully.")
    except psycopg2.Error as e:
        print("Error inserting users:", e)

# Function to search contacts based on a pattern
def search_contacts(conn, pattern):
    try:
        cur = conn.cursor()
        cur.execute("SELECT * FROM phonebook WHERE name ILIKE %s OR phone ILIKE %s", (f'%{pattern}%', f'%{pattern}%'))
        contacts = cur.fetchall()
        return contacts
    except psycopg2.Error as e:
        print("Error searching contacts:", e)
        return []

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

# Function for querying data with pagination
def get_contacts_with_pagination(conn, limit, offset):
    try:
        cur = conn.cursor()
        cur.execute("SELECT * FROM phonebook LIMIT %s OFFSET %s", (limit, offset))
        contacts = cur.fetchall()
        return contacts
    except psycopg2.Error as e:
        print("Error fetching contacts:", e)
        return []

# Procedure to delete data by username or phone
def delete_contact(conn, identifier):
    try:
        cur = conn.cursor()
        cur.execute("DELETE FROM phonebook WHERE name = %s OR phone = %s", (identifier, identifier))
        conn.commit()
        print("Contact(s) deleted successfully.")
    except psycopg2.Error as e:
        print("Error deleting contact(s):", e)

# Main function to interact with the phone book
def main():
    conn = connect_to_db()
    if conn:
        create_table_if_not_exists(conn)
        while True:
            print("\nPhone Book Menu:")
            print("1. Add Contact")
            print("2. Import Contacts from CSV")
            print("3. Search Contacts")
            print("4. Insert Many Users")
            print("5. Query Contacts with Pagination")
            print("6. Delete Contact")
            print("7. Display Contacts")
            print("8. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                name = input("Enter name: ")
                phone = input("Enter phone number: ")
                add_contact(conn, name, phone)
            elif choice == "2":
                csv_file = input("Enter the CSV file path: ")
                import_contacts_from_csv(conn, csv_file)
            elif choice == "3":
                pattern = input("Enter search pattern: ")
                matching_contacts = search_contacts(conn, pattern)
                print("Matching contacts:")
                for contact in matching_contacts:
                    print(contact)
            elif choice == "4":
                names = input("Enter names (comma-separated): ").split(',')
                phones = input("Enter phone numbers (comma-separated): ").split(',')
                insert_many_users(conn, names, phones)
            elif choice == "5":
                limit = int(input("Enter limit: "))
                offset = int(input("Enter offset: "))
                contacts = get_contacts_with_pagination(conn, limit, offset)
                print("Contacts with pagination:")
                for contact in contacts:
                    print(contact)
            elif choice == "6":
                identifier = input("Enter name or phone number to delete: ")
                delete_contact(conn, identifier)
            elif choice == "7":
                display_contacts(conn)
            elif choice == "8":
                break
            else:
                print("Invalid choice. Please try again.")

        conn.close()

# Call the main function directly
main()