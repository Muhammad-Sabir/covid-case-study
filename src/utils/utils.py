import json
import atexit
import logging.config
from pathlib import Path

from src.utils.constants import CONFIGS_DIR


def setup_logging():
    """
    Sets up logging configuration for the app.
    """
    config_file = CONFIGS_DIR / "logging_config.json"

    try:
        with open(config_file, "r") as file:
            config = json.load(file)
    except FileNotFoundError as e:
        raise FileNotFoundError(
            f"Logging configuration file not found: {config_file}"
        ) from e
    except json.JSONDecodeError as e:
        raise json.JSONDecodeError(
            f"Invalid JSON in logging configuration file: {config_file}", e.doc, e.pos
        )
    except Exception as e:
        raise Exception(f"Unexpected error while reading logging config: {e}") from e

    # Ensure log directories exist
    for handler in config.get("handlers", {}).values():
        filename = handler.get("filename")
        if filename:
            log_path = Path(filename)
            log_dir = log_path.parent
            log_dir.mkdir(parents=True, exist_ok=True)

    try:
        logging.config.dictConfig(config)
    except ValueError as e:
        raise ValueError(f"Invalid logging configuration: {e}") from e
    except Exception as e:
        raise Exception(f"Unexpected error while applying logging config: {e}") from e

    try:
        queue_handler = logging.getHandlerByName("queue_handler")
        if queue_handler is not None:
            listener = getattr(queue_handler, "listener", None)
            if listener is None:
                raise AttributeError(
                    "The 'queue_handler' does not have a 'listener' attribute."
                )
            listener.start()
            atexit.register(listener.stop)
    except AttributeError as e:
        raise AttributeError(
            f"Error starting or stopping the queue_handler's listener: {e}"
        ) from e
    except Exception as e:
        raise Exception(f"Unexpected error while handling queue_handler: {e}") from e
