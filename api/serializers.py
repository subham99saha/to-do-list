from rest_framework import serializers
from api.models import *

class todoSerializer(serializers.ModelSerializer):
	class Meta:
		model = todo
		fields = "__all__"