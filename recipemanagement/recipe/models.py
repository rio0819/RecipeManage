from django.db import models
from pathlib import Path
import uuid

class Page(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name="ID")
    title = models.CharField(max_length=100, verbose_name="タイトル")
    material=models.TextField(max_length=1000, verbose_name="材料")
    recipe = models.TextField(max_length=2000,verbose_name="手順")
    cook_time = models.DurationField (verbose_name="調理時間")
    picture = models.ImageField(upload_to="recipe/picture/", blank=True, null=True, verbose_name="写真")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="作成日時")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="更新日時")

    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        picture = self.picture
        super().delete(*args, **kwargs)
        if picture:
            Path(picture.path).unlink(missing_ok=True)