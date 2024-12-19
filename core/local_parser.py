import re
from typing import Dict, Optional

class CommandParser:
    def parse_command(self, command: str) -> Optional[Dict]:
        """Parse natural language commands without using an API"""
        command = command.lower().strip()
        
        # File creation patterns
        create_patterns = [
            r"(?:create|make|new).*?(?:file|document).*?(?:called|named)?\s*['']?([a-zA-Z0-9._-]+)['']?",
            r"(?:create|make|new).*?['']?([a-zA-Z0-9._-]+)['']?"
        ]
        
        # List files patterns
        list_patterns = [
            r"(?:list|show|display).*?(?:files|contents)",
            r"(?:ls|dir)"
        ]
        
        # Delete patterns
        delete_patterns = [
            r"(?:delete|remove|del).*?(?:file)?\s*['']?([a-zA-Z0-9._-]+)['']?",
        ]
        
        # Move patterns
        move_patterns = [
            r"(?:move|mv).*?['']?([a-zA-Z0-9._-]+)['']?.*?(?:to|into).*?['']?([a-zA-Z0-9._/-]+)['']?"
        ]
        
        # Check for create command
        for pattern in create_patterns:
            if match := re.search(pattern, command):
                filename = match.group(1) if match.group(1) else "newfile.txt"
                return {
                    'type': 'file_operation',
                    'operation': 'create',
                    'filename': filename
                }
        
        # Check for list command
        for pattern in list_patterns:
            if re.search(pattern, command):
                return {
                    'type': 'file_operation',
                    'operation': 'list',
                    'path': '.'
                }
        
        # Check for delete command
        for pattern in delete_patterns:
            if match := re.search(pattern, command):
                return {
                    'type': 'file_operation',
                    'operation': 'delete',
                    'filename': match.group(1)
                }
        
        # Check for move command
        for pattern in move_patterns:
            if match := re.search(pattern, command):
                return {
                    'type': 'file_operation',
                    'operation': 'move',
                    'source': match.group(1),
                    'destination': match.group(2)
                }
        
        return None
