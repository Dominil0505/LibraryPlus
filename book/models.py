import uuid
from django.db import models

class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(null=False, db_index=True, unique=True)
    
    class Meta:
        abstract = True
    
    def __str__(self):
        return self.name

class Publisher(BaseModel):
    pass

class Category(BaseModel):
    pass

class Author(BaseModel):
    pass

class Book(BaseModel):
    released_date = models.DateTimeField(null=False)
    copy_number = models.PositiveSmallIntegerField(null=False)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, null=False)
    categories = models.ManyToManyField(Category, related_name="books")
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    fee = models.PositiveSmallIntegerField()
    
    def __str__(self):
        return self.name
    
