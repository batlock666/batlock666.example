# NOQA: D100

import argparse

from . import functions


def hello():
    """Script ``hello``.
    """
    # Define the arguments
    parser = argparse.ArgumentParser(description="Print a hello message.")
    parser.add_argument(
        "name",
        type=str,
        nargs="?",
        default=None,
        help="a name",
    )

    # Parse the arguments
    args = parser.parse_args()

    # Calculate and print the result
    print(functions.hello(args.name))
