from typing import Dict, Optional
from rich.console import Console
import os
import shutil

class CommandExecutor:
    def __init__(self):
        self.console = Console()
        
    def execute(self, command: Dict):
        command_type = command.get('type')
        if command_type == 'file_operation':
            self.handle_file_operation(command)
        elif command_type == 'system_operation':
            self.handle_system_operation(command)
        else:
            self.console.print(f"[yellow]Unknown command type: {command_type}[/yellow]")
            
    def handle_file_operation(self, command: Dict):
        operation = command.get('operation')
        if operation == 'create':
            filename = command.get('filename')
            if filename:
                with open(filename, 'w') as f:
                    pass
                self.console.print(f"[green]Created file: {filename}[/green]")
        elif operation == 'list':
            path = command.get('path', '.')
            files = os.listdir(path)
            for file in files:
                self.console.print(file)
        
    def handle_system_operation(self, command: Dict):
        operation = command.get('operation')
        if operation == 'pwd':
            self.console.print(os.getcwd())
        elif operation == 'ls':
            files = os.listdir('.')
            for file in files:
                self.console.print(file)