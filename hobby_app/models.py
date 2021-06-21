from django.db import models




# Create your models here.

from django.db.models.deletion import CASCADE # the regex model
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
# Create your models here.
class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        
        # add keys and values to errors dictionary for each invalid field
        FIRST_NAME_REGEX = re.compile(r'^[a-zA-Z ]+$') # fist name check, should be letters
        if not  FIRST_NAME_REGEX.match(postData['f_name']):             
            errors['first_name_format'] = "Invalid name format"
        if len(postData['f_name']) < 2:
            errors['f_name'] = "First name should be at least 2 characters"
        if len(postData['l_name']) < 2:
            errors['l_name'] = "Last name should be at least 2 characters"
        if len(postData['email']) < 6:
            errors['email'] = "Email should be at least 6 characters" 
        if len(postData['pw']) < 8:
            errors['password'] = "Password should be at least 9 characters"
        if postData['pw'] != postData['pw_conf']:
            errors['match'] = "User or password do not match"
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):    # test whether a field matches the pattern            
            errors['regex'] = "Invalid email format!"

        users_with_email = User.objects.filter(email = postData['email']) 
        if len(users_with_email) >=1:
            errors['users_duplicate'] = "Email address taken already, choose another"
        
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name =  models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.TextField()
    user_img = models.ImageField(default='default.png',upload_to="images/")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

class HobbyManager(models.Manager):
    
    def basic_validator(self, postData):
        a_hobby = Hobby.objects.filter(name = postData['name'])
        errors = {}
        
        # add keys and values to errors dictionary for each invalid field
        
        if len(postData['name']) < 3:
            errors['name'] = "Hobby name should be at least 3 characters"
        if len(postData['description']) < 3:
            errors['description'] = "Hobby description should be at least 3 characters"
        # if a_hobby:
        #     errors['hobby_duplicate'] = "This hobby already exists, create another one"

        return errors


class Hobby(models.Model):
    name = models.CharField(max_length=255)
    description= models.TextField()
    hobby_img = models.ImageField(upload_to="images/")
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    creator = models.ForeignKey(User,related_name="hobbies", on_delete=CASCADE)
    like = models.ManyToManyField(User, related_name="liked_hobbies",blank=True)

    objects = HobbyManager()
    def __str__(self):
        return self.name

class CommentManager(models.Manager):
    def basic_validator(self, postData):
        
        errors = {}
        
        # add keys and values to errors dictionary for each invalid field
        
        if len(postData['content']) < 6:
            errors['content'] = "Comment should be at least 6 characters"
        
        return errors
    


class Comment(models.Model):
    content = models.TextField()
    poster = models.ForeignKey(User,related_name="user_comments", on_delete=CASCADE)
    hobby_comment = models.ForeignKey(Hobby,related_name="hobby_comments",on_delete=CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = CommentManager()
    













