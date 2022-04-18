from flask import Flask, jsonify, request 
import pymongo

#database
client = pymongo.MongoClient("mongodb+srv://venky:venkadesh@users.pxarx.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.blogPage

class Blog:

    def signup(self):

        blogData = {
            "_id": "",
            "heading": request.form.get('heading'),
            "content": request.form.get('content'),
            "date": request.form.get('date')
        }

        count = 0

        print("Request Accepted")

        datas = db.blogs.find()
        for i in datas:
            count += 1

        blogData["_id"] = count

        print("Going to insert data!")

        if db.blogs.insert_one(blogData):
            print("Successfully inserted!!")
            return jsonify(blogData), 200
    
        return jsonify({"error", "Entry Failed"}), 400