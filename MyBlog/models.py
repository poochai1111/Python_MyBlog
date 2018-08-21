# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class User(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name')  # Field name made lowercase.
    password = models.TextField(db_column='Password')  # Field name made lowercase.
    createdate = models.TextField(db_column='CreateDate')  # Field name made lowercase.
    updatedate = models.TextField(db_column='UpdateDate', blank=True, null=True)  # Field name made lowercase.
    status = models.IntegerField(db_column='Status')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'user'


class Blog(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=45)  # Field name made lowercase.
    content = models.CharField(db_column='Content', max_length=45)  # Field name made lowercase.
    createdate = models.DateTimeField(db_column='CreateDate')  # Field name made lowercase.
    updatedate = models.DateTimeField(db_column='UpdateDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'blog'
