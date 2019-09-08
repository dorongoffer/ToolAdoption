class ToolsRepo(object):
    def __init__(self):
        self.tools = {}

    def register_tool(self, tool):
        self.tools[tool.id] = tool

    def get_tool(self, tool_id):
        return self.tools[tool_id]

    def mark_abandoned(self, tool_id, generation):
        if tool_id not in self.tools:
            raise Exception("Tool {} is not registered".format(tool_id))
        tool = self.tools[tool_id]
        if tool.is_abandoned():
            raise Exception("Tool {} is already marked as abandoned at generation {}. This shouldn't happen.".format(
                tool_id, tool.abandoned_at))
        tool.abandoned_at = generation

    def __len__(self):
        return len(self.tools)

    def __iter__(self):
        return iter(self.tools.values())
