from django.db import models

CATEGORY = (('business', 'ビジネス'), ('life', '生活'), ('manga', '漫画'), ('other', 'その他'))

class Book(models.Model):
    # データ型の定義
    title = models.CharField(max_length=100)
    text = models.TextField()
    category = models.CharField(max_length=100, choices=CATEGORY)

    def __str__(self) -> str:
        return self.title