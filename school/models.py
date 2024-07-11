from django.db import models

from users.models import User

NULLABLE = {"blank": True, "null": True}


class Course(models.Model):
    name = models.CharField(
        max_length=128,
        verbose_name="название курса",
        help_text="укажите название курса",
    )
    description = models.TextField(
        verbose_name="описание учебного курса",
        help_text="укажите описание учебного курса",
        **NULLABLE,
    )
    image = models.ImageField(
        upload_to="course/images/",
        verbose_name="изображение",
        help_text="загрузите изображение",
        **NULLABLE,
    )
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='cоздатель',
        **NULLABLE,
    )

    class Meta:
        verbose_name = "учебный курс"
        verbose_name_plural = "учебные курсы"

    def __str__(self):
        return (
            f"наименование курса: {self.name}, описание курса: {self.description}"
        )


class Lesson(models.Model):
    name = models.CharField(
        max_length=128,
        verbose_name="название урока",
        help_text="укажите название урока",
    )
    description = models.TextField(
        verbose_name="описание урока",
        help_text="укажите описание урока",
        **NULLABLE,
    )
    image = models.ImageField(
        upload_to="course/images/",
        verbose_name="изображение",
        help_text="загрузите изображение",
        **NULLABLE,
    )
    video_track = models.CharField(
        max_length=256,
        verbose_name="видео",
        help_text="укажите ссылку на видео",
        **NULLABLE,
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        verbose_name='курс',
        null=True,
        blank=True)
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='cоздатель',
        **NULLABLE,
    )

    class Meta:
        verbose_name = "урок"
        verbose_name_plural = "уроки"

    def __str__(self):
        return (
            f"наименование урока: {self.name}, описание урока: {self.description}"
        )

