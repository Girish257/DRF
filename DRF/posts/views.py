from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status, generics, mixins  # FOR GENERIC API VIEW
from rest_framework.decorators import api_view, APIView
# API VIEW FOR CLASS BASED API VIEW
from .models import Post
from .serializers import PostSerializer
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated

# posts = [
#     {
#         "id": 1,
#         "title": "Why is it difficult to learn Programming?",
#         "content": "This is to give reasons why it is hard"
#     },
#     {
#         "id": 2,
#         "title": "Learn JavaScript",
#         "content": "This is course on JS"
#     },
#     {
#         "id": 3,
#         "title": "Is it difficult to learn Programming ?",
#         "content": "No"
#     }
# ]

# Funtion Based API View


# @api_view(http_method_names=["GET", "POST"])
# def homepage(request: Request):

#     if request.method == "POST":
#         data = request.data

#         response = {'message': 'Hello World', 'data': data}

#         return Response(data=response, status=status.HTTP_201_CREATED)

#     response = {'message': 'Hello World'}
#     return Response(data=response, status=status.HTTP_200_OK)


# @api_view(http_method_names=["GET", "POST"])
# def list_posts(request: Request):
#     posts = Post.objects.all()

#     if request.method == "POST":
#         data = request.data

#         serilizer = PostSerializer(data=data)
#         if serilizer.is_valid():
#             serilizer.save()

#             response = {
#                 "message": "Post Created",
#                 "data": serilizer.data
#             }
#             return Response(data=response, status=status.HTTP_201_CREATED)
#         return Response(data=serilizer.errors, status=status.HTTP_400_BAD_REQUEST)

#     serilizer = PostSerializer(instance=posts, many=True)

#     response = {
#         "message": "posts",
#         "data": serilizer.data
#     }

#     return Response(data=response, status=status.HTTP_200_OK)


# @api_view(http_method_names=["GET"])
# def post_details(request: Request, post_id: int):
#     post = get_object_or_404(Post, pk=post_id)

#     serilizer = PostSerializer(instance=post)

#     response = {
#         "message": "post",
#         "data": serilizer.data
#     }

#     return Response(data=response, status=status.HTTP_200_OK)


# @api_view(http_method_names=["PUT"])
# def update_post(request: Response, post_id: int):
#     post = get_object_or_404(Post, pk=post_id)

#     data = request.data
#     serilizer = PostSerializer(instance=post, data=data)

#     if serilizer.is_valid():
#         serilizer.save()

#         response = {
#             "message": "Post Updated Successfully",
#             "data": serilizer.data
#         }

#         return Response(data=response, status=status.HTTP_200_OK)

#     return Response(data=serilizer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(http_method_names=["DELETE"])
# def delete_post(request: Response, post_id: int):
#     post = get_object_or_404(Post, pk=post_id)

#     post.delete()

#     return Response(status=status.HTTP_204_NO_CONTENT)


# Classed Based API VIEW


# class PostListCreateView(APIView):
#     """
#         a view for creating and listing posts
#     """

#     serializer_class = PostSerializer

#     def get(self, request: Request, *args, **kwargs):
#         posts = Post.objects.all()
#         serializer = self.serializer_class(instance=posts, many=True)

#         return Response(data=serializer.data, status=status.HTTP_200_OK)

#     def post(self, request: Request, *args, **kwargs):
#         data = request.data
#         serializer = self.serializer_class(data=data)

#         if serializer.is_valid():
#             serializer.save()

#             response = {
#                 "message": "Post Created",
#                 "data": serializer.data
#             }
#             return Response(data=response, status=status.HTTP_201_CREATED)

#         return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class PostRetrieveUpdateDeleteView(APIView):
#     serializer_class = PostSerializer

#     def get(self, request: Request, post_id: int):
#     post = get_object_or_404(Post, pk=post_id)
#     serializer = self.serializer_class(instance=post)

#     return Response(data=serializer.data, status=status.HTTP_200_OK)

# def put(self, request: Request, post_id: int):

#     post = get_object_or_404(Post, pk=post_id)

#     data = request.data
#     serializer = self.serializer_class(instance=post, data=data)

#     if serializer.is_valid():
#         serializer.save()

#         responce = {
#             "message": "Post Updated",
#             "data": serializer.data
#         }
#         return Response(data=responce, status=status.HTTP_200_OK)

#     return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# def delete(self, request: Request, post_id: int):
#     post = get_object_or_404(Post, pk=post_id)

#     post.delete()

#     return Response(status=status.HTTP_204_NO_CONTENT)


# Generic API View and Model Mixins


class PostListCreateGenericView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]
    queryset = Post.objects.all()

    def get(self, request: Request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request: Request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class PostRetrieveUpdateDeleteGenericView(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):

    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def get(self, request: Request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request: Request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request: Request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
