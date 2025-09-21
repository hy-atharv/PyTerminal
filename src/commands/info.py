from rich.console import Console
from rich.table import Table

class InfoCommands:
    def __init__(self, console: Console):
        self.console = console

    def show_commands(self, args=None):
        """Prints a table of available commands and descriptions."""
        table = Table(title="Available Commands", border_style="bright_blue")

        table.add_column("Command", style="cyan", no_wrap=True)
        table.add_column("Description", style="white")

        commands = [
            ("ls", "List files and directories in the current directory"),
            ("pwd", "Show the current directory path"),
            ("cd", "Change directory"),
            ("mkdir", "Create a new directory"),
            ("cat", "View a file's content or create and write to it"),
            ("rm", "Remove a file or directory"),
            ("mv", "Moves/Renames a file or directory"),
            ("cpu", "Show CPU usage percentage"),
            ("mem", "Show memory usage details"),
            ("processes", "List running processes"),
            ("help", "Show this commands table"),
            ("exit / quit", "Exit the terminal"),
        ]

        for cmd, desc in commands:
            table.add_row(cmd, desc)

        self.console.print(table)

        self.console.print("[magenta]Apart from the above mentioned commands, I can also talk and follow your instructions ^_^[/magenta]")
        self.console.print("[magenta]Use !ai prefix to talk with me or instruct me.[/magenta]")
