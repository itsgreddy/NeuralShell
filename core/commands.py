from typing import Dict, Optional
from rich.console import Console
from rich.table import Table
import os
import shutil
import humanize
import socket
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
            
        elif operation == 'network':
            info = self.system_utils.get_network_info()
            table = Table(title="Network Information")
            table.add_column("Property", style="cyan")
            table.add_column("Value", style="magenta")
            
            # Handle basic network info
            table.add_row("Hostname", info['hostname'])
            table.add_row("IP Address", info['ip_address'])
            
            # Handle network interfaces
            for interface, addrs in info['interfaces'].items():
                for addr in addrs:
                    if addr.family == socket.AF_INET:  # IPv4
                        table.add_row(f"Interface {interface}", f"IPv4: {addr.address}")
                    elif addr.family == socket.AF_INET6:  # IPv6
                        table.add_row(f"Interface {interface}", f"IPv6: {addr.address}")
            
            self.console.print(table)
            
        elif operation == 'processes':
            processes = self.system_utils.get_process_info()
            table = Table(title="Running Processes")
            table.add_column("PID", style="cyan")
            table.add_column("Name", style="magenta")
            table.add_column("CPU %", style="green")
            table.add_column("Memory %", style="yellow")
            
            # Sort processes by CPU usage and show top 10
            sorted_processes = sorted(processes, key=lambda x: x.get('cpu_percent', 0), reverse=True)[:10]
            
            for proc in sorted_processes:
                table.add_row(
                    str(proc.get('pid', 'N/A')),
                    str(proc.get('name', 'N/A')),
                    f"{proc.get('cpu_percent', 0):.1f}%",
                    f"{proc.get('memory_percent', 0):.1f}%"
                )
            
            self.console.print(table)