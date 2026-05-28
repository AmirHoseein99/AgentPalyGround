from llm.parser import parse_openrouter_stream


def stream_to_terminal(openrouter_api, messages):
    for llm_response_chunk in openrouter_api.stream_openrouter_response(messages=messages):
        parsed_llm_response = parse_openrouter_stream(llm_response_chunk) 

        if parsed_llm_response :
            print(parsed_llm_response, end='', flush=True)