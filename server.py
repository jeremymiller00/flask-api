from random import shuffle
from sqlite3 import Connection as SQLite3Connection
from datetime import datetime
from sqlalchemy import event
from sqlalchemy.engine import Engine
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, request, jsonify
from LinkedList import LinkedList
from HashTable import HashTable
from BinarySearchTree import BinarySearchTree
from CustomQueue import CustomQueque
from CustomStack import CustomStack


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///sqlitedb.file"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = 0


# configure sqlite3 to enforce foreign key constraints
@event.listens_for(Engine, "connect")
def _set_sqlite_pragma(dbapi_connection, connection_record):
    if isinstance(dbapi_connection, SQLite3Connection):
        cursor = dbapi_connection.cursor()
        cursor.execute("PRAGMA foreign_keys=ON;")
        cursor.close()


db = SQLAlchemy(app)
now = datetime.now()


# data models - maps to a SQL table
# ORM with SQL Alchemy
class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(50))
    address = db.Column(db.String(200))
    phone = db.Column(db.String(50))
    posts = db.relationship("BlogPost", cascade="all, delete")


class BlogPost(db.Model):
    __tablename__ = "blog_post"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    body = db.Column(db.String(200))
    date = db.Column(db.Date)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)


@app.route("/user", methods=["POST"])
def create_user():
    data = request.get_json()
    new_user = User(
        name=data["name"],
        email=data["email"],
        address=data["address"],
        phone=data["phone"]
    )
    db.session.add(new_user)
    db.session.commit()
    return jsonify( {"message": "User Created"} ), 200


@app.route("/user/descending_id", methods=["GET"])
def get_all_users_descending():
    users = User.query.all()
    all_users_ll = LinkedList()

    for user in users:
        all_users_ll.insert_beginning(
            {
                "id": user.id,
                "name": user.name,
                "email": user.email,
                "address": user.address,
                "phone": user.phone,
            }
        )
    return jsonify(all_users_ll.to_list()), 200


@app.route("/user/ascending_id", methods=["GET"])
def get_all_users_ascending():
    users = User.query.all()
    all_users_ll = LinkedList()

    for user in users:
        all_users_ll.insert_beginning(
            {
                "id": user.id,
                "name": user.name,
                "email": user.email,
                "address": user.address,
                "phone": user.phone,
            }
        )
    return jsonify(all_users_ll.to_list()), 200


@app.route("/user/<user_id>", methods=["GET"])
def get_one_user(user_id):
    users = User.query.all()
    all_users_ll = LinkedList()

    for user in users:
        all_users_ll.insert_beginning(
            {
                "id": user.id,
                "name": user.name,
                "email": user.email,
                "address": user.address,
                "phone": user.phone,
            }
        )
    user = all_users_ll.get_user_by_id(user_id)
    return jsonify(user), 200


@app.route("/user/<user_id>", methods=["DELETE"])
def delete_user(user_id):
    user = User.query.filter_by(id=user_id).first()
    db.session.delete(user)
    db.session.commit()
    return jsonify( {"message": "user deleted"} ), 200


@app.route("/blog_post/<user_id>", methods=["POST"])
def create_blog_post(user_id):
    data = request.get_json()
    user = User.query.filter_by(id=user_id).first()
    if not user:
        return jsonify({"message": "user does not exist"}), 400
    
    ht = HashTable(10)
    ht.add_key_value_pair("title", data["title"])
    ht.add_key_value_pair("body", data["body"])
    ht.add_key_value_pair("date", now)
    ht.add_key_value_pair("user_id", user_id)
    
    blog_post = BlogPost(
        title = ht.get_value("title"),
        date = ht.get_value("date"),
        body = ht.get_value("body"),
        user_id = ht.get_value("user_id")
    )
    db.session.add(blog_post)
    db.session.commit()

    return jsonify({"message": "new blog post created"}), 200


@app.route("/user/<user_id>", methods=["GET"])
def get_all_blog_posts(user_id):
    pass


@app.route("/blog_post/<blog_post_id>", methods=["GET"])
def get_one_blog_post(blog_post_id):
    blog_posts = BlogPost.query.all()
    shuffle(blog_posts)
    bst = BinarySearchTree()
    for post in blog_posts:
        bst.insert({
            "id": post.id,
            "title": post.title,
            "body": post.body,
            "user_id": post.user_id,
        })

    result = bst.search(blog_post_id)
    if not result:
        return jsonify({"message": "post not found"}), 200
    return jsonify(result)


@app.route("/user/numeric_body", methods=["GET"])
def get_numeric_body():
    blog_posts = BlogPost.query.all()
    q = CustomQueque()
    for bp in blog_posts:
        q.enqueue(bp)
    output = []
    for i in range(len(blog_posts)):
        post = q.dequeue()
        numeric_body = 0
        if post.data.body is not None:
            for char in post.data.body:
                numeric_body += ord(char)
        post.data.body = numeric_body
        output.append(
            {
                "id": post.data.id,
                "title": post.data.title,
                "body": post.data.body,
                "user_id": post.data.user_id
            }
        )
    return jsonify(output), 200


@app.route("/user/<blog_post_id>", methods=["DELETE"])
def delete_blog_posts(user_id):
    pass


#######################################################

if __name__ == '__main__':
    app.run(debug=True)