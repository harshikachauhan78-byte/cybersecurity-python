import hashlib
import sqlite3


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def register(username, password):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    hashed = hash_password(password)

    try:
        cursor.execute(
            "INSERT INTO users(username, password) VALUES (?, ?)",
            (username, hashed)
        )
        conn.commit()
        print("Registration Successful!")
    except sqlite3.IntegrityError:
        print("Username already exists!")

    conn.close()


def login(username, password):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    hashed = hash_password(password)

    cursor.execute(
        "SELECT * FROM users WHERE username=? AND password=?",
        (username, hashed)
    )

    user = cursor.fetchone()

    if user:
        print("Login Successful!")
    else:
        print("Invalid Username or Password!")

    conn.close()