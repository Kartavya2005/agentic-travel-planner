from utils.constants import (
    TRAIN_COST_PER_KM,
    BUS_COST_PER_KM,
    FLIGHT_COST_PER_KM
)

class TravelAgent:

    def estimate_cost(self, distance):

        train = int(distance * TRAIN_COST_PER_KM)
        bus = int(distance * BUS_COST_PER_KM)
        flight = int(distance * FLIGHT_COST_PER_KM)

        return {
            "Train": train,
            "Bus": bus,
            "Flight": flight
        }
