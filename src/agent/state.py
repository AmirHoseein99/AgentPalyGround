from dataclasses import dataclass, field


@dataclass
class AgentState:
    conversation_id: str
    user_input: str

    messages: list = field(default_factory=list)

    current_step: int = 0

    last_response: dict | None = None

    tool_results: list = field(default_factory=list)

    finished: bool = False

    final_answer: str | None = None
