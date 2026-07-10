class LLMRunner:

    def __init__(self, llm):
        self.llm = llm


    def run(self, messages):

        return self.llm.call_openrouter_api(
            messages=messages
        )