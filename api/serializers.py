from rest_framework import serializers
from rest_framework.fields import empty
from rest_framework.settings import api_settings
from .models import URL
class UrlSerializer(serializers.Serializer):

    """Bu serializer createurl endpointine yapılacak isteğin bodysi için yapıldı.
        run_validation() fonksiyonu;
         longUrl haricinde, başka bir field gelirse hata versin diyedir."""

    longUrl = serializers.URLField(required=True)

    def run_validation(self, data=empty):
        if data is not empty:
            unknown = set(data) - set(self.fields)
            if unknown:
                errors = ["Unknown field: {}".format(f) for f in unknown]
                raise serializers.ValidationError({
                    api_settings.NON_FIELD_ERRORS_KEY: errors,
                })

        return super(UrlSerializer, self).run_validation(data)


class UrlSerializerForExample(serializers.Serializer):

    class Meta:
        model = URL      