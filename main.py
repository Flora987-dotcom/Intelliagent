from agents.planner_agent import PlannerAgent
from agents.tool_agent import ToolAgent
from agents.evaluator_agent import EvaluatorAgent
from memory.session_memory import SessionMemory
from observability.logger import log_activity

planner = PlannerAgent()
tool = ToolAgent()
evaluator = EvaluatorAgent()
memory = SessionMemory()

def run_system(user_input):

    log_activity("User Input Received")

    memory.save_input(user_input)

    plan = planner.create_plan(user_input)

    result = tool.execute_task(plan)

    final = evaluator.validate_output(result)

    memory.save_output(final)

    log_activity("Task Completed")

    return final


if __name__ == "__main__":
    while True:
        user_input = input("\nEnter your task: ")
        if user_input.lower() == "exit":
            break

        response = run_system(user_input)
        print("\nFinal Response:\n", response)
