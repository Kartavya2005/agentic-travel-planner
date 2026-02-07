from database.db_connection import get_connection


def save_trip(
    user_id,
    source,
    destination,
    days,
    trip_type,
    cost
):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO trips
        (user_id, source, destination, days, trip_type, estimated_cost)
        VALUES (%s,%s,%s,%s,%s,%s)
        """,
        (user_id, source, destination, days, trip_type, cost)
    )

    conn.commit()

    cursor.close()
    conn.close()
def get_user_trips(user_id):

    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute(
        """
        SELECT * FROM trips
        WHERE user_id=%s
        ORDER BY created_at DESC
        """,
        (user_id,)
    )

    trips = cursor.fetchall()

    cursor.close()
    conn.close()

    return trips
