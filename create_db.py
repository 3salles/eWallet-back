import sqlite3

connection = sqlite3.connect('ewallet.db')
cursor = connection.cursor()

create_table = 'CREATE TABLE IF NOT EXISTS transactions (uid text PRIMARY KEY,\
category text, date text, amount real, description text, institution text)'

create_transaction_01 = "INSERT INTO transactions VALUES ('752d013d-4a7d-48c7-993c-87f8296757c8', 'entertainment', '2023-06-17', 300, 'Hogwarts Legacy', 'PS Store')"
create_transaction_02 = "INSERT INTO transactions VALUES ('008b2d8f-7bc3-4241-b156-1122574635e5', 'food', '2023-06-17', 300, 'Sanduíche', 'Swbway')"
create_transaction_03 = "INSERT INTO transactions VALUES ('e5b01419-e3ea-4998-9016-5bec1464a909', 'shopping', '2023-06-17', 300, 'Capa para celular', 'Shopping')"
create_transaction_04 = "INSERT INTO transactions VALUES ('33f0d30f-d117-40e7-ac04-46b56165abd6', 'income', '2023-06-17', 4567.23, 'Salário', NULL)"
create_transaction_05 = "INSERT INTO transactions VALUES ('908e8857-9d3e-4da8-a2e2-c6eb38948b0c', 'transportation', '2023-06-17', 26.12, 'Uber', 'Uber')"
create_transaction_06 = "INSERT INTO transactions VALUES ('fdc055aa-2c8b-4ea1-a4c1-5e0e88a39f6c', 'housing', '2023-06-17', 354.95, 'Conta de luz', 'Equatorial')"


cursor.execute(create_table)
cursor.execute(create_transaction_01)
cursor.execute(create_transaction_02)
cursor.execute(create_transaction_03)
cursor.execute(create_transaction_04)
cursor.execute(create_transaction_05)
cursor.execute(create_transaction_06)

connection.commit()
connection.close()