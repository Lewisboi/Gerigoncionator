import os
import sys
from enum import Enum

from gerigoncionator import Gerigoncionator


class Command(Enum):
    READ = 0


gerigoncio_instance = Gerigoncionator()


def gerigoncify_file(path: str) -> None:
    with open(path, "r") as boring:
        lines = boring.readlines()
    gerigoncified_lines = []
    with open(f"{os.path.basename(path)}_gerigoncified.txt", "w") as gerigoncified:
        for line in lines:
            stripped_line = line.strip()
            gerigoncified_line = gerigoncio_instance.gerigoncify(stripped_line)
            gerigoncified_lines.append(gerigoncified_line)
        gerigoncified.write("\n".join(gerigoncified_lines))


arguments = sys.argv[1:]

COMMANDS = {"-r": Command.READ, "--read": Command.READ}

match arguments:
    case [content]:
        gerigoncified = gerigoncio_instance.gerigoncify(content)
        print(gerigoncified)
    case [command, argument]:
        try:
            command_type = COMMANDS[command]
            match command_type:
                case Command.READ:
                    gerigoncify_file(argument)
        except KeyError:
            print(f"invalid command '{command}'")
    case _:
        print(f"Invalid arguments {arguments}")
