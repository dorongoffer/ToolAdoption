from json import JSONEncoder

from util.tools_repo import ToolsRepo


class JsonSerializer(JSONEncoder):
    def default(self, o):
        if isinstance(o, set):
            return sorted(list(o))
        if isinstance(o, ToolsRepo):
            return sorted(o.tools.values(), key=id)
        return o.__dict__
