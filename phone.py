import phonenumbers
from phonenumbers import geocoder, timezone, carrier

service_provider = phonenumbers.parse("+91 enter number")

# this will print the service provider name
print(carrier.name_for_number(service_provider,'en'))

# this will print the timezone
print(timezone.time_zones_for_number(service_provider))

# this will print the country name
print(geocoder.description_for_number(service_provider, 'en'))