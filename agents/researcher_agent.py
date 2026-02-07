from database.db_connection import get_connection
from scrapers.hotel_scraper import scrape_hotels

class ResearcherAgent:

    def get_hotels(self, city):

        conn = get_connection()
        cursor = conn.cursor(dictionary=True)

        cursor.execute(
            "SELECT * FROM hotels WHERE city=%s",
            (city,)
        )

        hotels = cursor.fetchall()

        # If DB empty → scrape
        if not hotels:

            scraped_hotels = scrape_hotels(city)

            for hotel in scraped_hotels:

                cursor.execute(
                    """
                    INSERT INTO hotels (city, hotel_name, price, rating)
                    VALUES (%s,%s,%s,%s)
                    """,
                    (
                        city,
                        hotel["name"],
                        hotel["price"],
                        hotel["rating"]
                    )
                )

            conn.commit()

            hotels = scraped_hotels

        cursor.close()
        conn.close()

        return hotels
