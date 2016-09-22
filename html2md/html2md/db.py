# -*- coding: utf-8 -*-

import datetime
from peewee import *

db = SqliteDatabase('note.db')

class Note(Model):
    title = CharField()
    url = CharField()
    content = TextField()

    class Meta:
        database = db # This model uses the "people.db" database.

class Image(Model):
    url = CharField()
    path = CharField()

    class Meta:
        database = db

class Urls(Model):
    title = CharField(null=True)
    url = CharField(unique=True)
    state = IntegerField(null=True)
    timestamp = DateTimeField(null=True,default=datetime.datetime.now)

    class Meta:
        database = db

def delete_note():
    return Note.delete().execute()

def delete_image():
    return Image.delete().execute()

def init_table():
    db.connect()
    db.create_tables([Note, Image, Urls])

if __name__ == '__main__':
    db.connect()
    db.create_tables([Note, Image, Urls])