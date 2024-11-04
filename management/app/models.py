from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name','last_name']
    ROLES_CHOICE = [
        (0,'user'),
        (1,'Project manager'),
        (2,'developer'),
        (3,'tester')
    ]
    role = models.PositiveIntegerField(choices=ROLES_CHOICE, default=0)
    

class Project(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(null=True,blank=True)
    created_by = models.ForeignKey(User,on_delete=models.CASCADE,related_name='project_user')
    members = models.ManyToManyField(User,related_name='project_members')
    start_date = models.DateTimeField(null=True,blank=True)
    end_date = models.DateTimeField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    

class Task(models.Model):
    
    Priority_choice = [
        ('Low','Low'),
        ('Medium','Medium'),
        ('High','High')
    ]
    
    Status_Choice = [
        ('Open','Open'),
        ('In Progress','In Progress'),
        ('Done','Done')
    ]
    
    title= models.CharField(max_length=200)
    description= models.TextField(null=True,blank=True)
    created_by = models.ForeignKey(User,on_delete=models.CASCADE,related_name='task_user')
    assignee = models.ForeignKey(User,on_delete=models.CASCADE,related_name='task_assigne',null=True,blank=True)
    project = models.ForeignKey(Project,on_delete=models.CASCADE,related_name='task_project')
    images = models.FileField(upload_to='tasks/',null=True,blank=True)
    priority = models.CharField(max_length=20,choices=Priority_choice,default='Low')
    status = models.CharField(max_length=20,choices=Status_Choice, default='Open')
    due_date = models.DateTimeField(null=True,blank=True)
    
    def __str__(self):
        return self.title
        
        
class Comment(models.Model):
    content = models.TextField()
    created_by = models.ForeignKey(User,on_delete=models.CASCADE,related_name='comment_user')
    task = models.ForeignKey(Task,on_delete=models.CASCADE,related_name='comment_task')
    created_at = models.DateTimeField(auto_now_add=True)
        
    
