# System CLI Tool

A modern command-line interface tool that provides system monitoring capabilities and file operations with natural language processing support. This tool allows users to interact with their system using plain English commands instead of remembering specific syntax.

## Features

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

## Usage

The tool accepts natural language commands. Here are some examples:

### System Commands
```bash
show system info
display memory usage
show disk space
show network info
show processes
```

### File Operations
```bash
create file example.txt
read example.txt
move file1.txt to folder/file2.txt
copy source.txt to backup/source.txt
delete oldfile.txt
```

### Directory Operations
```bash
where am i
current location
```

## Example Output

When you run system information commands, you'll get nicely formatted tables like this:

```
┏━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Property  ┃ Value                  ┃
┡━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━┩
│ OS        │ Windows                │
│ Version   │ 10.0.19045            │
│ Machine   │ AMD64                  │
│ Processor │ Intel64 Family 6       │
└───────────┴────────────────────────┘
```

## Requirements

- Python 3.6+
- All dependencies are listed in requirements.txt

## Project Structure

```
NEURALSHELL/
├── core/                   # Core functionality
│   ├── __pycache__/
│   ├── __init__.py        # Package initializer
│   ├── commands.py        # Command definitions
│   ├── llm.py            # Language model integration
│   ├── local_parser.py   # Command parsing logic
│   ├── system_utils.py   # System utility functions
│   └── terminal.py       # Terminal interface
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

## Contact

Your Name - [@g.hvr](https://www.instagram.com/g.hvr/)

Project Link: [https://github.com/itsgreddy/NeuralShell.git](https://github.com/itsgreddy/NeuralShell.git)