from django.core.exceptions import ValidationError

# Create your models here.
def validate_content(value):
	content = value
	if content == "abc":
		raise ValidationError("Cannot be ABC")
	return value