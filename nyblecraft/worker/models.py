from datetime import datetime
from django.db import models
from django.urls import reverse

class Department(models.Model):

    name_department = models.CharField(
        max_length=255,
        )
    

    class Meta:
        db_table = "department"
        verbose_name = "Department"
        verbose_name_plural = "Departments"

    def __str__(self):
        return self.name_department


class Position(models.Model):

    name_position = models.CharField(
        max_length=255,
        )

    class Meta:
        db_table = "position"
        verbose_name = "Position"
        verbose_name_plural = "Positions"

    def __str__(self):
        return self.name_position


class Worker(models.Model):

    last_name = models.CharField(
        max_length=255,
    )
    first_name = models.CharField(
        max_length=255,
    )
    patronymic = models.CharField(
        max_length= 255,
    )
    current_department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        unique=False,
    )
    current_position = models.ForeignKey(
        Position,
        on_delete=models.CASCADE,
        unique=False,
    )
    device_date = models.DateField()


    def get_absolute_url(self):
        return reverse('worker', kwargs={"pk":self.pk})


    def experience(self):
        return (datetime.date.today() - self.device_date()).days

    class Meta:
        db_table = "worker"
        verbose_name = "Worker"
        verbose_name_plural = "Workers"

    def __str__(self):
        return f"{self.last_name} {self.first_name} {self.patronymic}"
