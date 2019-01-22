#import pymysql

#conn=pymysql.connect(host="localhost",user="root",passwd="",db="mypython")
#myCursor = conn.cursor()
#myCursor.execute("select * from names;")

#def Trainees():
 #   trainees = myCursor.fetchall()
 #   return trainees

def Trainees():
    Trainees = [
        {
            'id': 1,
            'Name':'Rim',
            'email':'Rim@sta.com',
            'age':'20',
            'Registeredsince':'04-25-2017'
        },
        {
            'id': 2,
            'Name':'Adam',
            'email':'Adam@sta.com',
            'age':'28',
            'Registeredsince':'01-23-2017'
        },
        {
            'id': 3,
            'Name':'Adelle',
            'email':'Adelle@sta.com',
            'age':'16',
            'Registeredsince':'02-05-2017'
        },
        {
            'id': 4,
            'Name':'Fadel',
            'email':'Fadel@sta.com',
            'age':'23',
            'Registeredsince':'01-05-2017'
        },
        {
            'id': 5,
            'Name':'Pamella',
            'email':'Pam@sta.com',
            'age':'26',
            'Registeredsince':'02-07-2017'
        },
        {
            'id': 6,
            'Name':'Tia',
            'email':'Tia@sta.com',
            'age':'17',
            'Registeredsince':'07-05-2017'
        },
        {
            'id': 7,
            'Name':'Sara',
            'email':'Serah@sta.com',
            'age':'16',
            'Registeredsince':'01-15-2017'
        },
        {
            'id': 8,
            'Name':'Karim',
            'email':'Karim@sta.com',
            'age':'24',
            'Registeredsince':'03-05-2017'
        },
        {
            'id': 9,
            'Name':'Nivine',
            'email':'Nivine@sta.com',
            'age':'26',
            'Registeredsince':'02-12-2017'
        }
    ]
    return Trainees

