from django.utils.crypto import get_random_string
from django.utils import timezone

def createRandomString():
  return get_random_string(length=64)

def returnDateInFuture():
  now = timezone.now()
  return now + timezone.timedelta(days=7)