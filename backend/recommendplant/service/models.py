from django.db import models

# Create your models here.

class PlantModel(models.Model):
    plant_id =models.BigAutoField(primary_key=True,null=False,unique=True)
    plant_name = models.CharField(max_length=100,null=False)
    description = models.CharField(max_length=1000,null=True)
    plant_landscape_type = models.CharField(max_length=100,null=False) # 조경종류 n:m
    eclogy_type=models.CharField(max_length=100,null=True) # n:m
    flower=models.CharField(max_length=50,null=True) # n:m
    plant_type =models.CharField(max_length=100,null=False) # 식물 종/속
    frt_info = models.CharField(max_length=200,null=True) #비료
    grow_area = models.IntegerField(null=False)
    grow_height = models.IntegerField(null=False)
    grow_temperature = models.CharField(max_length=100,null=True,default="16~20℃") # type으로 바꾸기
    grow_whstle = models.CharField(max_length=30,null=False) # 성장 모양 n:m
    grow_humidity = models.CharField(max_length=30,null=True,default = "70% 이상") # type으로 바꾸기
    flower_season = models.CharField(max_length=30,null=True)
    leaf_color = models.CharField(max_length=100,null=True,default='기타')
    light_demand = models.CharField(max_length=200,null=False) # type으로 바꾸기
    manage_demand =models.CharField(max_length=50,null=False) # type으로 바꾸기
    plant_bne_name = models.CharField(max_length=200,null=False)
    plant_eng_name = models.CharField(max_length=200,null=False)
    plant_place = models.CharField(max_length=500,null=False)
    birth_type = models.CharField(max_length=100,null=False) # n:m
    spring_water_cycle = models.CharField(max_length=200,null=True,default="토양 표면이 말랐을때 충분히 관수함")
    summer_water_cycle = models.CharField(max_length=200,null=True,default="토양 표면이 말랐을때 충분히 관수함")
    autumn_water_cycle = models.CharField(max_length=200,null=True,default="토양 표면이 말랐을때 충분히 관수함")
    winter_water_cycle = models.CharField(max_length=200,null=True,default="토양 표면이 말랐을때 충분히 관수함")
    
    
    
    
    
    