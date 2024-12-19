import re
from typing import Dict, Optional
from datetime import datetime

class CommandParser:
    def __init__(self):
        self.command_history = []
        
    def parse_command(self, command: str) -> dict:
        """Enhanced natural language command parser with semantic understanding"""
        command = command.lower().strip()
        
        # System commands - with more variations
        if any(word in command for word in ['show', 'display', 'get', 'tell', 'what']):
            if any(x in command for x in ['system info', 'system information', 'about system', 'system details']):
                return {'type': 'system_operation', 'operation': 'system_info'}
            elif any(x in command for x in ['memory', 'ram', 'memory usage']):
                return {'type': 'system_operation', 'operation': 'memory'}
            elif any(x in command for x in ['disk', 'storage', 'space']):
                return {'type': 'system_operation', 'operation': 'disk'}
            elif any(x in command for x in ['network', 'internet', 'connection']):
                return {'type': 'system_operation', 'operation': 'network'}
            elif any(x in command for x in ['process', 'running', 'tasks']):
                return {'type': 'system_operation', 'operation': 'process'}
        
        # File operations with flexible matching
        # Move operation
        if any(word in command for word in ['move', 'mv', 'transfer', 'relocate']):
            parts = command.split()
            try:
                # Find source and destination
                if 'to' in parts:
                    to_index = parts.index('to')
                    # Look for the source file before 'to'
                    source = None
                    for i in range(to_index-1, -1, -1):
                        if parts[i].endswith(('.txt', '.doc', '.pdf')) or '.' in parts[i]:
                            source = parts[i]
                            break
                    # Look for the destination after 'to'
                    destination = None
                    for i in range(to_index+1, len(parts)):
                        if parts[i].endswith(('.txt', '.doc', '.pdf')) or '.' in parts[i] or '/' in parts[i]:
                            destination = parts[i]
                            break
                    
                    if source and destination:
                        return {
                            'type': 'file_operation',
                            'operation': 'move',
                            'source': source,
                            'destination': destination
                        }
            except:
                pass

        # Copy operation
        if any(word in command for word in ['copy', 'cp', 'duplicate']):
            parts = command.split()
            try:
                if 'to' in parts:
                    to_index = parts.index('to')
                    # Similar logic as move
                    source = None
                    for i in range(to_index-1, -1, -1):
                        if parts[i].endswith(('.txt', '.doc', '.pdf')) or '.' in parts[i]:
                            source = parts[i]
                            break
                    destination = None
                    for i in range(to_index+1, len(parts)):
                        if parts[i].endswith(('.txt', '.doc', '.pdf')) or '.' in parts[i] or '/' in parts[i]:
                            destination = parts[i]
                            break
                    
                    if source and destination:
                        return {
                            'type': 'file_operation',
                            'operation': 'copy',
                            'source': source,
                            'destination': destination
                        }
            except:
                pass

        # Existing file operations with more flexible matching
        if any(x in command for x in ['create', 'make', 'new']) and any(x in command for x in ['file', 'document']):
            parts = command.split()
            for part in parts:
                if '.' in part:
                    return {'type': 'file_operation', 'operation': 'create', 'filename': part}
        
        elif any(x in command for x in ['read', 'open', 'show content', 'display content', 'what is in']):
            parts = command.split()
            for part in parts:
                if '.' in part:
                    return {'type': 'file_operation', 'operation': 'read', 'filename': part}
        
        elif any(x in command for x in ['delete', 'remove', 'del', 'rm']):
            parts = command.split()
            for part in parts:
                if '.' in part:
                    return {'type': 'file_operation', 'operation': 'delete', 'filename': part}
                    
        # Directory operations with more variations
        if any(x in command for x in ['where am i', 'current location', 'pwd', 'current directory', 'present directory']):
            return {'type': 'directory_operation', 'operation': 'pwd'}
            
        return None