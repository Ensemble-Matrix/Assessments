from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.core.files.storage import FileSystemStorage
from numpy import array, frombuffer, argmax
from .serializers import ImageSerializer
from imagemanipulation.models import Imager
from PIL import Image
import cv2, json, requests

@api_view(['POST'])
def postTest(request):
    serializer = ImageSerializer(data=request.data)
    if serializer.is_valid():
        file = request.FILES['image']
        image = Image.open(file).resize((28,28)).convert('L')
        arraydata = array(image)
        arraydata = arraydata / 255.0
        arraydata = arraydata.reshape(1, 28, 28, 1)
        data = json.dumps({"signature_name":"serving_default","instances": arraydata.tolist()})
        headers = {"content-type": "application/json"}
        json_response = requests.post('http://localhost:8501/v1/models/fashion_model:predict', data=data, headers=headers)
        predictions = json.loads(json_response.text)['predictions']
        print(argmax(predictions[0]))
        class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']
        predicted_label = class_names[argmax(predictions[0])]
        serializer.save(predicted_label=predicted_label)
        return Response(serializer.data)
    return Response(serializer.data)
    
















#if request.FILES['image']:
    #    file = request.FILES['label']
    #    class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
    #           'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']
    #    ##myfile = str(file.read())
    #    ##image = cv2.imdecode(numpy.frombuffer(myfile, numpy.uint8), cv2.IMREAD_UNCHANGED)
    #    #print(image.shape)
    #    fss = FileSystemStorage()
    #    savefile = fss.save(file.name, file)
    #    image = Image.open(file.name).resize((28,28)).convert('L')
    #    arraydata = array(image)#.reshape(-1,28,28,1)
    #    arraydata = arraydata / 255.0
    #    arraydata = arraydata.reshape(1,28,28,1)
    #    #print(arraydata)
    #    print(arraydata.shape)
    #    print(arraydata.dtype)
    #    data = json.dumps({"signature_name":"serving_default","instances": arraydata.tolist()})
    #    headers = {"content-type": "application/json"}
    #    json_response = requests.post('http://localhost:8501/v1/models/fashion_model:predict', data=data, headers=headers)
    #    predictions = json.loads(json_response.text)['predictions']
    #    print(predictions)
    #    print(argmax(predictions[0]))
    #    return Response({"message":"you sent image file nice"})
    #else:
    #    return Response({"message":"you sent garbage not nice"})
    #return Response({"message":"post request works"})


