import cmd
from rich.console import Console
from rich.layout import Layout
from rich.panel import Panel
from typing import Dict, Optional
from .llm import process_with_llm
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
    
