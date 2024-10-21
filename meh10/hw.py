import sqlite3

conn = sqlite3.connect('not_telegram.db')
cursor = conn.cursor()

cursor.execute('DELETE FROM Users WHERE id = ?', (6,))

cursor.execute('SELECT COUNT(*) FROM Users')
total_users = cursor.fetchone()[0]
print(f"Общее количество записей: {total_users}")

cursor.execute('SELECT SUM(balance) FROM Users')
total_balance = cursor.fetchone()[0]

if total_users > 0:
    average_balance = total_balance / total_users
else:
    average_balance = 0

print(f"Средний баланс всех пользователей: {average_balance}")

conn.commit()
conn.close()
