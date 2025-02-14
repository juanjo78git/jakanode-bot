"""
Script management service
"""

import os
import subprocess

from config.logging import logger

# Get the current script's directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# Go up one level and enter the /scripts directory
SCRIPTS_DIR = os.path.abspath(os.path.join(BASE_DIR, "..", "scripts"))


def get_scripts():
    """
    Retrieves a list of executable scripts in the /scripts directory.

    Returns:
        list: A list of executable script names (without file extension).
    """
    scripts = []

    # Lists the files and filters only the executable ones
    for f in os.listdir(SCRIPTS_DIR):
        script_path = os.path.join(SCRIPTS_DIR, f)
        if os.path.isfile(script_path) and os.access(script_path, os.X_OK):
            scripts.append(f[:-3])

    logger.info("Available scripts: %s", scripts)
    return scripts


def run_script(script_name):
    """
    Executes a script if it is available in the list of executable scripts.

    Args:
        script_name (str): The name of the script to execute (without file extension).

    Returns:
        str or None: The output of the script if execution is successful, or None if the
                     script is not available. In case of errors, returns an error message.
    """
    available_scripts = get_scripts()
    if script_name not in available_scripts:
        logger.warning("Script '%s' is not available or not executable.", script_name)
        return None

    script_path = os.path.join(SCRIPTS_DIR, script_name + ".sh")

    try:
        # Copy the environment variables from the main process
        env = os.environ.copy()

        result = subprocess.run(
            [script_path], text=True, capture_output=True, check=True, env=env
        )
        output = result.stdout if result.stdout else result.stderr
        logger.info(
            "Script '%s' executed successfully. Output: %s", script_name, output.strip()
        )
        return output

    except subprocess.CalledProcessError as e:
        # Error when the script returns a non-zero exit code
        logger.error(
            "Error executing script %s: %s",
            script_name,
            e.stderr.strip() if e.stderr else e.stdout.strip(),
        )
        return _(
            f"Error executing script {script_name}: "
            f"{e.stderr.strip() if e.stderr else e.stdout.strip()}"
        )

    except FileNotFoundError:
        logger.error("Error: File %s was not found", script_name)
        return _("Command not recognized.")

    except Exception as e:  # pylint: disable=W0718
        logger.error("Unknown error executing script '%s': %s", script_name, str(e))
        return str(e)
