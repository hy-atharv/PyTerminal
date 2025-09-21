import os
import shutil
from rich.console import Console
from rich.table import Table

class FileSystemCommands:
    def __init__(self, console: Console):
        self.console = console
        self.current_dir = os.getcwd()

    def _resolve_path(self, path: str) -> str:
        return os.path.abspath(os.path.join(self.current_dir, path))
    
    def cat(self, args, content: str | None = None):
        """
        Basic cat command.
        - Display single/multiple files
        - Concatenate files
        - > overwrite
        - >> append
        - Interactive mode for creating new files
        - Optional content parameter for direct write/append
        """
        if not args and content is None:
            self.console.print("[red]cat: missing arguments[/red]")
            return

        # Detect redirection (> or >>)
        if ">" in args or ">>" in args:
            self._handle_redirection(args, content)
            return

        # No redirection: just display files
        for file in args:
            file_path = self._resolve_path(file)
            if not os.path.exists(file_path):
                self.console.print(f"[red]cat: {file} does not exist[/red]")
                continue
            try:
                with open(file_path, "r") as f:
                    self.console.print(f.read(), end="")
            except Exception as e:
                self.console.print(f"[red]Error reading {file}: {e}[/red]")

    def _handle_redirection(self, args, content: str | None = None):
        """Handle cat > file.txt, cat >> file.txt, interactive mode, and direct content writing."""
        try:
            if ">>" in args:
                idx = args.index(">>")
                files = args[:idx]
                target = args[idx + 1]
                mode = "a"
            else:
                idx = args.index(">")
                files = args[:idx]
                target = args[idx + 1]
                mode = "w"
        except IndexError:
            self.console.print("[red]cat: invalid redirection usage[/red]")
            return

        target_path = self._resolve_path(target)

        # If content is provided, write/append directly
        if content is not None:
            try:
                with open(target_path, mode) as f:
                    f.write(content + "\n")
                action = "appended to" if mode == "a" else "written to"
                self.console.print(f"[green]cat: content {action} {target}[/green]")
            except Exception as e:
                self.console.print(f"[red]Error writing to {target}: {e}[/red]")
            return

        # Interactive mode: no files, write mode
        if not files and mode == "w":
            self.console.print(
                f"[bold yellow]Enter content for {target} (Ctrl+D or Ctrl+Z+Enter to save):[/bold yellow]"
            )
            lines = []
            try:
                while True:
                    line = input()
                    lines.append(line)
            except (EOFError, KeyboardInterrupt):
                pass

            try:
                cleaned_lines = [l.replace("\x1a", "").strip() for l in lines if l.strip() != ""]
                with open(target_path, "w") as f:
                    f.write("\n".join(cleaned_lines) + "\n")
                self.console.print(f"\n[green]cat: created {target}[/green]")
            except Exception as e:
                self.console.print(f"[red]Error writing to {target}: {e}[/red]")
            return

        # Read from source files and write to target
        output_data = []
        for file in files:
            file_path = self._resolve_path(file)
            if not os.path.exists(file_path):
                self.console.print(f"[red]cat: {file} does not exist[/red]")
                continue
            try:
                with open(file_path, "r") as f:
                    output_data.append(f.read())
            except Exception as e:
                self.console.print(f"[red]Error reading {file}: {e}[/red]")

        try:
            with open(target_path, mode) as f:
                f.write("\n".join(output_data))
            self.console.print(f"[green]cat: written to {target}[/green]")
        except Exception as e:
            self.console.print(f"[red]Error writing to {target}: {e}[/red]")


    def ls(self, args):
        path = self.current_dir if not args else self._resolve_path(args[0])
        try:
            items = os.listdir(path)
            table = Table()
            table.add_column(f"{os.path.basename(path)}", style="cyan")
            for item in items:
                table.add_row(item)
            self.console.print(table)
        except FileNotFoundError:
            self.console.print(f"[red]No such directory:[/red] {path}")

    def pwd(self, args):
        self.console.print(f"[bold yellow]{self.current_dir}[/bold yellow]")

    def cd(self, args):
        if not args:
            self.console.print("[red]cd: missing argument[/red]")
            return
        new_path = self._resolve_path(args[0])
        if os.path.isdir(new_path):
            self.current_dir = new_path
            os.chdir(new_path)
        else:
            self.console.print(f"[red]cd: no such directory:[/red] {args[0]}")

    def mkdir(self, args):
        if not args:
            self.console.print("[red]mkdir: missing directory name[/red]")
            return
        path = self._resolve_path(args[0])
        try:
            os.makedirs(path, exist_ok=False)
            self.console.print(f"[green]Directory created:[/green] {path}")
        except FileExistsError:
            self.console.print(f"[red]mkdir: cannot create directory '{args[0]}': File exists[/red]")
    
    def mv(self, args):
        """
        Move or rename a file/directory.
        Usage: mv source_path destination_path
        """
        if len(args) < 2:
            self.console.print("[red]mv: missing source or destination[/red]")
            return

        src = self._resolve_path(args[0])
        dest = self._resolve_path(args[1])

        if not os.path.exists(src):
            self.console.print(f"[red]mv: source does not exist:[/red] {args[0]}")
            return

        try:
            shutil.move(src, dest)
            self.console.print(f"[green]Moved/Renamed:[/green] {src} → {dest}")
        except Exception as e:
            self.console.print(f"[red]mv: error moving '{args[0]}' to '{args[1]}': {e}[/red]")

    def rm(self, args):
        if not args:
            self.console.print("[red]rm: missing file/directory name[/red]")
            return
        path = self._resolve_path(args[0])
        if os.path.isfile(path):
            os.remove(path)
            self.console.print(f"[green]Removed file:[/green] {path}")
        elif os.path.isdir(path):
            shutil.rmtree(path)
            self.console.print(f"[green]Removed directory:[/green] {path}")
        else:
            self.console.print(f"[red]rm: cannot remove '{args[0]}': No such file or directory[/red]")
