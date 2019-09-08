class ToolsRepo(object):
    def __init__(self):
        self.tools = {}

    def register_tool(self, tool):
        self.tools[tool.id] = tool

    def get_tool(self, tool_od):
        return self.tools[tool_od]
