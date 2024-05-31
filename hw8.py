import sqlite3

connect = sqlite3.connect("optima_bank.db")
cursor = connect.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS customs(
               id INTEGER PRIMARY KEY,
               name VARCHAR(100) NOT NULL,
               surname VARCHAR(100) NOT NULL,  
               age INTEGER NOT NULL,
               email TEXT, balance DOUBLE (8, 2),
               is_active BOOLEAN DEFAULT FALSE);""")

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

    def plus(self, pl):
        cursor.execute(f"""UPDATE customs SET balance = balance + {pl} WHERE email = '{self.email}'""")
        connect.commit()
        self.balance += pl

    def minus(self, min):
        cursor.execute(f"""UPDATE customs SET balance = balance - {min} WHERE email = '{self.email}'""")
        connect.commit()
        self.balance -= min

    def main(self):
        while True:
            print("1 = войти, 2 = пополнение, 3 = вывесьт денги, 4 = выйти")
            command = int(input("Выберите дествие: "))
            if command == 1:
                
                name = input("Введите имя: ")
                surname = input("Введите фамилию: ")
                age = int(input("Введите возраст: "))
                email = input("Введите email: ")
                self.register(name, surname, age, email)
                print(f"Вы успешно вошли! Ваш email: {email}")

            elif command == 2:
                if self.email:
                    
                    pl = int(input("Введите сумму: "))
                    self.plus(pl)
                    print(f"Вы успешно пополнили сумму: {pl}")
                else:
                    print("Попробуйте заново")

            elif command == 3:
                if self.email:
                    
                    min = int(input('Введите суму для снятия: '))
                    self.minus(min)
                    print(f"Вы успешно сняли сумму: {min}")
                else:
                    print("Попробуйте заново")
            elif command == 4:
                break

            else:
                 print("1 = войти, 2 = пополнение, 3 = вывесьт денги, 4 = выйти")
                 command = int(input("Выберите дествие: "))



bank = Bank()
bank.main()