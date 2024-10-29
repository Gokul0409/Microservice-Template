import toml
from box import Box
from pathlib import Path


def read_toml(toml_path: Path) -> Box:

    """
    read_toml : Used to parse Toml file to python-box

    Args:
        toml_path (Path): Path to the configuration TOML

    Raises:
        FileNotFoundError: Raise FileNotFoundError if given path is invalid.

    Returns:
        Box : It return python-box after successful parsing
    """
    if isinstance(toml_path, Path):
        try:
            with open(toml_path, 'r') as f:
                config = toml.load(f)
            return Box(**config)

        except Exception as e:
            print(e)
            raise Exception("Unable to parse the toml")
    else:
        raise FileNotFoundError
