from rest_framework.response import Response
# from rest_framework.decorators import api_view
from .models import Student
from .serializer import StudentSerializer
from rest_framework.views import APIView

# Create your views here.
class StudentAPI(APIView):
    def get(self, request):
        students_objs= Student.objects.all()
        serializer = StudentSerializer(students_objs, many=True)
        return Response({'status':200,"mesage":"hello",'payload':serializer.data})
    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status':200,"mesage":"Data inserted successfully",'payload':serializer.data})
        else:
            return Response({'status':400,"mesage":"Invalid data",'payload':serializer.errors})
    def put(self, request, id):
        pass
    def patch(self, request):
        student = Student.objects.get(id=request.data['id'])
        serializer=StudentSerializer(student,data=request.data)

