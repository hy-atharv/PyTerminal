import shlex
from io import StringIO
import sys
from commands.filesystem import FileSystemCommands
from commands.system import SystemCommands
from commands.info import InfoCommands


class CommandParser:
    def __init__(self, console):
        self.console = console
        self.fs = FileSystemCommands(console)
        self.sys = SystemCommands(console)
        self.info = InfoCommands(console)

        self.commands = {
            "ls": self.fs.ls,
            "pwd": self.fs.pwd,
            "cd": self.fs.cd,
            "mkdir": self.fs.mkdir,
            "cat": self.fs.cat,
            "rm": self.fs.rm,
            "mv": self.fs.mv,
            "cpu": self.sys.cpu,
            "mem": self.sys.mem,
            "processes": self.sys.processes,
            "help": self.info.show_commands,
        }

    def execute(self, user_input: str, capture_output: bool = False, content: str | None = None) -> str | None:
        """
        Execute a command.
        - capture_output=True: return output as string instead of printing.
        - content: optional string to pass to commands that accept it (e.g., cat).
        """
        try:
            tokens = shlex.split(user_input.strip())
            if not tokens:
                return ""

            cmd, *args = tokens
            if cmd not in self.commands:
                msg = f"[red]Unknown command:[/red] {cmd}"
                if capture_output:
                    self.console.print(msg)
                    return msg
                self.console.print(msg)
                return ""

            if capture_output:
                # Redirect stdout temporarily
                old_stdout = sys.stdout
                sys.stdout = buffer = StringIO()

            # Pass content to command if it accepts it
            if cmd == "cat":
                self.commands[cmd](args, content=content)
            else:
                self.commands[cmd](args)

            if capture_output:
                sys.stdout = old_stdout
                return buffer.getvalue().strip()

        except ValueError as e:
            msg = f"[red]Parsing error:[/red] {e}"
            if capture_output:
                return msg
            self.console.print(msg)
        except Exception as e:
            msg = f"[red]Error executing command:[/red] {e}"
            if capture_output:
                return msg
            self.console.print(msg)

