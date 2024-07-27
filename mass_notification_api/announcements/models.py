from django.db import models
from users.models import CustomUser

class Announcement(models.Model):
    title = models.CharField(max_length=100)
    message = models.TextField()
    author = models.ForeignKey(CustomUser, related_name='announcements', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return f'Title: {self.title}\nMessage: {self.message}\nAuthor: {self.author}\nDate created: {self.date_created}\nLast Modified: {self.last_modified}'