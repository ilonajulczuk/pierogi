from django.core.exceptions import ObjectDoesNotExist
from django.utils.encoding import smart_text

from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from food.models import Food, Place, FoodUser, Company


class CompanySlugRelatedField(serializers.SlugRelatedField):
    def to_internal_value(self, data):
        try:
            return self.get_queryset().get(
                **{
                    self.slug_field: data,
                    "company_id": self.context['company_id']
                }
            )
        except ObjectDoesNotExist:
            self.fail('does_not_exist', slug_name=self.slug_field, value=smart_text(data))
        except (TypeError, ValueError):
            self.fail('invalid')


class FoodSerializer(ModelSerializer):
    place = CompanySlugRelatedField(
        queryset=Place.objects.all(),
        slug_field='id',
        read_only=False,
        required=False
    )

    class Meta:
        model = Food
        fields = (
            'id',
            'name',
            'giver',
            'taker',
            'place',
            'image'
        )


class FoodUserSerializer(ModelSerializer):
    company = serializers.SlugRelatedField(
        slug_field='name',
        read_only=True
    )

    class Meta:
        model = FoodUser
        fields = (
            'id',
            'name',
            'should_be_notified',
            'company'
        )
