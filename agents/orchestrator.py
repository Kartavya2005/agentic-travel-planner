from agents.researcher_agent import ResearcherAgent
from agents.travel_agent import TravelAgent
from agents.budget_agent import BudgetAgent
from agents.writer_agent import WriterAgent
from utils.distance_helper import get_distance
from services.trip_service import save_trip


class Orchestrator:

    def __init__(self):
        self.researcher = ResearcherAgent()
        self.travel_agent = TravelAgent()
        self.budget_agent = BudgetAgent()
        self.writer = WriterAgent()

    def plan_trip(self, user_id, source, destination, days, trip_type):

        distance = get_distance(source, destination)

        if not distance:
            return "Distance not found in database."

        hotels = self.researcher.get_hotels(destination)

        avg_hotel_price = sum(
            h["price"] for h in hotels
        ) // len(hotels)

        travel_options = self.travel_agent.estimate_cost(distance)

        cheapest_travel = min(travel_options.values())

        total, category = self.budget_agent.calculate_total(
            avg_hotel_price,
            cheapest_travel,
            days
        )
        save_trip(
            user_id,
            source,
            destination,
            days,
            trip_type,
            total
        )

        return self.writer.generate_plan(
            source,
            destination,
            days,
            hotels,
            travel_options,
            total,
            category
        )
