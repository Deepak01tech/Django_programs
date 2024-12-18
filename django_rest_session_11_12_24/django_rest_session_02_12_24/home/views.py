from rest_framework.response import Response
from rest_framework.decorators import api_view 
from .models import Student
from .serializer import StudentSerializer,UserSerializer
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
# Create your views here.

# @api_view(['GET'])
# def home(request):
#     student_objs = Student.objects.all()
#     serializer=StudentSerializer(student_objs,many=True)
#     return Response({'status':200,"message": "Hello, world!",'payload':serializer.data})


# @api_view(['POST'])
# def register_student(request):
#     serializer = StudentSerializer(data=request.data)
#     if not serializer.is_valid():
#         return Response({'status':500,'message':'something went wrong','error':serializer.errors})
    
#     serializer.save()
#     return Response({'status':200,'message':'Student added successfully'})



# @api_view(['PUT'])
# def update_student(request,id):
#     student=Student.objects.get(id=id)
#     serailizer=StudentSerializer(student,data=request.data,partial=True)
#     if not serailizer.is_valid():
#         return Response({'status':500,'message':'something went wrong','error':serailizer.errors})
#     serailizer.save()
#     return Response({'status':200,'message':'Student updated successfully.'})



# @api_view(['DELETE'])
# def delete_student(request,id):
#     try:
#         student=Student.objects.get(id=id)
#         student.delete()
#     except:
#         return Response({'status':404,'message':'Student not found'})
#     return Response({'status':200,'message':'Student deleted succesfully'})



class StudentAPI(APIView):
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]
    def get(self,request):
        student_objs = Student.objects.all()
        serializer=StudentSerializer(student_objs,many=True)
        return Response({'status':200,"message": "Hello, world!",'data':serializer.data})
    def post(self,request):
        serializer = StudentSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({'status':500,'message':'something went wrong','error':serializer.errors})
        
        serializer.save()
        return Response({'status':200,'message':'Student added successfully'})
    def put(self,request):
        pass
    def patch(self,request):
        student=Student.objects.get(id=request.data['id'])
        serailizer=StudentSerializer(student,data=request.data,partial=True)
        if not serailizer.is_valid():
            return Response({'status':500,'message':'something went wrong','error':serailizer.errors})
        serailizer.save()
        return Response({'status':200,'message':'Student updated successfully.'})
    def delete(self,request):
        try:
            student=Student.objects.get(id=request.GET.get('id'))
            student.delete()
        except:
            return Response({'status':404,'message':'Student not found'})
        return Response({'status':200,'message':'Student deleted succesfully'})



class RegisterAPI(APIView):
    def post(self,request):
        serializer = UserSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({'status':500,'message':'something went wrong','error':serializer.errors})
        
        serializer.save()
        return Response({'status':200,'message':'User added successfully'})




from rest_framework import generics



class StudentGeneric(generics.ListAPIView,generics.CreateAPIView):
        queryset = Student.objects.all()
        serializer_class = StudentSerializer




class StudentGeneric1(generics.UpdateAPIView,generics.DestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    lookup_field='id'



# gunicorn --workers 4 --worker-class gthread --threads 2 --timeout 120 --bind 0.0.0.0:8000 todo.wsgi

