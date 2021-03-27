from import_export import resources
from .models import Country

class CountryResource(resources.ModelResource):
    class Meta:
        model = Country