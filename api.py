from flask import Flask, jsonify, request, url_for, render_template
import requests
from UnitOfWork import SqlAlchemyUnitOfWork
from DB.DBModels import User
from Services.UserService import UserService

app = Flask(__name__, template_folder='template')


# Настройка подключения к базе данных


@app.route("/user/<int:user_id>")
def get_user(user_id):
    print(user_id)
    uow = SqlAlchemyUnitOfWork()
    with uow:
        user = uow.repository.get_by_id(User, user_id)

        if user is None:
            return dict(), 404
        return user.to_dict()


@app.route("/user/add", methods=["POST"])
def add_user():
    uow = SqlAlchemyUnitOfWork()
    uservice = UserService(uow)

    data = request.json

    res = uservice.execute(data)

    return {'user': res}


@app.route("/user/form", methods=["GET", "POST"])
def user_form():
    if request.method == "POST":
        path = "http://localhost:5000" + url_for("add_user")
        response = requests.post(path, json=request.form)
        return render_template("input.html", response=response.json())
    else:
        return render_template("input.html")


if __name__ == '__main__':
    app.run(debug=True)