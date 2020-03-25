from data import db_session, users, jobs
from flask import Flask, render_template
import datetime

User = users.User
Jobs = jobs.Jobs
app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def create_start_base():
    data = [
        {'surname': "Scott",
         'name': "Ridley",
         'age': 21,
         'position': "captain",
         'speciality': "research engineer",
         'address': "module_1",
         'email': "scorr_chief@mars.org",
         'hashed_password': "qwerty123"},

        {'surname': "Hunhau",
         'name': "Nata",
         'age': 27,
         'position': "officer",
         'speciality': "scientist",
         'address': "module_2",
         'email': "natali@saturn.ru",
         'hashed_password': "hihihaha228"},

        {'surname': "Zayko",
         'name': "Oleg",
         'age': 19,
         'position': "soldier",
         'speciality': "cleaner",
         'address': "module_3",
         'email': "hunter337@yandex.ru",
         'hashed_password': "1pasha2is3nickto4lol5"},

        {'surname': "Hurican",
         'name': "Felix",
         'age': 15,
         'position': "officer",
         'speciality': "pilot",
         'address': "module_2",
         'email': "fifteen@mail.ru",
         'hashed_password': "JSADHuhkusahdu123u"}
    ]

    db_session.global_init("db/colonists.sqlite")
    session = db_session.create_session()
    for elem in data:
        user = User()
        user.surname = elem['surname']
        user.name = elem['name']
        user.age = elem['age']
        user.position = elem['position']
        user.speciality = elem['speciality']
        user.address = elem['address']
        user.email = elem['email']
        user.hashed_password = elem['hashed_password']
        session.add(user)

    jobs = Jobs()
    jobs.team_leader = 1
    jobs.job = 'deployment of residential modules 1 and 2'
    jobs.work_size = 15
    jobs.collaborators = '2, 3'
    jobs.start_date = datetime.datetime.now()
    jobs.is_finished = False
    session.add(jobs)

    jobs = Jobs()
    jobs.team_leader = 2
    jobs.job = 'clean'
    jobs.work_size = 3
    jobs.collaborators = '3'
    jobs.start_date = datetime.datetime.now()
    jobs.is_finished = False
    session.add(jobs)

    session.commit()


@app.route('/')
@app.route('/index')
def index():
    session = db_session.create_session()
    data = session.query(Jobs).all()
    return render_template("index.html", data=data)


def main():
    db_session.global_init('db/colonists.sqlite')
    app.run()


if __name__ == "__main__":
    main()
