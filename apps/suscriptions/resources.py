# THIRD APP IMPORTS
from import_export import resources

# TOWI IMPORTS
from .models import Promos, Suscription


class PromoResource(resources.ModelResource):
    class Meta:
        model = Promos
        fields = [
            'id', 'amount', 'description', 'unique',
            'promo_code', 'suscription'
        ]


class SuscriptionResource(resources.ModelResource):
    class Meta:
        model = Suscription
        fields = (
            'id',
            'user',
            'type',
            'children',
            'start_date',
            'finished_date',
            'is_recurrent',
            'trial',
        )
