class PlannerAgent:

    def create_plan(self, user_input):
        print("[Planner Agent Activated]")
        steps = f"Step 1: Understand task\nStep 2: Use tools\nStep 3: Generate output for: {user_input}"
        return steps
