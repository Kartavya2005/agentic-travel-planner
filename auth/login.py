from database.db_connection import get_connection
from auth.password_utils import verify_password


def login_user(email, password):

    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute(
        "SELECT * FROM users WHERE email=%s",
        (email,)
    )

    user = cursor.fetchone()

    cursor.close()
    conn.close()

    if not user:
        return None, "User not found"

    stored_hash = user["password_hash"]

    if isinstance(stored_hash, str):
        stored_hash = stored_hash.encode()

    if verify_password(password, stored_hash):
        return user, "Login successful"

    return None, "Invalid password"
