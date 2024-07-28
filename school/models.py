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
        **NULLABLE,
    )
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


class Subscription(models.Model):
    user = models.ForeignKey(
        User,
        verbose_name='ползователь',
        on_delete=models.CASCADE
    )
    course = models.ForeignKey(
        Course,
        verbose_name='Course',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f'Пользватель с ID {self.user} подписан на курс {self.course}'

    class Meta:
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'


class Payments(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='пользователь'
    )
    date = models.DateField(
        auto_now=True,
        verbose_name='дата платежа'
    )
    paid_lesson = models.ForeignKey(
        Lesson,
        on_delete=models.CASCADE,
        verbose_name='оплаченный урок',
        **NULLABLE
    )
    paid_course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        verbose_name='оплаченный курс',
        **NULLABLE
    )
    summ = models.PositiveIntegerField(
        verbose_name='сумма платежа'
    )
    session_id = models.CharField(
        max_length=255,
        verbose_name='session_id',
        **NULLABLE
    )
    link = models.URLField(
        max_length=400,
        verbose_name='ссылка на оплату',
        **NULLABLE
    )

    def __str__(self):
        return (f'Платёж {self.summ} от {self.user} способ оплаты {self.pay_method} '
                f'за {self.paid_course if self.paid_course else self.paid_lesson}')

    class Meta:
        verbose_name = 'платёж'
        verbose_name_plural = 'платежи'
        ordering = ('date',)
