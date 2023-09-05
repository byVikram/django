from rest_framework.decorators import api_view
from rest_framework.response import Response
from subapp.serializers import PeopleSerializers
from subapp.models import Person, hello
from rest_framework.views import APIView
from rest_framework import status


@api_view(['GET'])
def index(request):
    hello=request.GET.get("search")
    courses = {
        'course_name': 'python',
        'learn':['flask','django','tornado'],
        'course_provider':'scalar'
    }
    print(hello)
    return Response(courses)
@api_view(['GET','POST','PUT','PATCH'])
def people(request):
        if request.method == "GET":
            # name = request.data['first']
            # print(name)
            objs = hello.objects.all()
            serializer = PeopleSerializers(objs,many=True)
            return Response(serializer.data,  status=status.HTTP_201_CREATED) 

        
        elif request.method == "POST":
            name = request.data['first']
            print(name)
            data=request.data
            obj = hello.objects.filter(first=name)
            if obj:
                print("User Exhist")
                return Response({"message":"user exhist"})
            else:
                serializer = PeopleSerializers(data=data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data,  status=status.HTTP_201_CREATED) 
                return Response(serializer.errors)
            
        elif request.method == 'PUT':
            data=request.data
            obj = hello.objects.get(id=data['id'])
            serializer=PeopleSerializers(obj,data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors)
        
        elif request.method == 'PATCH':
            data=request.data
            obj = hello.objects.get(id=data['id'])
            serializer=PeopleSerializers(obj,data=data , partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors)
        
        elif request.method == 'DELETE':
            data = request.data
            obj = hello.objects.get(id=data['id'])
            obj.delete()
            return({"message" : "Deleted in database"})
             

class main(APIView):
    def get(self,request):
        return Response({"message":"get requested"})
    def post(self,request):
        return Response({"message":"post requested"})

    