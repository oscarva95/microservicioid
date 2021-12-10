from rest_framework import serializers
from authApp.models.createid import createid


class createidSerializer(serializers.ModelSerializer):
    class Meta:
        model = createid
        fields = ['id','namepc', 'ubicationpc']

    def to_representation(self, obj):
        Createid= createid.objects.get(id=createid.id)
     
        return{
            'id'            : Createid.id,
            'namepc'         : Createid.namepc,
            'ubicationpc'      : Createid.ubicationpc,
            
        }