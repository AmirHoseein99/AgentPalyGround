# ai.py
import sys
from rich import print
from llm.openrouter import OpenRouterAPI
from llm.prompt import SYSTEM_PROMPT

def main():
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
    ]

    while True:
        print("[cyan] Ai Assistant is here, print /exit to quit, /clear to reset[/cyan]\n")
        user_message = input("You: ")
        
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
            openrouter_api = OpenRouterAPI()
            llm_response = openrouter_api.call_openrouter_api(messages)
            result = openrouter_api.format_response(llm_response)
            print("[green]\n--- Response ---\n[/green]")
            print(result)
        except Exception as e:
            print(f"[red]Error:[/red] {e}")


if __name__ == "__main__":
    main()