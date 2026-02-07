from agents.orchestrator import Orchestrator

planner = Orchestrator()

result = planner.plan_trip(
    1,              # user_id (change if needed)
    "Indore",
    "Goa",
    4,
    "Family"
)

print(result)
