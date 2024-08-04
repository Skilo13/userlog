class UserManager:
    def __init__(self):
        self.users = {}
        self.next_id = 1

    def addUser(self, name):
        # Создание нового пользователя с уникальным ID
        user_id = self.next_id
        self.users[user_id] = name
        self.next_id += 1
        return user_id

    def getUser(self, user_id):
        # Получение имени пользователя по его уникальному ID
        return self.users.get(user_id, None)

    def deleteUser(self, user_id):
        # Удаление пользователя по его уникальному ID
        if user_id in self.users:
            del self.users[user_id]
            return True
        return False

    def findUserByName(self, name):
        # Поиск всех ID пользователей по их имени
        return [user_id for user_id, user_name in self.users.items() if user_name == name]
userManager = UserManager()

id1 = userManager.addUser("Jarasar")
id2 = userManager.addUser("Adil")
id3 = userManager.addUser("Jarasar")

print(userManager.getUser(id1))  # Вернет "Jarasar"
print(userManager.getUser(id2))  # Вернет "Adil"
print(userManager.getUser(999))  # Вернет None

print(userManager.findUserByName("Jarasar"))  # Вернет [id1, id3]
print(userManager.findUserByName("Baha"))  # Вернет []

print(userManager.deleteUser(id2))  # Вернет True
print(userManager.deleteUser(999))  # Вернет False

print(userManager.getUser(id2))  # Вернет None