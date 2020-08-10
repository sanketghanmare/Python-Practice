import sqlite3

db = sqlite3.connect("contacts.sqlite")

email = "newupdate@update.com"
# phone = 1234

# you can enter the sql injection attack here
# for example: enter number like this along with other drop statement
# 1234;drop table contacts (sample input statement)
phone = input("Please enter the phone number")

# update_sql = f"UPDATE contacts SET email = '{email}' where phone = '{phone}'"
update_sql = " UPDATE contacts SET email = ? where phone = ? "

print(update_sql)


update_cursor = db.cursor()

# statement to execute multiple sql statement
# update_cursor.executescript(update_sql)

update_cursor.execute(update_sql, (email, phone))
print(f"{update_cursor.rowcount} rows update")


print()
print(f"Are connections the same: {update_cursor.connection == db}")
print()

update_cursor.connection.commit()
update_cursor.close()

for name, phone, email in db.execute("SELECT * FROM contacts"):
    print(name)
    print(phone)
    print(email)
    print('-' * 20)
db.close()
