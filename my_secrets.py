import os
from rich import print
from dotenv import load_dotenv

load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")
if not gemini_api_key:
    print(
        "[bold red]Error:[/bold red] [green]GEMINI_API_KEY[/green] not found in environment variables. Please set it in your .env file."
    )
    exit(1)

gemini_api_url = os.getenv("GEMINI_API_URL")
if not gemini_api_url:
    print(
        "[bold red]Error:[/bold red] [green]GEMINI_API_URL[/green] not found in environment variables. Please set it in your .env file."
    )
    exit(1)

gemini_api_model = os.getenv("GEMINI_API_MODEL")
if not gemini_api_model:
    print(
        "[bold red]Error:[/bold red] [green]GEMINI_API_MODEL[/green] not found in environment variables. Please set it in your .env file."
    )
    exit(1)


class Secrets:
    def __init__(self):
        self.gemini_api_key = gemini_api_key
        self.gemini_api_url = gemini_api_url
        self.gemini_api_model = gemini_api_model