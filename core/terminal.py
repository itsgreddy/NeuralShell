import cmd
from rich.console import Console
from rich.layout import Layout
from rich.panel import Panel
from rich.text import Text
from rich.table import Table
from typing import Dict, Optional
from .llm import process_with_llm
from .local_parser import CommandParser
from .commands import CommandExecutor

class TerrAI(cmd.Cmd):
    intro = 'Welcome to TerrAI - Your AI-powered terminal assistant. Type "help" or "?" for commands.\n'
    prompt = '\033[92m❯\033[0m '

    def __init__(self):
        super().__init__()
        self.console = Console()
        self.layout = Layout()
        self.command_executor = CommandExecutor()
        self.setup_ui()
        
    def setup_ui(self):
        self.layout.split(
            Layout(name="header", size=3),
            Layout(name="main"),
            Layout(name="footer", size=3)
        )
        self.update_display()
        
    def update_display(self):
        self.layout["header"].update(Panel("TerrAI Terminal", style="bold blue"))
        
    def default(self, line):
        try:
            # Process command with LLM
            parsed_command = process_with_llm(line)
            if parsed_command:
                self.command_executor.execute(parsed_command)
            else:
                self.console.print("[yellow]Could not understand command[/yellow]")
        except Exception as e:
            self.console.print(f"[red]Error: {str(e)}[/red]")

    def do_exit(self, arg):
        """Exit TerrAI"""
        print("Goodbye!")
        return True

# class TerrAI(cmd.Cmd):
#     intro = '''
# [blue]Welcome to TerrAI - Your intelligent terminal assistant[/blue]
# [green]Type "help" or "?" to list commands.[/green]
# '''
#     prompt = '\033[92m❯\033[0m '

#     def __init__(self):
#         super().__init__()
#         self.console = Console()
#         self.layout = Layout()
#         self.command_executor = CommandExecutor()
#         self.parser = CommandParser()
#         self.setup_ui()
        
#     def setup_ui(self):
#         """Initialize the terminal UI layout"""
#         self.layout.split(
#             Layout(name="header", size=3),
#             Layout(name="main"),
#             Layout(name="footer", size=3)
#         )
#         self.update_display()
        
#     def update_display(self):
#         """Update the terminal display"""
#         self.layout["header"].update(
#             Panel(
#                 Text("TerrAI Terminal", justify="center", style="bold blue"),
#                 border_style="blue"
#             )
#         )
        
#     def default(self, line):
#         """Handle any command not specifically defined"""
#         try:
#             parsed_command = self.parser.parse_command(line)
#             if parsed_command:
#                 self.command_executor.execute(parsed_command)
#             else:
#                 self.show_command_suggestions()
#         except Exception as e:
#             self.console.print(f"[red]Error: {str(e)}[/red]")

#     def show_command_suggestions(self):
#         """Show helpful command suggestions"""
#         table = Table(title="Command Examples", border_style="yellow")
#         table.add_column("Category", style="cyan", no_wrap=True)
#         table.add_column("Examples", style="green")

#         table.add_row(
#             "File Operations",
#             "- create file example.txt\n"
#             "- read file test.txt\n"
#             "- delete data.txt\n"
#             "- move source.txt to dest.txt\n"
#             "- copy file.txt to backup.txt\n"
#             "- search for pattern"
#         )

#         table.add_row(
#             "Directory Operations",
#             "- where am i (pwd)\n"
#             "- change directory to path\n"
#             "- create directory newdir\n"
#             "- remove directory olddir"
#         )

#         table.add_row(
#             "System Operations",
#             "- show system info\n"
#             "- show memory usage\n"
#             "- show disk space\n"
#             "- show network info\n"
#             "- show processes"
#         )

#         self.console.print(table)

#     def do_help(self, arg):
#         """Show detailed help message"""
#         if not arg:
#             help_table = Table(title="TerrAI Help", border_style="blue")
#             help_table.add_column("Category", style="cyan", no_wrap=True)
#             help_table.add_column("Description", style="green")
#             help_table.add_column("Examples", style="yellow")

