from rest_framework import serializers
from bank.models import Branch


class BranchSerializer(serializers.ModelSerializer):

    class Meta:
        model = Branch
        fields = '__all__'
