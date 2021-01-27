from rest_framework import serializers
from first_app.models import Student


class StudentSerializer(serializers.ModelSerializer):

    url = serializers.HyperlinkedIdentityField(
        view_name='GetUpdateDelete',
        lookup_field='id'
    )

    class Meta:
        model = Student
        fields = ["url", "id", "first_name", "last_name", "number"]
