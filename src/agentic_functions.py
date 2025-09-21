# functions.py

FUNCTION_DEFINITIONS = [
    {
        "name": "list_directory",
        "description": "List files and directories. Works like the 'ls' command.",
        "parameters": {
            "type": "object",
            "properties": {
                "path": {
                    "type": "string",
                    "description": "Path to list. If None, defaults to the current working directory."
                },
            },
            "required": []
        }
    },
    {
        "name": "print_working_directory",
        "description": "Show the absolute path of the current working directory (like 'pwd').",
        "parameters": {"type": "object", "properties": {}, "required": []}
    },
    {
        "name": "change_directory",
        "description": "Change the current working directory (like 'cd').",
        "parameters": {
            "type": "object",
            "properties": {
                "path": {
                    "type": "string",
                    "description": "Path to change into. Can be absolute or relative."
                }
            },
            "required": ["path"]
        }
    },
    {
        "name": "make_directory",
        "description": "Create a new directory (like 'mkdir').",
        "parameters": {
            "type": "object",
            "properties": {
                "path": {"type": "string", "description": "The directory path to create."}
            },
            "required": ["path"]
        }
    },
    {
        "name": "move_path",
        "description": "Move or rename a file or directory (like 'mv').",
        "parameters": {
            "type": "object",
            "properties": {
                "source": {
                    "type": "string",
                    "description": "Path of the file or directory to move/rename."
                },
                "destination": {
                    "type": "string",
                    "description": "Target path or new name for the file/directory."
                }
            },
            "required": ["source", "destination"]
        }
    },
    {
        "name": "cat_file",
        "description": "Read file contents, concatenate multiple files, or create/write to a file (like 'cat').",
        "parameters": {
            "type": "object",
            "properties": {
                "files": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "List of source files to read/concatenate. Optional if creating a new file."
                },
                "target": {
                    "type": "string",
                    "description": "If provided, write/append to this target file instead of just printing."
                },
                "mode": {
                    "type": "string",
                    "enum": ["read", "write", "append"],
                    "description": "read = show file contents, write = overwrite target, append = append to target."
                },
                "content": {
                    "type": "string",
                    "description": "If writing/appending, this is the content to put into the file. Optional if interactive mode is allowed."
                }
            },
            "required": ["mode"]
        }
    },
    {
        "name": "remove_path",
        "description": "Remove a file or directory (like 'rm').",
        "parameters": {
            "type": "object",
            "properties": {
                "path": {"type": "string", "description": "The file or directory path to remove."}
            },
            "required": ["path"]
        }
    },
    {
        "name": "show_cpu",
        "description": "Show CPU usage percentage (like 'cpu').",
        "parameters": {"type": "object", "properties": {}, "required": []}
    },
    {
        "name": "show_memory",
        "description": "Show memory usage details (like 'mem').",
        "parameters": {"type": "object", "properties": {}, "required": []}
    },
    {
        "name": "list_processes",
        "description": "List running processes (like 'processes').",
        "parameters": {"type": "object", "properties": {}, "required": []}
    },
    {
        "name": "show_help",
        "description": "Show the available commands table (like 'help').",
        "parameters": {"type": "object", "properties": {}, "required": []}
    },
    {
        "name": "exit_terminal",
        "description": "Exit the PyTerminal (like 'exit' or 'quit').",
        "parameters": {"type": "object", "properties": {}, "required": []}
    }
]
