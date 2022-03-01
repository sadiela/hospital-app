from pymongo import MongoClient
import gridfs

db = MongoClient().gridfs_example
fs = gridfs.GridFS(db)