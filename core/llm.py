from openai import OpenAI
import os
from typing import Dict, Optional
from dotenv import load_dotenv

def process_with_llm(command: str) -> Optional[Dict]:
    try:
        load_dotenv()
        client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
        
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": """You are a terminal assistant. Convert natural language commands into structured actions.
                For file operations, return JSON in this format:
                {
                    "type": "file_operation",
                    "operation": "create|list|delete|move",
                    "filename": "example.txt",
                    "path": "optional_path"
                }
                """},
                {"role": "user", "content": command}
            ]
        )
        
        return parse_response(response)
    except Exception as e:
        print(f"Error processing command with AI: {str(e)}")
        return None

def parse_response(response) -> Dict:
    try:
        content = response.choices[0].message.content
        # Basic command parsing - you can enhance this
        if 'create' in content.lower():
            return {
                'type': 'file_operation',
                'operation': 'create',
                'filename': 'test.txt'  # You can make this more sophisticated
            }
        elif 'list' in content.lower():
            return {
                'type': 'file_operation',
                'operation': 'list',
                'path': '.'
            }
        return {'type': 'command', 'action': content}
    except Exception as e:
        print(f"Error parsing AI response: {str(e)}")
        return None
