from utils.parser import CommandParser
from nlp import process_nlp_input
from rich.console import Console
from rich.prompt import Prompt
from rich.panel import Panel
from rich.align import Align
from rich.text import Text
from rich.console import Group
import os

console = Console()

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def show_welcome():
    # Title
    title = Align.center(Text("PyTerminal\n", style="bold cyan", justify="center"))

    # Subtitle
    subtitle = Align.center(Text("Python Based Smart Terminal for Developers\n", style="bold white"))

    # Features
    commands = ["Filesystem Operations", "Process Checks", "Commands History","Natural Language Queries"]
    commands_text = Text(" | ".join(commands), style="grey20")
    commands_text = Align.center(commands_text)

    # Together in a Box
    group = Group(title, subtitle, commands_text)

    # 5️⃣ Put in a panel
    panel = Panel(
        group,
        title="[bold yellow]Welcome[/bold yellow]",
        border_style="bright_blue",
        padding=(1, 4),
    )

    console.print(panel)


def main():
    clear_screen()
    show_welcome()  # Display welcome panel
    parser = CommandParser(console)

    while True:
        try:
            current_dir = os.getcwd()
            prompt_text = f"\n[bold yellow]Current Directory:[/bold yellow] {current_dir}\n[bold green]PyTerminal>>[/bold green]"
            user_input = Prompt.ask(prompt_text)
            console.print("")
            if user_input.strip().lower() in ["exit", "quit"]:
                console.print("[bold yellow]Exiting PyTerminal...[/bold yellow]")
                break

            if user_input.startswith("!ai"):
                process_nlp_input(user_input.replace("!ai", "", 1).strip(), parser, console)
            else:
                parser.execute(user_input)

        except KeyboardInterrupt:
            console.print("\n[red]Use 'exit' to quit.[/red]")
        except EOFError:
            break

if __name__ == "__main__":
    main()
