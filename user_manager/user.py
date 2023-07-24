from .models import UserModel

class User:

    def get(self,filters:dict = None):
        try:
            instance = UserModel.objects.filter(**filters).all()
            user_data = list(instance.values())
            return user_data
        except Exception as e:
            print("-----User EPTN-------",e)
            return False
    def post(self,payload : dict = None):
        try:
            instance = UserModel(**payload)
            instance.save()
            return True
        except Exception as e:
            print("-----User EPTN-------",e)
            return False
    def put(self,payload : dict, user_id : int):
        try:
            instance = UserModel.objects.get(user_id = user_id)
            for key, value in payload.items():
                setattr(instance, key, value)
            instance.save()
        except Exception as e:
            print("-----User EPTN-------",e)
            return False
    def delete(self,user_id : int):
        pass