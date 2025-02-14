"""
Load command parameters configuration.
"""

import json
import os


def load_command_params(command=None):
    """
    Loads the JSON file containing parameters for each command.
    If a command is provided, it returns only the configuration for that specific command.

    Args:
        command (str, optional): The name of the command whose parameters are to be loaded.
                                  If no command is provided, the function will return
                                  the parameters for all commands.

    Returns:
        dict: A dictionary containing the parameters for the specified command, or all commands
              if no command is given.

    Raises:
        FileNotFoundError: If the 'command_params.json' file is not found.
        json.JSONDecodeError: If there is an error decoding the JSON file.
    """
    # Directory of the script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    json_path = os.path.join(script_dir, "command_params.json")

    with open(json_path, "r", encoding="utf-8") as f:
        command_data = json.load(f)

    if command:
        # Returns the command's configuration or an empty dict if not found
        return command_data.get(command, {})
    # If no command is provided, returns the entire JSON
    return command_data
