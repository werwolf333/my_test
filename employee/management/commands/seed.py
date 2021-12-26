from django.contrib.auth.models import User, Group
from django.core.management.base import BaseCommand
from django_seed import Seed
from faker import Faker

from employee.models import InfoPaidSalary, Employee


class Command(BaseCommand):

    help = "This command generated users"

    def add_arguments(self, parser):

        parser.add_argument(
            "--mode", default="", help="mode"
        )

    def handle(self, *args, **options):
        mode = options.get("mode")
        if mode != "":
            if mode == "drop":
                InfoPaidSalary.objects.all().delete()
                Employee.objects.all().delete()
                User.objects.all().delete()
                Group.objects.all().delete()
                self.stdout.write(self.style.SUCCESS("delete all rows!"))

            if mode == "add":
                seeder = Seed.seeder()
                seeder.add_entity(User, 1, {"is_staff": True, "is_superuser": True,
                                            "password": "pbkdf2_sha256$320000$aoMRtNadLK6f8RLcNGXB0W$5dJU5VimyhYvVGxm0/TcWkCDjj1mNrRAkp1SEgmvRBQ=",
                                            "username": "werwolf"
                                            })
                seeder.add_entity(User, 28, {"is_staff": True, "is_superuser": False})
                seeder.add_entity(Employee, 29)
                seeder.add_entity(InfoPaidSalary, 300)
                seeder.execute()
                self.stdout.write(self.style.SUCCESS("add all rows!"))
