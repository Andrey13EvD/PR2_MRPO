from flask import Flask, request, jsonify, redirect, url_for
from sqlalchemy.orm import sessionmaker
from DB.DBModels import engine, User, Exercise, TrainingProgram
from Services.register_user import register_user
from Services.create_exercise_service import create_exercise
from Services.check_user_register import CheckUserRegister
from Repository import UserRepository

# Создание Flask приложения
app = Flask(__name__)

# Создание сессии
Session = sessionmaker(bind=engine)
session = Session()

# Роут для регистрации пользователя
from flask import render_template

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/register', methods=['POST'])
def register():
    data = request.json
    try:
        new_user = register_user(
            age=data['age'],
            gender=data['gender'],
            weight=data['weight'],
            height=data['height'],
            name=data['name'],
            purpose=data['purpose'],
            username=data['username'],
            password=data['password']
        )
        if new_user:
            return jsonify({'message': 'User registered successfully!'}), 201
        else:
            return jsonify({'message': 'Username already exists.'}), 409
    except KeyError as e:
        return jsonify({'message': f'Missing parameter: {e}'}), 400

# Роут для создания упражнения
@app.route('/exercise', methods=['POST'])
def create_exercise_route():
    data = request.json
    try:
        new_exercise = create_exercise(
            name=data['name'],
            description=data['description'],
            repetitions=data['repetitions'],
            equipment_id=data.get('equipment_id'),
            muscle_group_ids=data.get('muscle_group_ids', [])
        )
        if new_exercise:
            return jsonify({'message': 'Exercise created successfully!'}), 201
        else:
            return jsonify({'message': 'Error creating exercise.'}), 400
    except KeyError as e:
        return jsonify({'message': f'Missing parameter: {e}'}), 400

# Роут для проверки регистрации пользователя
@app.route('/check_registration', methods=['POST'])
def check_registration():
    data = request.json
    try:
        user_id = data['user_id']
        user_repo = UserRepository(session)
        checker = CheckUserRegister(user_repo)
        is_registered = checker.execute(user_id)
        return jsonify({'is_registered': is_registered}), 200
    except KeyError as e:
        return jsonify({'message': f'Missing parameter: {e}'}), 400

# Роут для получения всех упражнений
@app.route('/exercises', methods=['GET'])
def get_exercises():
    exercises = session.query(Exercise).all()
    exercise_list = [
        {
            'id': exercise.id,
            'name': exercise.name,
            'description': exercise.description,
            'repetitions': exercise.repetitions
        } for exercise in exercises
    ]
    return jsonify(exercise_list), 200

# Запуск приложения
if __name__ == '__main__':
    app.run(debug=True)
