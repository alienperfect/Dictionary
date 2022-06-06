from datetime import timedelta
from apps.account.models import Collection
from config.celery import app
from django.utils import timezone


@app.task(name='auto_delete')
def auto_delete():
    """Deletes collections older than 24 hours."""
    age = timezone.now() - timedelta(hours=24)
    Collection.objects.filter(created__lte=age).delete()
