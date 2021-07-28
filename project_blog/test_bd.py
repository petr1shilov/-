import sqlite3

class Bd_actions:

    def __init__(self, database):
        # Подключаемся к БД и сохраняем курсор соединения
        self.connection = sqlite3.connect(database)
        self.cursor = self.connection.cursor()
    
    
    # Проверяем, есть ли уже пользователь в базе
    def exists_user(self, user_name):
            
            with self.connection:
                result = self.cursor.execute('SELECT * FROM `user_reqest_user_request` WHERE `user_name` = ?', (user_name,)).fetchall()
                return bool(len(result)) 
            self.connection.commit()

        # Добавляем нового пользователя
    def add_User(self, user_name, text_1, pub_date, user_conact, pub_time):
        
        with self.connection:
            return self.cursor.execute("INSERT INTO `user_reqest_user_request` (`user_name`, `text_1`, `pub_date`, `user_conact`, `pub_time`) VALUES(?,?)", (user_name,text_1, pub_date, user_conact, pub_time))
        self.connection.commit()

    # Обновляем таблицы
    def update_user(self, user_name, text_1):
        
        with self.connection:
            return self.cursor.execute('''UPDATE `user_reqest_user_request` SET `text_1` = ? WHERE `user_name` = ?''', (user_name, text_1))        
        self.connection.commit()

    # Уданение элемента из таблицы
    def delite(self, user_name):
        with self.connection:
            return self.cursor.execute('''DELETE FROM `user_reqest_user_request` WHERE `user_name` = ? ''', (user_name))
        self.connection.commit()
