from rest_framework.response import Response
from rest_framework.decorators import api_view

from.models import Student

from.serializer import StudentSerializer

# Create your views here.

@api_view(['GET'])
def home(request):
    student_obj = Student.objects.all()
    serializer = StudentSerializer(student_obj, many=True)
    return Response({'status': 200, "message": "Success", "data": serializer.data})


@api_view(['POST'])
def create_student(request):
    serializer = StudentSerializer(data=request.data)
    if not serializer.is_valid():
        return Response({'status': 500, 'message': 'Something went wrong', 'error': serializer.errors})
    serializer.save()
    return Response({'status': 200, 'message': 'Success', 'data': serializer.data})

@api_view(['PUT'])
def update_student(request, id):
    try:
        student = Student.objects.get(id=id)
    except Student.DoesNotExist:
        return Response({'status': 404, 'message': 'Student not found'})

    serializer = StudentSerializer(instance=student, data=request.data)
    if not serializer.is_valid():
        return Response({'status': 500, 'message': 'Something went wrong', 'error': serializer.errors})
    serializer.save()
    return Response({'status': 200, 'message': 'Success', 'data': serializer.data})


@api_view(['DELETE'])
def delete_student(request, id):
    try:
        student = Student.objects.get(id=id)
        student.delete()
        return Response({'status': 200, 'message': 'Student deleted successfully'})
    except Student.DoesNotExist:
        return Response({'status': 404, 'message': 'Student not found'})
