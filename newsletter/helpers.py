from django.utils.crypto import get_random_string
from django.utils.timezone import now,timedelta

def createRandomString():
  return get_random_string(length=64)

def returnDateInFuture():
  now = now()
  return now + timedelta(days=7)