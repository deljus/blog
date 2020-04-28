from django.db import models
from django.contrib.auth.models import User
from crum import get_current_user


class Posts(models.Model):
    name = models.CharField(max_length=255)
    post = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        user = get_current_user()
        self.user = user
        super(Posts, self).save(*args, **kwargs)
