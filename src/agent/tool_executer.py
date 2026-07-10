from exceptions import ToolNotFoundError


class ToolExecutor:
    def __init__(self, tools):
        self.tools = tools

    def execute(self, tool_name, args):

        tool = self.tools.get(tool_name)

        if tool is None:
            raise ToolNotFoundError(f"Tool {tool_name} not found")

        tool.validate(args)

        return tool.execute(**args)
