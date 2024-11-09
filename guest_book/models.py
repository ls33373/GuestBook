from django.db import models

# 방명록 모델
class GuestBook(models.Model):
    description = models.TextField(max_length = 500, blank = False)
    create_time = models.DateTimeField(auto_now_add = True)
    writer = models.CharField(max_length = 20, blank = True)
    # password = models.CharField(max_length = 8, blank = True)
