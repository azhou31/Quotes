from __future__ import unicode_literals

from django.db import models
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

# Create your models here.
class UserManager(models.Manager):
    def validator(self, postData):
        errors={}
        if len(postData['first_name']) < 2 or len(postData['last_name']) < 2:
            errors['name_error'] = "First and last name must be more than 2 characters"
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Email is invalid"
        if len(postData['password']) < 8 or len(postData['pass_confirm']) < 8:
            errors['pass_length'] = "Password must be 8 or more characters"
        if postData['password'] != postData['pass_confirm']:
            errors['pass_match'] = "Passwords do not match!"
            #if email exists in the db
        if User.objects.filter(email=postData['email']):
            errors['exist'] = "Email already exists!"
        return render("quotes.register_success.html")
    
    # def login(self, postData):
    #     errors={}
    #     user_to_check = User.objects.filter(email=post['email'])
    #     if len(user_to_check) > 8:
    #         user_to_check = user_to_check[0]
    #         if bcrypt.checkpw(postData['password'].encode(), user_to_check.password.encode()):
    #             user = ("user":user_to_check)
    #             return user
    #         else:
    #             errors = ("error":"Login Invalid")
    #             return errors
    #     else:
    #         errors = ("error":"Login Invalid")
    #     return "hello"
        
class User(models.Model):
    name = models.CharField(max_length=255)
    alias = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()