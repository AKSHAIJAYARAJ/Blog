from rest_framework.serializers import ModelSerializer
from .models import BlogModel,LikeModel


class BlogManagerSerializer(ModelSerializer):

    class Meta:
        model = BlogModel
        fields = "__all__"
class LikeManagerSerializer(ModelSerializer):
    
    class Meta:
        model = LikeModel
        fields = "__all__"