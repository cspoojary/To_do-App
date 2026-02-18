from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=100, null = False, blank = False)
    created_at = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return self.title
