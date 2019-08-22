import sqlite3

conn = sqlite3.connect('tutorial.db')
c = conn.cursor()

def create_table():
    c.execute("CREATE TABLE example(Language VARCHAR, Version REAL, Skill TEXT)")

def enter_data():
    c.execute("INSERT INTO example VALUES('Ruby on rails', 1.7, 'Begginer')")
    c.execute("INSERT INTO example VALUES('Ruby on rails', 2.3, 'Intermediate')")
    c.execute("INSERT INTO example VALUES('Ruby on rails', 5.4, 'Expert')")
    conn.commit()

def enter_dynamic_data():
    lang = input("What language?: ")
    version = float(input("What version?: "))
    skill = input("What skill level?: ")

    c.execute("INSERT INTO example (Language, Version, Skill) VALUES(?, ?, ?)", (lang, version, skill))
    conn.commit()

def read_from_database():

    what_skill = input("What skill are you looking for?: ")
    what_language = input("What language are you looking for?: ")
    
    sql = "SELECT * FROM example WHERE Skill == ? AND Language == ?"

    for row in c.execute(sql, [(what_skill), (what_language)]):
        print(row)

def update_database():
    sql = "UPDATE example SET Skill = 'Intermediate' WHERE Skill = 'Intermidiate'"

    c.execute(sql)

    sql = "SELECT * FROM example"

    for row in c.execute(sql):
        print(row)

    conn.commit()

def delete_database():
    sql = "DELETE FROM example WHERE Version = '5.4'"
    c.execute(sql)

    sql = "SELECT * FROM example"
    for row in c.execute(sql):
        print(row)
    conn.commit()

        
delete_database()


#conn.close()
