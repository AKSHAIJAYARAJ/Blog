from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import BlogManagerSerializer,LikeManagerSerializer
from .blog_manager import BlogManager
from .like_manager import LikeManager
# from education.paginator import PaginatedView
from django.conf import settings
from jwt.api_jws import decode
import json


class BlogManagerViewSet(APIView):
    
    validator = BlogManagerSerializer
    
    def post(self,request):
        try:
            decoded_token = json.loads(decode(request.headers.get('Authorization').split(' ')[1], settings.SECRET_KEY, algorithms=['HS256']))
            data =request.data
            data.update({'user_id':decoded_token['id']})
            blog = self.validator(data=data,context={'request': self.request})
            if blog.is_valid():
                response = BlogManager().post(payload = blog.validated_data)
                return Response(data={"status":'OK',"result":'blog created','message':"SUCCESS"},status=status.HTTP_200_OK)
            else: 
                return Response(data={"status":'ERROR',"result": blog.errors,'message':"Invalid"},status=status.HTTP_200_OK)
        except Exception as e:
            print("-----EPTN----",e)
            return Response(data={"status":"ERROR","result":'','message':'ERROR'},status=status.HTTP_400_BAD_REQUEST)

    def get(self,request):
        blog_id = request.query_params.get("blog_id")
        try:
            response = BlogManager().get(filters= {'blog_id':blog_id})
            return Response(data={"status":'OK',"result":response,'message':"SUCCESS"},status=status.HTTP_200_OK)
        except Exception as e:
            print("-----EPTN----",e)
            return Response(data={"status":"ERROR","result":'','message':'ERROR'},status=status.HTTP_400_BAD_REQUEST)


    def put(self,request):
        decoded_token = json.loads(decode(request.headers.get('Authorization').split(' ')[1], settings.SECRET_KEY, algorithms=['HS256']))
        blog_id = request.query_params.get("blog_id")
        try:
            blog = self.validator(data=request.data,context={'request': self.request})
            if blog.is_valid():
                response = BlogManager().put(payload = blog.validated_data,filters={"blog_id":blog_id,"user_id": decoded_token['id']})
                return Response(data={"status":'OK',"result":'blog updated','message':"SUCCESS"},status=status.HTTP_200_OK)
            else: 
                return Response(data={"status":'ERROR',"result": blog.errors,'message':"Invalid"},status=status.HTTP_200_OK)
        except Exception as e:
            print("-----EPTN----",e)
            return Response(data={"status":"ERROR","result":'','message':'ERROR'},status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request):
        decoded_token = json.loads(decode(request.headers.get('Authorization').split(' ')[1], settings.SECRET_KEY, algorithms=['HS256']))

        blog_id = request.query_params.get("blog_id")
        try:
        
            response = BlogManager().delete(filters= {'blog_id':blog_id,'user_id':decoded_token['id']})
            return Response(data={"status":'OK',"result":'blog deleted','message':"SUCCESS"},status=status.HTTP_200_OK)
       
        except Exception as e:
            print("-----EPTN----",e)
            return Response(data={"status":"ERROR","result":'','message':'ERROR'},status=status.HTTP_400_BAD_REQUEST)
        
class BlogLikesViewSet(APIView):
    
    validator = BlogManagerSerializer

    def get(self,request):
        blog_id = request.query_params.get("blog_id")
        try:
            response = BlogManager().get_blog_details(blog_id = blog_id)
            return Response(data={"status":'OK',"result":response,'message':"SUCCESS"},status=status.HTTP_200_OK)
        except Exception as e:
            print("-----EPTN----",e)
            return Response(data={"status":"ERROR","result":'','message':'ERROR'},status=status.HTTP_400_BAD_REQUEST)


class LikeManagerViewSet(APIView):
    
    validator = LikeManagerSerializer
    
    def post(self,request):
        try:
            decoded_token = json.loads(decode(request.headers.get('Authorization').split(' ')[1], settings.SECRET_KEY, algorithms=['HS256']))
            data =request.data
            data.update({'user_id':decoded_token['id']})
            like = self.validator(data=data,context={'request': self.request})
            if like.is_valid():
                payload = like.validated_data
                print(payload)
                response = LikeManager().post(payload = payload)
                return Response(data={"status":'OK',"result":'like created','message':"SUCCESS"},status=status.HTTP_200_OK)
            else: 
                return Response(data={"status":'ERROR',"result": like.errors,'message':"Invalid"},status=status.HTTP_200_OK)
        except Exception as e:
            print("-----EPTN----",e)
            return Response(data={"status":"ERROR","result":'','message':'ERROR'},status=status.HTTP_400_BAD_REQUEST)

    def get(self,request):
        like_id = request.query_params.get("like_id")
        try:
            response = LikeManager().get(filters= {'like_id':like_id})
            return Response(data={"status":'OK',"result":response,'message':"SUCCESS"},status=status.HTTP_200_OK)
        except Exception as e:
            print("-----EPTN----",e)
            return Response(data={"status":"ERROR","result":'','message':'ERROR'},status=status.HTTP_400_BAD_REQUEST)


    def put(self,request):
        decoded_token = json.loads(decode(request.headers.get('Authorization').split(' ')[1], settings.SECRET_KEY, algorithms=['HS256']))
        like_id = request.query_params.get("like_id")
        try:
            like = self.validator(data=request.data,context={'request': self.request})
            if like.is_valid():
                response = LikeManager().put(payload = like.validated_data,filters={"like_id":like_id,"user_id": decoded_token['id']})
                return Response(data={"status":'OK',"result":'like updated','message':"SUCCESS"},status=status.HTTP_200_OK)
            else: 
                return Response(data={"status":'ERROR',"result": like.errors,'message':"Invalid"},status=status.HTTP_200_OK)
        except Exception as e:
            print("-----EPTN----",e)
            return Response(data={"status":"ERROR","result":'','message':'ERROR'},status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request):
        decoded_token = json.loads(decode(request.headers.get('Authorization').split(' ')[1], settings.SECRET_KEY, algorithms=['HS256']))
        like_id = request.query_params.get("like_id")
        try:
        
            response = LikeManager().delete(filters = {'like_id':like_id,'user_id':decoded_token['id']})
            return Response(data={"status":'OK',"result":'like deleted','message':"SUCCESS"},status=status.HTTP_200_OK)
       
        except Exception as e:
            print("-----EPTN----",e)
            return Response(data={"status":"ERROR","result":'','message':'ERROR'},status=status.HTTP_400_BAD_REQUEST)