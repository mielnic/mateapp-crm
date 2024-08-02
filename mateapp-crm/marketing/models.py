from django.db import models

class BaseModel(models.Model):
    create_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    deleted = models.BooleanField(blank=True, default=0)
    deletedBy = models.BigIntegerField(blank=True, null=True)
    
    class Meta:
        abstract = True

class Target(BaseModel):
    email = models.EmailField()
    data = models.JSONField(blank=True, null=True)
    optOut = models.BooleanField(default=False)
    valid = models.BooleanField(default=True)

    def __str__(self):
        return self.email
    
class TargetList(BaseModel):
    name = models.TextField(max_length=50)
    targets = models.ManyToManyField(Target)

    def __str__(self):
        return self.name
    
class EmailTemplate(BaseModel):
    name = models.TextField(max_length=50)
    file = models.FileField(upload_to='mail_templates', null=True)

    def __str__(self):
        return self.name
    
class Mailing(BaseModel):
    name = models.TextField(max_length=50)
    emailTemplate = models.ForeignKey(EmailTemplate, on_delete=models.DO_NOTHING)
    targetList = models.ForeignKey(TargetList, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name