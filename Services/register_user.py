from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError
from DB.DBModels import User, Recommendations, engine
import hashlib

# Создание сессии
Session = sessionmaker(bind=engine)
session = Session()

def encrypt_password(password: str) -> str:
    return hashlib.sha256(password.encode('utf-8')).hexdigest()

def register_user(age: int, gender: str, weight: float, height: float, name: str, purpose: str, username: str, password: str, recommendations_id: int = None) -> User:
    encrypted_password = encrypt_password(password)

    new_user = User(
        age=age,
        gender=gender,
        weight=weight,
        height=height,
        name=name,
        purpose=purpose,
        username=username,
        _password=encrypted_password,
        recommendations_id=recommendations_id
    )

    try:
        session.add(new_user)
        session.commit()
        print("Пользователь успешно зарегистрирован!")
        return new_user
    except IntegrityError:
        session.rollback()
        print("Ошибка: Пользователь с таким именем уже есть.")
        return None
    except Exception as e:
        session.rollback()
        print(f"Ошибка: {e}")
        return None

# Пример использования
if __name__ == "__main__":
    # Пример данных для нового пользователя
    age = 25
    gender = "male"
    weight = 70.0
    height = 175.0
    name = "John Doe"
    purpose = "Fitness"
    username = "johndoe"
    password = "securepassword123"

    registered_user = register_user(age, gender, weight, height, name, purpose, username, password)

    if registered_user:
        print(f"Пользователь {registered_user.name} зарегистрирован с ID: {registered_user.id}")
    else:
        print("Ошибка регистрации.")
