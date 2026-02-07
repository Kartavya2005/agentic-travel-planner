from utils.constants import FOOD_PER_DAY

class BudgetAgent:

    def calculate_total(self, hotel_price, travel_cost, days):

        food_cost = FOOD_PER_DAY * days

        total = hotel_price + travel_cost + food_cost

        if total < 10000:
            category = "Budget"
        elif total < 25000:
            category = "Moderate"
        else:
            category = "Luxury"

        return total, category
