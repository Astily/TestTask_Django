from django.apps import apps
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    args = 'None'
    help = 'All models and object counts'

    def handle(self, *args, **options):
        try:
            app_models = apps.get_models()
        except:
            raise CommandError('Error getting model list')

        for model in app_models:
            cls = model.__name__
            num = model.objects.count()

            self.stdout.write('"%s": %d' % (cls, num))
