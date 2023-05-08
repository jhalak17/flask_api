import mysql.connector
from flask import make_response

class user_model():

    def __init__(self):
        self.con = mysql.connector.connect(host = "localhost", user = "root", password = "root", database = "flask_api")
        self.con.autocommit=True
        self.cursor = self.con.cursor(dictionary = True)

    def all_user_model(self):
        self.cursor.execute("Select * from users")
        result = self.cursor.fetchall()
        if len(result) > 0:
            return make_response({'users':result},200)
        else:
            return make_response({'users':"No Data Found"}, 204)
        
    def get_user_model(self, id):
        self.cursor.execute(f"SELECT * fROM users WHERE id = {id}")
        result = self.cursor.fetchall()
        if len(result) > 0:
            return make_response({'users':result},200)
        else:
            return make_response({'users':"No Data Found"}, 204)

    def add_user_model(self, data):
        self.cursor.execute(f"INSERT INTO users(name, email, phone, password) VALUES('{data['name']}', '{data['email']}', '{data['phone']}', '{data['password']}')")
        return make_response({"message":"User Created Successfully"}, 201)

    def update_user_model(self, data):
        self.cursor.execute(f"UPDATE users SET name = '{data['name']}', email = '{data['email']}', phone = '{data['phone']}', password = '{data['password']}' WHERE id = {data['id']}")
        if self.cursor.rowcount > 0:
            return make_response({"message":"User Updated Successfully"}, 200)
        else:
            return make_response({"message":"Nothing to Update"}, 202)
    
    def delete_user_model(self, id):
        self.cursor.execute(f"DELETE FROM users WHERE id = {id}")
        if self.cursor.rowcount > 0:
            return make_response({"message":"User Deleted Successfully"}, 200)
        else:
            return make_response({"message":"Nothing to Delete"}, 202)
