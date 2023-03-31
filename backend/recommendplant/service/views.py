from django.shortcuts import render
from .models import PlantModel
import pandas as pd
import json
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import PlantSerializer
from .inference import predict_image_classification_sample
from PIL import Image
import os
# Create your views here.


@api_view(["GET"])
def search_all(request):
    queryset = PlantModel.objects.all()
    serializer = PlantSerializer(queryset,many=True)
    return Response(serializer.data)

@api_view(["GET"])
def search_by_name(request):
    name=request.GET.get('name',None)
    queryset = PlantModel.objects.filter(plant_name__contains=name)
    serializer = PlantSerializer(queryset,many=True)
    return Response(serializer.data)

@api_view(["POST",])
def inference(request):
    image = request.data['image']
    img = Image.open(image)
    img_path = f'/home/rpgplant2023/recommendplant/data/{image}'
    img.save(img_path, 'png')
    result = predict_image_classification_sample(filename=img_path)
    os.remove(img_path)
    if len(result['displayNames']) > 0:
        plant_name = int(result['displayNames'][0])
    else:
        plant_name = 1
    queryset = PlantModel.objects.filter(plant_id=plant_name)
    serializer = PlantSerializer(queryset,many=True)
    return Response(serializer.data)

@api_view(["GET"])
def db_init(sample_data):
    sample_data = pd.read_csv("./data/plant_data.tsv",sep='\t')
    n_sample = len(sample_data)
    sample_data['growthHg'] = sample_data['growthHg'].fillna(10)
    for i in range(n_sample):
        sample = sample_data.loc[i]
        instance = PlantModel()
        instance.plant_name = sample['name']
        instance.description = sample['advise']
        instance.plant_landscape_type = sample['clcode']
        instance.eclogy_type=sample['eclgyCode']
        instance.flower=sample['flclrNm']
        instance.plant_type =sample['fmlCode']
        instance.frt_info = sample['frtlzrInfo']
        instance.grow_area = sample['growthAra']
        instance.grow_height = sample['growthHg']
        instance.grow_temperature = sample['grwhTp']
        instance.grow_whstle = sample['grwhstle']
        instance.grow_humidity = sample['hdcode']
        instance.flower_season = sample['ignseason']
        instance.leaf_color = sample['leafcolor']
        instance.light_demand = sample['lightdemand']
        instance.manage_demand =sample['managedemand']
        instance.plant_bne_name = sample['plntbneNm']
        instance.plant_eng_name = sample['plntzrNm']
        instance.plant_place = sample['postngplace']
        instance.birth_type = sample['prpgtmth']
        instance.spring_water_cycle = sample['watercycleSpring']
        instance.summer_water_cycle = sample['watercycleSummer']
        instance.autumn_water_cycle = sample['watercycleAutumn']
        instance.winter_water_cycle = sample['watercycleWinter']
        instance.save()