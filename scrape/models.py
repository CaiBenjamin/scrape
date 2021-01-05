from django.db import models

# Create your models here.
class pc_parts(models.Model):
    unique_url = models.CharField(max_length=200)
    part_type = models.CharField(max_length=200)
    part_name = models.CharField(max_length=200)
    pub_date = models.CharField(max_length=200)
    greater_than = False

    def __str__(self):
        return ("Unique Url: " + self.unique_url +"Part_Type: " +  self.part_type + "Part_Name: " + self.part_name + "Date: " + self.pub_date)

#q = pc_parts(unique_url = "/b/asdfasdf", part_type = "Cpu",
#  part_name =  "AMD RYZEN 5 3600",pub_date = "12/12/2020")