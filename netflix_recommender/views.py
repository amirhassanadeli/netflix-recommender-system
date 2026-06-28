# netflix_recommender/views.py

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .serializers import RecommendationSerializer
from .recommender import get_recommendations


@api_view(["POST"])
def recommendations(request):
    serializer = RecommendationSerializer(data=request.data)

    if not serializer.is_valid():
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
        )

    title = serializer.validated_data["title"]

    recommendations = get_recommendations(title)

    if recommendations is None:
        return Response(
            {"error": "Movie not found"},
            status=status.HTTP_404_NOT_FOUND
        )

    return Response(
        {
            'title': title,
            'recommendations': recommendations
        }
    )
