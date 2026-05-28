import json

def parse_openrouter_stream(line) : 
        try:
            line_text = line.decode('utf-8')
            if line_text.startswith('data: '):
                data = line_text.removeprefix('data: ')
                if data == '[DONE]' : return
                parsed = json.loads(data)
                # Process normal content
                content = parsed['choices'][0]['delta'].get('content')
                if content:
                    return content
        except Exception as e :
            print(f" Error while parsing open router sse token, {e}, {line}") 