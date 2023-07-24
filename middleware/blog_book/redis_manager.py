# MODULE DETAILS
# __________________________________________________________________________________________________________________________
# MODULE NAME   : RedisManager
# VERSION       : 1.0
# SYNOPSYS      : This module is developed to perform redis operations.
# AUTHOR        : AKSHAI JAYARAJ
# CREATED ON    : 2023-MAY-27
# METHODS       : 
# 
# ENHANCEMENT HISTORY
# __________________________________________________________________________________________________________________________
# AUTHOR        : <AUTHOR>
# CREATED ON    : <CREATED ON>
# METHODS       : <METHODS>
# __________________________________________________________________________________________________________________________

from redis import Redis
import json 
from django.conf import settings

class RedisManager:

    def __init__(self):
        self.redis_client = Redis(
            port=settings.EXTERNAL_DB_CONFIG['redis']['port'],
            # password='',
            host=settings.EXTERNAL_DB_CONFIG['redis']['host'],
            # username=redis_conf['redis']['user-name']
            )
        
    def upsert(self,value ,key :str):
        try:
            value = json.dumps(value)
            self.redis_client.set(key,value)
            return True
        except:
           return False 
    
    def get(self,key : str):
        try:
            return json.loads(self.redis_client.get(key))
        except:
           return False 

    def delete(self,key : str):
        try:
            self.redis_client.delete(key)
            return True
        except:
           return False 
    def append(self,value ,key :str):
        try:
            current_data  = self.get(key=key)

            if isinstance(current_data,list) and isinstance(value,list):
                
                current_data.extend(value)

            elif isinstance(current_data,dict) and isinstance(value,dict):

                current_data.update(value)
            else:
                raise TypeError("Cannot concat different data types")
            self.upsert(value=current_data,key=key)
            return True
        except:
           return False 