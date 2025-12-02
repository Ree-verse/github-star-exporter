"""
github-star-exporter | https://github.com/ree-verse/github-star-exporter

Copyright © 2025 Ree-verse. All rights reserved.
Licensed under the MIT License. See LICENSE in the project root for license information.
"""

import sys

from colorama import Fore

from . import __version__, arg_parser, colorize, export_starred_repos


def main() -> int:
    args = arg_parser()

    if args.version:
        print(f"github-star-exporter version {__version__}")
        return 0

    if not args.token:
        print(
            colorize(
                "Error: TOKEN argument is required (unless using --version)",
                Fore.RED,
            )
        )
        return 1

    # for name in ["token", "user", "output"]:
    #     arg = getattr(args, name)
    #     if arg is not None and not isinstance(arg, str):
    #         print(
    #             colorize(
    #                 f"{name.upper()} argument must be a str{', or None' if name == 'user' else ''}, not '{type(arg).__name__}'",
    #                 Fore.RED,
    #             )
    #         )
    #         return(1)

    try:
        export_starred_repos(
            token=args.token,
            target_user=args.user,
            output_path=args.output,
        )
    except Exception as e:
        print(colorize(f"Unexpected error:\n{e}", Fore.RED))
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
