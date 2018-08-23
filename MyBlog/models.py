# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class MyBlog(models.Model):
    id = models.IntegerField(db_column='blog_id', primary_key=True, auto_created=True)  # Field name made lowercase.
    name = models.CharField(db_column='blog_creater', max_length=45)
    title = models.CharField(db_column='blog_title', max_length=45)
    content = models.CharField(db_column='blog_content', max_length=4500)  # Field name made lowercase.
    create_date = models.DateTimeField(db_column='blog_create_date')  # Field name made lowercase.
    update_date = models.DateTimeField(db_column='blog_update_date', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'my_blog'
