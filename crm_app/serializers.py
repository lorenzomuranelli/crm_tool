# crm_app/serializers.py
from rest_framework import serializers
from .models import Lead, Contact, Opportunity

class LeadSerializer(serializers.ModelSerializer):
    contacts = serializers.StringRelatedField(many=True, read_only=True)
    opportunities = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Lead
        fields = ['id', 'name', 'email', 'phone', 'company', 'contacts', 'opportunities', 'created_at', 'updated_at']

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['id', 'lead', 'first_name', 'last_name', 'email', 'phone', 'created_at', 'updated_at']

class OpportunitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Opportunity
        fields = ['id', 'lead', 'name', 'stage', 'amount', 'close_date', 'created_at', 'updated_at']