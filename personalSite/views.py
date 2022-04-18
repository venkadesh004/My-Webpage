from flask import Blueprint, render_template
from .models import Blog, db

views = Blueprint('views', __name__)


@views.route('/')
def index():
    # db = client.test
    # print(db)
    return render_template("home.html")

@views.route('/blogwriter', methods=["POST", "GET"])
def blogwriter():
    blog = Blog()
    return blog.signup()

@views.route('/blogs', methods=["POST", "GET"])
def blogs():
    # print(blog.signup())
    data = db.blogs.find()
    # print(db)
    data = db.blogs.find()
    # print(data)
    dataLst = []
    for i in data:
        if i["heading"] != None or i["content"] != None or i["date"] != None:
            dataLst.append(i)
    dataLst.reverse()
    return render_template("blogs.html", data=dataLst)

@views.route('/blogs/myWriter', methods=["POST", "GET"])
def blogWriter():
    return render_template("blogWriter.html")

@views.route('/blogs/<int:blogId>')
def blogPage(blogId):
    print(blogId)
    data = db.blogs.find_one({"_id": blogId})
    print(data)
    return render_template("blogPage.html", data=data)

@views.route('/acheivements')
def achievements():
    return render_template("achievements.html")

@views.route('/contact-me')
def contactMe():
    return render_template("contactme.html")