# ai.py
from multiprocessing.spawn import import_main_path
import sys
from rich import print
from llm.openrouter import OpenRouterAPI
from llm.prompt import SYSTEM_PROMPT
from llm.utils import stream_to_terminal
def main():
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
    ]

    openrouter_api = OpenRouterAPI()
    print("\n[cyan] Ai Assistant is here, print /exit to quit, /clear to reset[/cyan]\n")
    while True:
        print("\n[red] You : [/red]")
        user_message = input('      ')
        
        if user_message.strip().lower() == "/exit":
            print("[yellow]Exiting...[/yellow]")
            sys.exit(0)
        elif user_message.strip().lower() == "/clear":
            messages = [
                {"role": "system", "content": SYSTEM_PROMPT}
            ]
            print("[yellow]Conversation cleared.[/yellow]\n")
            continue
        else:
            messages.append({"role": "user", "content": user_message})
        try:
            print("[blue] Thinking ... [/blue]\n")
            stream_to_terminal(openrouter_api=openrouter_api, messages=messages)
        except Exception as e:
            print(f"[red]Error:[/red] {e}")


if __name__ == "__main__":
    main()