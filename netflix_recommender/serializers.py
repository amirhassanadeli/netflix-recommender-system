from rest_framework import serializers

class RecommendationSerializer(serializers.Serializer):
    title = serializers.CharField(
        max_length=255,
        required=True,
        allow_blank=False,
        error_messages={
            'required': 'Recommendation title is required',
            'blank': 'title is required'
        }
    )
