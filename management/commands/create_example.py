"""
Django management command.
https://docs.djangoproject.com/en/4.0/howto/custom-management-commands/.
"""
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Django management command."""

    help = ""

    def add_arguments(self, parser):
        # Named (optional) arguments.
        parser.add_argument(
            "--delete",
            action="store_true",
            help="Delete example instead of creating it",
        )

    def handle(self, *args, **options):
        """Clears all caches defined in settings."""
        if options["delete"]:
            self.stdout.write("Deleted example.\n")
        else:
            self.stdout.write("Created example.\n")
