from pymongo import MongoClient

connection = MongoClient("mongodb://user:password@ds155191.mlab.com:55191/goto_cats")
database = connection['goto_cats']
cats_collection = database['cats']

cats = [
            {"name": "Бывалый", "image": "images/1.jpg", "id": 1, "comments": []},
            {"name": "Красавица", "image": "images/2.jpg", "id": 2, "comments": []},
            {"name": "243", "image": "images/3.jpg", "id": 3, "comments": []},
            {"name": "Янезнаю", "image": "images/4.jpg", "id": 4, "comments": []},
            {"name": "Мурзик", "image": "images/5.jpg", "id": 5, "comments": []},
        ]

cats_collection.insert_many(cats)