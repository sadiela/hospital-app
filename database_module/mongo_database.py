import pymongo

#filepath = r'C:\Users\sadie\Documents\BU\spring_2022\ec530\hospital-app\cert\X509-cert-1835095331508356146.pem'
filepath = r'/Users/sadiela/Documents/courses_spring_2022/ec530/cert/X509-cert-1835095331508356146.pem'

uri  = r"mongodb+srv://cluster0.ipuos.mongodb.net/healthDB?authSource=%24external&authMechanism=MONGODB-X509&retryWrites=true&w=majority"
mongodb_client = pymongo.MongoClient(uri,
                     tls=True,
                     tlsCertificateKeyFile=filepath)

                    # hospital-app\cert\X509-cert-1835095331508356146.pem