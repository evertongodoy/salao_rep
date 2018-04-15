from django.db import models

# blank = true, NAO E CAMPO OBRIGATORIO
# null = true, a nivel de banco de dado eh NULLABLE


class Employees(models.Model):

    EMPLOYEE_ID = models.IntegerField(primary_key=True)
    FIRST_NAME = models.CharField(max_length=20)
    LAST_NAME = models.CharField(max_length=25)
    EMAIL = models.CharField(max_length=25)
    PHONE_NUMBER = models.CharField(max_length=20)
    HIRE_DATE = models.DateField()
    JOB_ID = models.CharField(max_length=10)
    SALARY = models.FloatField()
    COMMISSION_PCT = models.FloatField()
    MANAGER_ID =  models.IntegerField()
    DEPARTMENT_ID = models.IntegerField()

    def __str__(self):
        return '% %s' %(self.first_name, self.last_name)

    class Meta:
        db_table = 'employees' # define your custom name  https://stackoverflow.com/questions/32657766/how-to-control-table-names-created-by-django-migrate
