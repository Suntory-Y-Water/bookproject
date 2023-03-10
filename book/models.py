from django.db import models
from .consts import MAX_RATE

CATEGORY = (('business', 'ビジネス'), ('life', '生活'), ('manga', '漫画'), ('fan', '推し'), ('other', 'その他'))
RATE_CHOICES = [(x, str(x)) for x in range(0, MAX_RATE + 1)]

class Book(models.Model):
    # データ型の定義
    title = models.CharField(max_length=100)
    text = models.TextField()

    # nullとblankはセットがいい
    thumbnail = models.ImageField(null=True, blank=True, default=None)
    category = models.CharField(max_length=100, choices=CATEGORY)

    # ユーザの記録を残すための処理
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title

class Review(models.Model):
    # 上のBookを元にデータを引っ張ってきている
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    text = models.TextField()
    rate = models.IntegerField(choices=RATE_CHOICES)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title