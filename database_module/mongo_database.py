import pymongo
uri  = r"mongodb+srv://cluster0.ipuos.mongodb.net/healthDB?authSource=%24external&authMechanism=MONGODB-X509&retryWrites=true&w=majority"
mongodb_client = pymongo.MongoClient(uri,
                     tls=True,
                     tlsCertificateKeyFile='/Users/sadiela/Documents/courses_spring_2022/ec530/cert/X509-cert-1835095331508356146.pem')