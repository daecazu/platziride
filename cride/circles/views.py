"""Circles views"""

# Django REST Framework
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Models
from cride.circles.models import Circle

#Serializers

from cride.circles.serializers import CircleSerializer
from cride.circles.serializers import CreateCircleSerializer
@api_view(['GET'])
def list_circles(request):
    """List circles"""
    circles = Circle.objects.filter(is_public=True)
    serializer = CircleSerializer(circles, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_circle(request):
    """Create circle"""
    serializer = CreateCircleSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    data=serializer.data
    circle=Circle.objects.create(**data)
    return Response(CircleSerializer(circle).data)

