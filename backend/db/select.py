import db
from db.types import User


def user_by_id(id: int) -> User:
    cursor, connection = db.connect()
    user_tuple = cursor.execute(f"SELECT * FROM users WHERE id=?", (id,)).fetchone()
    assert user_tuple is not None
    connection.close()
    return User(
        id=user_tuple[0],
        email=user_tuple[1],
        password=user_tuple[2],
        first_name=user_tuple[3],
        last_name=user_tuple[4],
        ssn=user_tuple[5],
    )


def user_by_email(email: str) -> User:
    cursor, connection = db.connect()
    user_tuple = cursor.execute(
        f"SELECT * FROM users WHERE email=?", (email,)
    ).fetchone()
    assert user_tuple is not None
    connection.close()
    return User(
        id=user_tuple[0],
        email=user_tuple[1],
        password=user_tuple[2],
        first_name=user_tuple[3],
        last_name=user_tuple[4],
        ssn=user_tuple[5],
    )


def user_password(email: str) -> str:
    cursor, connection = db.connect()
    password = cursor.execute(
        "SELECT password FROM users WHERE email=?", (email,)
    ).fetchone()[0]
    connection.close()
    assert isinstance(password, str)
    return password


def user_id(email: str) -> str:
    cursor, connection = db.connect()
    id = cursor.execute("SELECT id FROM users WHERE email=?", (email,)).fetchone()[0]
    connection.close()
    assert isinstance(id, str)
    return id
