from tools.custom_tools import execute_tool

class ToolAgent:

    def execute_task(self, plan):
        print("[Tool Agent Activated]")
        return execute_tool(plan)