#             help_table.add_row(
#                 "File Operations",
#                 "Create, read, delete, move, copy files",
#                 "create file test.txt\nread file.txt\ndelete old.txt"
#             )

#             help_table.add_row(
#                 "Directory Operations",
#                 "Navigate and manage directories",
#                 "where am i\nchange directory to docs\ncreate directory new"
#             )

#             help_table.add_row(
#                 "System Operations",
#                 "View system information and status",
#                 "show system info\nshow memory usage\nshow processes"
#             )

#             help_table.add_row(
#                 "Search",
#                 "Search for files and content",
#                 "search for example\nfind file test.txt"
#             )

#             self.console.print(help_table)
#             self.console.print("\n[blue]For detailed help on a specific category, type:[/blue]")
#             self.console.print("help files  - File operation details")
#             self.console.print("help system - System operation details")
#             self.console.print("help dir    - Directory operation details")
#         else:
#             self.show_category_help(arg.lower())

#     def show_category_help(self, category):
#         """Show help for a specific category"""
#         if category in ['files', 'file', 'f']:
#             table = Table(title="File Operations Help", border_style="blue")
#             table.add_column("Command", style="cyan")
#             table.add_column("Description", style="green")
#             table.add_column("Examples", style="yellow")
            
#             table.add_row(
#                 "create",
#                 "Create a new file",
#                 "create file test.txt\nmake file data.txt"
#             )
#             table.add_row(
#                 "read",
#                 "Display file contents",
#                 "read file.txt\nshow content of doc.txt"
#             )
#             table.add_row(
#                 "delete",
#                 "Remove a file",
#                 "delete old.txt\nremove temp.txt"
#             )
#             table.add_row(
#                 "move/copy",
#                 "Move or copy files",
#                 "move source.txt to dest.txt\ncopy file.txt to backup.txt"
#             )
            
#             self.console.print(table)
            
#         elif category in ['system', 'sys', 's']:
#             table = Table(title="System Operations Help", border_style="blue")
#             table.add_column("Command", style="cyan")
#             table.add_column("Description", style="green")
#             table.add_column("Examples", style="yellow")
            
#             table.add_row(
#                 "system info",
#                 "Show system details",
#                 "show system info\nsystem information"
#             )
#             table.add_row(
#                 "memory",
#                 "Show memory usage",
#                 "show memory usage\nmemory info"
#             )
#             table.add_row(
#                 "disk",
#                 "Show disk space",
#                 "show disk space\ndisk usage"
#             )
#             table.add_row(
#                 "network",
#                 "Show network info",
#                 "show network info\nnetwork status"
#             )
            
#             self.console.print(table)
            
#         elif category in ['dir', 'directory', 'd']:
#             table = Table(title="Directory Operations Help", border_style="blue")
#             table.add_column("Command", style="cyan")
#             table.add_column("Description", style="green")
#             table.add_column("Examples", style="yellow")
            
#             table.add_row(
#                 "pwd",
#                 "Show current directory",
#                 "where am i\ncurrent directory"
#             )
#             table.add_row(
#                 "cd",
#                 "Change directory",
#                 "change directory to docs\ngo to path"
#             )
#             table.add_row(
#                 "mkdir",
#                 "Create directory",
#                 "create directory new\nmake folder test"
#             )
#             table.add_row(
#                 "rmdir",
#                 "Remove directory",
#                 "remove directory old\ndelete folder temp"
#             )
            
#             self.console.print(table)
#         else:
#             self.console.print("[yellow]Unknown help category. Try: help files, help system, or help dir[/yellow]")

#     def do_exit(self, arg):
#         """Exit TerrAI"""
#         self.console.print("[blue]Goodbye! Thank you for using TerrAI.[/blue]")
#         return True

#     def emptyline(self):
#         """Handle empty lines"""
#         pass

#     def do_EOF(self, arg):
#         """Handle EOF (Ctrl+D/Ctrl+Z)"""
#         return self.do_exit(arg)