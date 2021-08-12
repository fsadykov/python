from app import db, User


user = User(fname='Farkhod', lname='Sadykov', username='farkhodsadykov', email='sadykovfarkhod@gmail.com')

Session = sessionmaker(bind=engine)
