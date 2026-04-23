from django.db import models


class Book(models.Model):
    GENRE_CHOICES = [
        ('novel', '小説'),
        ('tech', '技術書'),
        ('business', 'ビジネス'),
        ('other', 'その他'),
    ]

    title = models.CharField(max_length=200, verbose_name='タイトル')
    author = models.CharField(max_length=100, verbose_name='著者')
    genre = models.CharField(
        max_length=20,
        choices=GENRE_CHOICES,
        default='other',
        verbose_name='ジャンル',
    )
    review = models.TextField(blank=True, verbose_name='感想')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='登録日時')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='更新日時')

    class Meta:
        ordering = ['-created_at']
        verbose_name = '書籍'
        verbose_name_plural = '書籍一覧'

    def __str__(self):
        return self.title
