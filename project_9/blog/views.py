from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer, ProfileSerializer
from .models import User, Profile


@api_view(['GET'])
def home(request):
    users = User.objects.all()
    user_data = []
    for user in users:
        profile = user.profile if hasattr(user, 'profile') else None
        user_data.append({
            'id': user.id,
            'username': user.username,
            'email': user.email,
            'content': user.content,
            'profile': {
                'name': profile.name if profile else None,
                'image': profile.image.url if profile and profile.image else None
            } if profile else None
        })
    return Response({'status': 200, 'message': 'Success', 'data': user_data})


@api_view(['POST'])
def create_user(request):
    serializer = UserSerializer(data=request.data)
    if not serializer.is_valid():
        return Response({'status': 500, 'message': 'Something went wrong', 'error': serializer.errors})
    serializer.save()
    return Response({'status': 200, 'message': 'Success', 'data': serializer.data})


@api_view(['PUT'])
def update_user(request, id):
    try:
        user = User.objects.get(id=id)
    except User.DoesNotExist:
        return Response({'status': 404, 'message': 'User not found'})

    serializer = UserSerializer(instance=user, data=request.data)
    if not serializer.is_valid():
        return Response({'status': 500, 'message': 'Something went wrong', 'error': serializer.errors})
    serializer.save()
    return Response({'status': 200, 'message': 'Success', 'data': serializer.data})


@api_view(['DELETE'])
def delete_user(request, id):
    try:
        user = User.objects.get(id=id)
        user.profile.delete()
        user.delete()
        return Response({'status': 200, 'message': 'User and profile deleted successfully'})
    except User.DoesNotExist:
        return Response({'status': 404, 'message': 'User not found'})


@api_view(['POST', 'PUT'])
def manage_profile(request, id=None):
    if request.method == 'POST':
        user = User.objects.get(id=id)
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            profile, created = Profile.objects.get_or_create(user=user)
            profile.name = serializer.validated_data.get('name', profile.name)
            profile.image = serializer.validated_data.get('image', profile.image)
            profile.save()
            return Response({'status': 200, 'message': 'Profile created/updated successfully', 'data': serializer.data})
        return Response({'status': 400, 'message': 'Invalid data', 'error': serializer.errors})

    if request.method == 'PUT':
        user = User.objects.get(id=id)
        profile = user.profile
        serializer = ProfileSerializer(profile, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 200, 'message': 'Profile updated successfully', 'data': serializer.data})
        return Response({'status': 400, 'message': 'Invalid data', 'error': serializer.errors})
