from rest_framework import serializers

from category.models import Category
from post.models import Post, PostImage


class PostImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostImage
        fields = '__all__'


class PostListSerializer(serializers.ModelSerializer):
    owner_username = serializers.ReadOnlyField(source='owner.username')
    category_name = serializers.ReadOnlyField(source='category.name')

    class Meta:
        model = Post
        fields = ('id', 'title', 'owner', 'owner_username',
                  'category', 'category_name', 'preview')


class PostCreateUpdateSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.id')
    category = serializers.PrimaryKeyRelatedField(
        required=True, queryset=Category.objects.all())
    images = PostImageSerializer(many=True, required=False)

    class Meta:
        model = Post
        fields = '__all__'

    def create(self, validated_data):
        request = self.context.get('request')
        images = request.FILES.getlist('images')
        post = Post.objects.create(**validated_data)
        for image in images:
            PostImage.objects.create(image=image, post=post)
        return post


class PostDetailSerializer(serializers.ModelSerializer):
    owner_username = serializers.ReadOnlyField(source='owner.username')
    category_name = serializers.ReadOnlyField(source='category.name')
    images = PostImageSerializer(many=True)

    class Meta:
        model = Post
        fields = '__all__'

