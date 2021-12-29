from django.contrib.auth.models import User, Group
from django.core.management.base import BaseCommand
from django_seed import Seed


from employee.models import Salary, Employee


class Command(BaseCommand):

    help = "This command generated users"

    def add_arguments(self, parser):

        parser.add_argument(
            "--mode", default="", help="mode"
        )

    def handle(self, *args, **options):
        mode = options.get("mode")
        if mode == "drop":
            Salary.objects.all().delete()
            Employee.objects.all().delete()
            User.objects.all().delete()
            Group.objects.all().delete()
            self.stdout.write(self.style.SUCCESS("delete all rows!"))

        if mode == "add":
            seeder = Seed.seeder()
            seeder.add_entity(User, 30, {"is_staff": False, "is_superuser": False})
            seeder.add_entity(Employee, 30)
            seeder.add_entity(Salary, 300)
            seeder.execute()
            self.stdout.write(self.style.SUCCESS("add all rows!"))
