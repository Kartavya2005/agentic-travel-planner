from database.db_connection import get_connection
from auth.password_utils import hash_password


def register_user(name, email, password):

    conn = get_connection()
    cursor = conn.cursor()

    hashed = hash_password(password)

    try:

        cursor.execute(
            """
            INSERT INTO users (name, email, password_hash)
            VALUES (%s, %s, %s)
            """,
            (name, email, hashed)
        )

        conn.commit()

        return True, "User registered successfully!"

    except Exception as e:

        return False, "Email already exists!"

    finally:
        cursor.close()
        conn.close()
