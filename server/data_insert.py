import sqlite3

connection = sqlite3.connect('MTG.db')
cursor = connection.cursor()

#Datainsert
Users = [[1,"abatista3056@gmail.com","abatista15",4079121683,"Admin1234"]]
for i in range(len(Users)):
    User_id = Users[i][0]
    Email = Users[i][1]
    Username = Users[i][2]
    Phone_number = Users[i][3]
    Password = Users[i][4]
    cursor.execute("INSERT INTO  Users VALUES(?,?,?,?,?)",(User_id,Email,Username,Phone_number,Password))

connection.commit()
connection.close()