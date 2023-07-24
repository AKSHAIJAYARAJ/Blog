from .models import BlogModel
from .models import LikeModel

class BlogManager:

    def get(self,filters:dict = None):
        try:
            instance = BlogModel.objects.filter(**filters).all()
            blog_data = list(instance.values())
            return blog_data
        except Exception as e:
            print("-----User EPTN-------",e)
            return False
    def post(self,payload : dict = None):
        try:
            instance = BlogModel(**payload)
            instance.save()
            return True
        except Exception as e:
            print("-----User EPTN-------",e)
            return False
    def put(self,payload : dict, filters : dict):
        try:
            instance = BlogModel.objects.get(**filters)
            for key, value in payload.items():
                setattr(instance, key, value)
            instance.save()
        except Exception as e:
            print("-----User EPTN-------",e)
            return False
    def delete(self,filters : dict):
        try:
            instance = BlogModel.objects.filter(**filters)
            instance.delete()
            
            return True
        except Exception as e:
            print("-----User EPTN-------",e)
            return False
    def get_blog_details(self,blog_id : int = None):

        try:
             
            if blog_id:
                instance = BlogModel.objects.filter(blog_id = blog_id)
                
            else:
                instance = BlogModel.objects.all()
            blog_data = list(instance.values())
            for blog_details in blog_data:
                like_instance = LikeModel.objects.filter(blog_id=blog_details["blog_id"])
                
                like_data = list(like_instance.values())
                blog_details['likes'] =len(like_data) 

            return blog_data
        except Exception as e:
            print("----FROMblog----",e)
            return False
