import json
from src.agent.parser import agent_format_response
from src.agent.state import AgentState
from src.exceptions import ParserError
from src.logger import get_logger
from src.memory.memory_manager import append_to_conversation


class ResponseHandler:
    def parse(self, response, conversation_id: str, state, logger):
        try:
            parsed_response = agent_format_response(response)
            append_to_conversation(
                role="assistant",
                content=parsed_response,
                conversation_id=conversation_id,
            )
            state.messages.append(
                {"role": "assistant", "content": json.dumps(parsed_response)}
            )
            state.last_resposne = json.dumps(parsed_response)
            return parsed_response
        except ParserError as e:
            logger.error(f"Failed to parse LLM response: {e}")
            state.messages.append(
                {
                    "role": "user",
                    "content": f"""
                        Your previous response could not be parsed.

                        Error:
                        {e}

                        Please produce a valid structured response.
                        """,
                }
            )
            raise ParserError(f"Failed to parse response: {e}")
