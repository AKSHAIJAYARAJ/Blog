from .models import LikeModel

class LikeManager:

    def get(self,filters:dict = None):
        try:
            instance = LikeModel.objects.filter(**filters).all()
            user_data = list(instance.values())
            return user_data
        except Exception as e:
            print("-----User EPTN-------",e)
            return False
    def post(self,payload : dict = None):
        try:
            instance = LikeModel(**payload)
            instance.save()
            return True
        except Exception as e:
            print("-----User EPTN-------",e)
            return False
    def put(self,payload : dict, filters:dict):
        try:
            instance = LikeModel.objects.get(**filters)
            for key, value in payload.items():
                setattr(instance, key, value)
            instance.save()
            return True
        except Exception as e:
            print("-----User EPTN-------",e)
            return False
    def delete(self,filters:dict):
        try:
            instance = LikeModel.objects.filter(**filters)
            instance.delete()
        except Exception as e:
            print("-----User EPTN-------",e)
            return False