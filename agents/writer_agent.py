class WriterAgent:

    def generate_plan(
        self,
        source,
        destination,
        days,
        hotels,
        travel_options,
        total_cost,
        category
    ):

        best_hotel = hotels[0]

        return f"""
Trip Plan: {source} → {destination}

Duration: {days} days
Hotel: {best_hotel['hotel_name'] if 'hotel_name' in best_hotel else best_hotel['name']}

Travel Options:
Train: ₹{travel_options['Train']}
Bus: ₹{travel_options['Bus']}
Flight: ₹{travel_options['Flight']}

Estimated Total Cost: ₹{total_cost}

Trip Category: {category}
"""
