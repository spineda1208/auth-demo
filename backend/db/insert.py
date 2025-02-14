import db
from db.core import connect
from .types import User


def user(user: User) -> int:
    assert user.id is None
    cursor, connection = db.connect()

    cursor.execute(
        "INSERT INTO users(email, password,  first_name, last_name, ssn) VALUES (?, ?, ?, ?, ?) RETURNING id;",
        (user.email, user.password, user.first_name, user.last_name, user.ssn),
    )
    user_id = cursor.fetchone()

    assert user_id is not None

    connection.commit()
    connection.close()
    return user_id
