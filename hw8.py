import sqlite3

connect = sqlite3.connect("bank.db")
cursor = connect.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS customs(id INTEGER PRIMARY KEY, name VARCHAR(100) NOT NULL, surname VARCHAR(100) NOT NULL,  
               age INTEGER NOT NULL, email TEXT, balance DOUBLE (8, 2), is_active BOOLEAN DEFAULT FALSE);""")

class Bank:
    def __init__(self):
        self.name = None
        self.surname = None
        self.age = 0
        self.email = None
        self.balance = 0
        self.is_active = False

    def register(self, name, surname, age, email,):
        self.name = name
        self.surname = surname
        self.age = age
        self.email = email

        cursor.execute(f"""INSERT INTO customs (name, surname, age, email, balance, is_active) 
                        VALUES('{name}', '{surname}','{age}','{email}', 0, True);""")
        connect.commit()

    def deposit(self, amount):
        cursor.execute(f"""UPDATE customs SET balance = balance + {amount} WHERE email = '{self.email}'""")
        connect.commit()
        self.balance += amount

    def minus(self, amount):
        cursor.execute(f"""UPDATE customs SET balance = balance - {amount} WHERE email = '{self.email}'""")
        connect.commit()
        self.balance -= amount

    def main(self):
        while True:
            print("1 = регистрация, 2 = пополнение, 3 = вывесьт денги, 4 = выйти")
            command = int(input("Выберите дествие: "))
            if command == 1:
                print('РЕГИСТРАЦИЯ')
                name = input("Введите имя: ")
                surname = input("Введите фамилию: ")
                age = int(input("Введите возраст: "))
                email = input("Введите email: ")
                self.register(name, surname, age, email)
                print(f"Вы успешно зарегистрировались! Ваш email: {email}")

            elif command == 2:
                if self.email:
                    print('ПОПОЛНЕНИЕ')
                    amount = int(input("Введите сумму: "))
                    self.deposit(amount)
                    print(f"Вы успешно пополнили сумму: {amount}")
                else:
                    print("Пройдите регистрацию")

            elif command == 3:
                if self.email:
                    print('ВЫВЕСТ ДЕНГИ')
                    amount = int(input('Введите суму для снятия: '))
                    self.minus(amount)
                    print(f"Вы успешно сняли сумму: {amount}")
                else:
                    print("Пройдите регистрацию")
            elif command == 4:
                break

            else:
                 print("1 = регистрация, 2 = пополнение, 3 = вывесьт денги, 4 = выйти")
                 command = int(input("Выберите дествие: "))



bank = Bank()
bank.main()