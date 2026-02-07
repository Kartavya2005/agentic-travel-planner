from agents.orchestrator import Orchestrator

planner = Orchestrator()

result = planner.plan_trip(
    "Indore",
    "Goa",
    4
)

print(result)
