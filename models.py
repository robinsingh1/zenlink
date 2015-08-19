from remodel.models import Model

class User(Model):
    has_many = ("Element",)
    pass

class Element(Model):
    belongs_to = ("User",)
    pass

# TODO
# Translate element_id from zenlink to cloudelement

''' 
Authorization: HTTP Headers
User JKELSDKEntgNAeZsGxY, 
Element NESLFOBeDke89w3ceaa
'''
