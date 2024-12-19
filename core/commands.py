from typing import Dict, Optional
from rich.console import Console
import os
import shutil
from typing import Dict, Optional
from rich.console import Console
from rich.table import Table
import os
import shutil
import humanize
from datetime import datetime
from .system_utils import SystemUtils

# class CommandExecutor:
#     def __init__(self):
#         self.console = Console()
        
#     def execute(self, command: Dict):
#         command_type = command.get('type')
#         if command_type == 'file_operation':
#             self.handle_file_operation(command)
#         elif command_type == 'system_operation':
#             self.handle_system_operation(command)
#         else:
#             self.console.print(f"[yellow]Unknown command type: {command_type}[/yellow]")
            
#     def handle_file_operation(self, command: Dict):
#         operation = command.get('operation')
#         if operation == 'create':
#             filename = command.get('filename')
#             if filename:
#                 with open(filename, 'w') as f:
#                     pass
#                 self.console.print(f"[green]Created file: {filename}[/green]")
#         elif operation == 'list':
#             path = command.get('path', '.')
#             files = os.listdir(path)
#             for file in files:
#                 self.console.print(file)
        
#     def handle_system_operation(self, command: Dict):
#         operation = command.get('operation')
#         if operation == 'pwd':
#             self.console.print(os.getcwd())
#         elif operation == 'ls':
#             files = os.listdir('.')
#             for file in files:
#                 self.console.print(file)

from typing import Dict, Optional
from rich.console import Console
from rich.table import Table
import os
import shutil
import humanize
from datetime import datetime
from .system_utils import SystemUtils

class CommandExecutor:
    def __init__(self):
        self.console = Console()
        self.system_utils = SystemUtils()
        
    def execute(self, command: Dict):
        """Execute the parsed command"""
        if not command:
            self.console.print("[yellow]Could not understand command.[/yellow]")
            return
            
        try:
            command_type = command.get('type')
            if command_type == 'file_operation':
                self.handle_file_operation(command)
            elif command_type == 'system_operation':
                self.handle_system_operation(command)
            elif command_type == 'directory_operation':
                self.handle_directory_operation(command)
            else:
                self.console.print(f"[yellow]Unknown command type: {command_type}[/yellow]")
        except Exception as e:
            self.console.print(f"[red]Error executing command: {str(e)}[/red]")
            
    def handle_file_operation(self, command: Dict):
        """Handle file-related operations"""
        operation = command.get('operation')
        filename = command.get('filename')
        
        if not filename:
            self.console.print("[red]No filename provided[/red]")
            return
            
        if operation == 'create':
            try:
                with open(filename, 'w') as f:
                    pass
                self.console.print(f"[green]Created file: {filename}[/green]")
            except Exception as e:
                self.console.print(f"[red]Error creating file: {str(e)}[/red]")
                
        elif operation == 'read':
            try:
                with open(filename, 'r') as f:
                    content = f.read()
                self.console.print(f"\n[blue]Content of {filename}:[/blue]")
                self.console.print(content if content else "[yellow]<empty file>[/yellow]")
            except Exception as e:
                self.console.print(f"[red]Error reading file: {str(e)}[/red]")
                
        elif operation == 'delete':
            try:
                os.remove(filename)
                self.console.print(f"[green]Deleted file: {filename}[/green]")
            except Exception as e:
                self.console.print(f"[red]Error deleting file: {str(e)}[/red]")

    def handle_system_operation(self, command: Dict):
        """Handle system-related operations"""
        operation = command.get('operation')
        
        if operation == 'system_info':
            info = self.system_utils.get_system_info()
            table = Table(title="System Information")
            table.add_column("Property", style="cyan")
            table.add_column("Value", style="magenta")
            
            for key, value in info.items():
                table.add_row(key.replace('_', ' ').title(), str(value))
            self.console.print(table)
            
        elif operation == 'memory':
            info = self.system_utils.get_memory_info()
            table = Table(title="Memory Information")
            table.add_column("Property", style="cyan")
            table.add_column("Value", style="magenta")
            
            for key, value in info.items():
                if key in ['total', 'available', 'used', 'free']:
                    value = humanize.naturalsize(value)
                elif key == 'percent':
                    value = f"{value}%"
                table.add_row(key.replace('_', ' ').title(), str(value))
            self.console.print(table)
            
        elif operation == 'disk':
            info = self.system_utils.get_disk_info()
            table = Table(title="Disk Information")
            table.add_column("Property", style="cyan")
            table.add_column("Value", style="magenta")
            
            for key, value in info.items():
                if key in ['total', 'used', 'free']:
                    value = humanize.naturalsize(value)
                elif key == 'percent':
                    value = f"{value}%"
                table.add_row(key.replace('_', ' ').title(), str(value))
            self.console.print(table)

    def handle_directory_operation(self, command: Dict):
        """Handle directory-related operations"""
        operation = command.get('operation')
        
        if operation == 'pwd':
            try:
                current_dir = os.getcwd()
                self.console.print(f"[blue]Current directory: {current_dir}[/blue]")
            except Exception as e:
                self.console.print(f"[red]Error getting current directory: {str(e)}[/red]")
                
        elif operation == 'cd':
            path = command.get('path')
            try:
                os.chdir(path)
                self.console.print(f"[green]Changed directory to: {path}[/green]")
            except Exception as e:
                self.console.print(f"[red]Error changing directory: {str(e)}[/red]")