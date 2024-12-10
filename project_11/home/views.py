from rest_framework.response import Response
# from rest_framework.decorators import api_view
from .models import Students
from .serializer import StudentsSerializer
from rest_framework.views import APIView

# Create your views here.
class StudentAPi(APIView):
    def get(self, request):
        students_objs= Students.objects.all()
        serializer = StudentsSerializer(students_objs, many=True)
        return Response({'status':200,"mesage":"hello",'payload':serializer.data})
    def post(self, request):
        serializer = StudentsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status':200,"mesage":"Data inserted successfully",'payload':serializer.data})
        else:
            return Response({'status':400,"mesage":"Invalid data",'payload':serializer.errors})
    def put(self, request, id):
        pass
    def patch(self, request):
        student = Students.objects.get(id=request.data['id'])
        serializer=StudentSerializer(student,data=request.data)

