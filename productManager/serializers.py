from rest_framework import serializers
from .models import PUser, Product,ProductMovements,Location
from drf_writable_nested import WritableNestedModelSerializer


class UserSerializer(serializers.ModelSerializer):
       
    class Meta:
        model = PUser
        fields = ['id', 'name', 'email', 'email_verified_at', 'password', 'created_at', 'updated_at']
        


class LocationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Location
        fields = ['location_id', 'product_id', 'locate', 'created_at', 'updated_at' ]
        

class ProductMovementSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ProductMovements
        fields =  ['id', 'product_id', 'from_location','to_location', 'status', 'created_at', 'updated_at' ]
            
            
class ProductSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
    location = LocationSerializer(many=True)
    movelocation =  ProductMovementSerializer(many=True)
    
    class Meta:
        model =  Product
        fields = ['Product_id', 'product_name','product_image', 'added_by', 'created_at', 'updated_at','location', 'movelocation' ]
        

        
        
        
# class ListSerializer(serializers.Serializer):
#     # devices = DeviceSerializer(many=True)
#     # activities = StatusActivitySerializer(many=True)

#     class Meta:
#         model = [Device, StatusActivity]
#         fields = ['device_id', 'device_name', 'changed_to', 'modified_at']
    
    
    