# api/serializers.py
from rest_framework import serializers
from collections import OrderedDict
from orders.models import Orders
from accesses.models import Accesses, Services
from subscriptions.models import Subscriptions, Equipment
from endpoints.models import Endpoints
from option82.models import Option82
from dhcplookup.models import Dhcplookup

serviceDetailField = ('service', 'connection', 'available', 'disconnection', 'forcedTakeoverPossible', )


class  EquipmentDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Equipment
        fields = ('vendorId', 'macAddress')


class SubscriptionListSerializer(serializers.ModelSerializer):
    service = serializers.StringRelatedField(many=False)
    equipment = EquipmentDetailSerializer(read_only=True, many=True)

    class Meta:
        model = Subscriptions
        fields = ('__all__')


    # https://stackoverflow.com/questions/27015931/remove-null-fields-from-django-rest-framework-response
    # Dont show NULL values
    def to_representation(self, instance):
        result = super().to_representation(instance)
        return OrderedDict([(key, result[key]) for key in result if result[key] is not None])


class SubscriptionDetailSerializer(serializers.ModelSerializer):
    service = serializers.StringRelatedField(many=False)
    equipment = EquipmentDetailSerializer(read_only=True, many=True)

    class Meta:
        model = Subscriptions
        fields = ('__all__')


    # https://stackoverflow.com/questions/27015931/remove-null-fields-from-django-rest-framework-response
    # Dont show NULL values
    def to_representation(self, instance):
        result = super().to_representation(instance)
        return OrderedDict([(key, result[key]) for key in result if result[key] is not None])


class ServiceDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Services
        #fields = ('__all__')
        fields = serviceDetailField


    # https://www.thetopsites.net/article/52169173.shtml
    # If value NULL show empty string
    def to_representation(self, instance):
        data = super().to_representation(instance)
        if not data['disconnection']:
            data['disconnection'] = ""
        return data


class AccessListSerializer(serializers.ModelSerializer):
    services = ServiceDetailSerializer(many=True, read_only=True)

    class Meta:
        model = Accesses
        fields = ('__all__')

    # https://stackoverflow.com/questions/52169173/django-rest-framework-how-to-substitute-null-with-empty-string
    # If value NULL show empty string
    def to_representation(self, instance):
        data = super().to_representation(instance)
        for key, value in data.items():
            try:
                if not value:
                    data[key] = ""
            except KeyError:
                pass
        return data


class AccessDetailSerializer(serializers.ModelSerializer):
    services = ServiceDetailSerializer(many=True, read_only=True)
    subscriptions = SubscriptionDetailSerializer(read_only=True, many=True)

    class Meta:
        model = Accesses
        fields = ('__all__')

    # https://stackoverflow.com/questions/52169173/django-rest-framework-how-to-substitute-null-with-empty-string
    # If value NULL show empty string
    def to_representation(self, instance):
        data = super().to_representation(instance)
        for key, value in data.items():
            try:
                if not value:
                    data[key] = ""
            except KeyError:
                pass
        return data


class OrderListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Orders
        fields = ('__all__')


class OrderDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Orders
        fields = ('__all__')


class EndpointListSerializer(serializers.ModelSerializer):
    unsupportedFields = serializers.StringRelatedField(many=True)
    class Meta:
        model = Endpoints
        #fields = ('__all__')
        fields = ('name', 'endpoint', 'version', 'documentation', \
                  'note', 'unsupportedFields')

    # https://stackoverflow.com/questions/27015931/remove-null-fields-from-django-rest-framework-response
    # Dont show NULL values
    def to_representation(self, instance):
        result = super().to_representation(instance)
        return OrderedDict([(key, result[key]) for key in result if result[key] is not None])


class Option82DetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Option82
        fields = ('accessId',)


class DhcplookupListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Dhcplookup
        fields = ('accessId',)

