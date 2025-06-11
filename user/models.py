import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
from book.models import Book

class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True
        
class CustomUser(AbstractUser):
    borrow_limit = models.SmallIntegerField(default=5)
    
    def __str__(self):
        return self.name

class Review(models.Model):
    review_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=False)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, null=False)
    rating = models.PositiveSmallIntegerField(null=False)
    comment = models.CharField(max_length=256, null=True)

class Borrow(models.Model):
    borrow_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.ManyToManyField(CustomUser, related_name="borrows")
    book = models.ForeignKey(Book, on_delete=models.CASCADE, null=False)
    borrow_date = models.DateTimeField(auto_now_add=True)
    expiration_date = models.DateTimeField()
    debt = models.PositiveIntegerField(null=False, default=0)