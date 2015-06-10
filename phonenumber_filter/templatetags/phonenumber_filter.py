import phonenumbers

@register.filter(name='phonenumber')
def phonenumber(value, country=None):
    return phonenumbers.parse(value, country)
