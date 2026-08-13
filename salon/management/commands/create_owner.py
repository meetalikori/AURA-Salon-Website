import os

from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model


class Command(BaseCommand):
    help = "Create the AURA salon owner account if it does not exist."

    def handle(self, *args, **options):
        User = get_user_model()

        username = os.environ.get("OWNER_USERNAME")
        email = os.environ.get("OWNER_EMAIL")
        password = os.environ.get("OWNER_PASSWORD")

        if not username or not email or not password:
            self.stdout.write(
                self.style.WARNING(
                    "Owner account variables are not configured."
                )
            )
            return

        if User.objects.filter(username=username).exists():
            self.stdout.write(
                self.style.SUCCESS(
                    f"Owner account '{username}' already exists."
                )
            )
            return

        User.objects.create_superuser(
            username=username,
            email=email,
            password=password,
        )

        self.stdout.write(
            self.style.SUCCESS(
                f"Owner account '{username}' created successfully."
            )
        )