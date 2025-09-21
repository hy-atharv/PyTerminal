import psutil
from rich.console import Console
from rich.table import Table

class SystemCommands:
    def __init__(self, console: Console):
        self.console = console

    def cpu(self, args):
        usage = psutil.cpu_percent(interval=1)
        self.console.print(f"[bold cyan]CPU Usage:[/bold cyan] {usage}%")

    def mem(self, args):
        mem = psutil.virtual_memory()
        table = Table(title="Memory Usage")
        table.add_column("Attribute", style="yellow")
        table.add_column("Value", style="green")
        table.add_row("Total", f"{mem.total / (1024**3):.2f} GB")
        table.add_row("Available", f"{mem.available / (1024**3):.2f} GB")
        table.add_row("Used", f"{mem.used / (1024**3):.2f} GB")
        table.add_row("Percentage", f"{mem.percent}%")
        self.console.print(table)

    def processes(self, args):
        table = Table(title="Running Processes")
        table.add_column("PID", style="cyan")
        table.add_column("Name", style="green")
        for proc in psutil.process_iter(['pid', 'name']):
            table.add_row(str(proc.info['pid']), proc.info['name'])
        self.console.print(table)
