# TerrAI CLI Tool (Terminal AI)

A modern command-line interface tool that provides system monitoring capabilities and file operations with optional natural language processing support. This tool can be used either with AI-powered natural language processing (using OpenAI's API) or as a standard CLI tool with direct commands.

## Video Tutorial
Watch the project demonstration and explanation:
[![TerrAI CLI Tool Demo](https://img.youtube.com/vi/cpQYQXSoa7M/0.jpg)](https://www.youtube.com/watch?v=cpQYQXSoa7M)


## Features

- **Two Operation Modes**
  - AI-Powered Mode: Process natural language commands using OpenAI's API
  - Standard Mode: Traditional command-line interface without AI integration

- **System Monitoring**
  - System Information (OS, version, machine, processor, etc.)
  - Memory Usage Statistics
  - Disk Usage Information
  - Network Information
  - Process Monitoring (Top 10 CPU-intensive processes)

- **File Operations**
  - Create new files
  - Read file contents
  - Move files
  - Copy files
  - Delete files

- **Directory Operations**
  - Show current directory
  - Navigate directories

## Installation

1. Clone the repository:
```bash
git clone https://github.com/itsgreddy/NeuralShell.git
cd NeuralShell
```

2. Install dependencies using requirements.txt:
```bash
pip install -r requirements.txt
```

If you're a developer working on the project, here's how to create/update requirements.txt:
```bash
pip freeze > requirements.txt
```

The main dependencies are:
- psutil: For system monitoring
- rich: For terminal formatting
- humanize: For human-readable output
- openai: For AI-powered mode (optional)

## Configuration

### AI-Powered Mode Setup
1. Uncomment the AI-related sections and comment the standard-mode section in `core/commands.py` and `core/terminal.py` (marked with comments)
2. Set up your OpenAI API key:
   ```bash
   export OPENAI_API_KEY='your-api-key-here'
   ```

### Standard Mode Setup
- Leave the AI-related sections commented out in both files
- No additional configuration needed

## Usage

### AI-Powered Mode
Processes a broad spectrum of natural language inputs, allowing users to phrase commands conversationally and receive intelligent interpretations even for complex or indirect requests. The AI model will extract the relevant command from your natural speech, making interaction more flexible and intuitive.

```bash
1. I need to know how my system is doing
2. Could you tell me about the memory situation on my computer?
```

### Standard Mode
Supports basic natural language processing with a focused command set. Commands should be expressed clearly and directly relate to the tool's core functionalities (system monitoring, file operations, and directory management). While some natural language variation is supported, commands should closely align with the intended operation.

```bash
1. Show me the system information
2. Could you display memory usage
3. What is my current location
```

### Common Commands for Both Modes

#### System Commands
```bash
show system info
display memory usage
show disk space
show network info
show processes
```

#### File Operations
```bash
create file example.txt
read example.txt
move file1.txt to folder/file2.txt
copy source.txt to backup/source.txt
delete oldfile.txt
```

#### Directory Operations
```bash
where am i
current location
```

## Example Output

When you run system information commands, you'll get nicely formatted tables like this:

```
┏━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Property  ┃ Value                 ┃
┡━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━┃
│ OS        │ Windows               ┃
│ Version   │ 10.0.19045            ┃
│ Machine   │ AMD64                 ┃
│ Processor │ Intel64 Family 6      ┃
└───────────┴───────────────────────┘
```

## Requirements

- Python 3.6+
- All dependencies are listed in requirements.txt
- OpenAI API key (only for AI-powered mode)

## Project Structure

```
NEURALSHELL/
├── core/                   # Core functionality
│   ├── __pycache__/
│   ├── __init__.py        # Package initializer
│   ├── commands.py        # Command definitions (contains AI/non-AI code)
│   ├── llm.py            # Language model integration
│   ├── local_parser.py   # Command parsing logic
│   ├── system_utils.py   # System utility functions
│   └── terminal.py       # Terminal interface (contains AI/non-AI code)
├── terr/                  # Additional directory
├── .env                   # Environment variables
├── .gitignore            # Git ignore rules
├── called                # Project files
├── LICENSE               # License file
├── main.py              # Main entry point
├── README.md            # Project documentation
├── requirements.txt     # Project dependencies
└── text.red            # Additional configuration
```

## Troubleshooting

### Common Issues
1. AI Mode Issues:
   - Verify OpenAI API key is set correctly
   - Ensure AI-related code sections are uncommented
   - Check internet connectivity

2. Standard Mode Issues:
   - Verify AI-related code sections remain commented
   - Check that basic dependencies are installed

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- [psutil](https://github.com/giampaolo/psutil) for system monitoring capabilities
- [rich](https://github.com/Textualize/rich) for beautiful terminal formatting
- [humanize](https://github.com/jmoiron/humanize) for human-readable output
- [OpenAI](https://openai.com) for AI capabilities in the AI-powered mode

## Contact

Your Name - [@g.hvr](https://www.instagram.com/g.hvr/)

Project Link: [https://github.com/itsgreddy/NeuralShell.git](https://github.com/itsgreddy/NeuralShell.git)