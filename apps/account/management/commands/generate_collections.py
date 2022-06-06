import timeit
from apps.account.models import Collection
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Creates collections.'

    def add_arguments(self, parser):
        parser.add_argument('num', nargs='+', type=int)

    def handle(self, *args, **options):
        num = options['num'][0]
        user = User.objects.get(username='alien')

        start = timeit.default_timer()

        objs = (Collection(name=i, user=user) for i in range(num))
        Collection.objects.bulk_create(objs, num)
        self.stdout.write(self.style.SUCCESS('Successfully created %d collections.' % num))

        end = timeit.default_timer()
        print('Execution time:', end-start)
