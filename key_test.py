from openai import OpenAI, OpenAIError
from colorama import init
from rich.console import Console
import os
os.system('cls' if os.name == 'nt' else 'clear')

init(autoreset=True)

console = Console()

banner_text = """
░█▀█░█▀█░█▀▀░█▀█░█▀█░▀█▀░░░█▀█░█▀█░▀█▀░░░█░█░█▀▀░█░█░░░▀█▀░█▀▀░█▀▀░▀█▀
░█░█░█▀▀░█▀▀░█░█░█▀█░░█░░░░█▀█░█▀▀░░█░░░░█▀▄░█▀▀░░█░░░░░█░░█▀▀░▀▀█░░█░
░▀▀▀░▀░░░▀▀▀░▀░▀░▀░▀░▀▀▀░░░▀░▀░▀░░░▀▀▀░░░▀░▀░▀▀▀░░▀░░░░░▀░░▀▀▀░▀▀▀░░▀░
                                      x/HFerrahoglu
"""
console.print(banner_text, style="yellow")

api_key = input("Please enter your OpenAI API key: ")

client = OpenAI(api_key=api_key)

try:
    completion = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Hello, how are you?"}
        ]
    )
    print("\n")
    console.print("[bold green]API key is valid. Request successful.[/bold green]")

except OpenAIError:
    print("\n")
    console.print("[bold red]API key is invalid or does not work.[/bold red]")

