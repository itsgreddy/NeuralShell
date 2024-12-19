from core.terminal import TerrAI
import os
from dotenv import load_dotenv

def main():
    load_dotenv()
    terminal = TerrAI()
    terminal.cmdloop()

if __name__ == "__main__":
    main()