"""Print hello custom django command."""
from django.core.management.base import BaseCommand, CommandParser


class Command(BaseCommand):
    """The django custom command to print hello world."""
    help = "Print hello world with optional name."

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument("name", nargs="?", type=str, help="The name of the user.")
        parser.add_argument("--kenobi", action="store_true", help="Hello there instead.")

    def handle(self, *args, **options) -> None:
        name: str = options["name"]
        kenobi: bool = options["kenobi"]

        if kenobi:
            if name:
                self.stdout.write(f"Hello there, {name}!")
            else:
                self.stdout.write("Hello there!")
        else:
            if name:
                self.stdout.write(f"Hello {name}!")
            else:
                self.stdout.write("Hello World!")
