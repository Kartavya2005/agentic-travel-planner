from database.db_connection import get_connection


def get_distance(source, destination):
    conn = get_connection()
    cursor = conn.cursor()

    query = """
        SELECT distance_km
        FROM city_distances
        WHERE source=%s AND destination=%s
    """

    cursor.execute(query, (source, destination))
    result = cursor.fetchone()

    cursor.close()
    conn.close()

    if result:
        return result[0]

    return None
