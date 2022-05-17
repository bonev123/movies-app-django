from rest_framework.serializers import ModelSerializer

from movieExamDef.main.models import Movie


class MovieListSerializer(ModelSerializer):
    class Meta:
        model = Movie
        fields = ('movie_name', 'director', 'genre', 'description', 'image_url', 'price',)



class MovieFullSerializer(ModelSerializer):
    class Meta:
        model = Movie
        fields = ('movie_name', 'director', 'genre', 'description', 'image_url', 'price',)

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)
