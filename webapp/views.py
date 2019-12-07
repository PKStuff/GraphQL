from .models import Employee
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializer import Employee_Serializer
import logging
log = logging.getLogger(__name__)

@api_view(['GET', 'POST'])
def get_post(request):

    if request.method == 'GET':

        data = Employee.objects.all()
        serializer = Employee_Serializer(data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'POST':

        serializer = Employee_Serializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def single_data(request, Emp_ID):

    try: 
        data1 = Employee.objects.get(Emp_ID=Emp_ID)

    except Exception as err:
        log.info("Data does not exists with error:{}".format(err))

    if request.method == 'GET':
        serializer = Employee_Serializer(data1)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'PUT':
        serializer = Employee_Serializer(data1, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        data1.delete()
    
