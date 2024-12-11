from odoo import fields,api,models

class NewProperty(models.Model):
    _name="new.property"
    _description="New Property"

    name=fields.Char(string="Name", help="Property Name", required=True)
    auction_id=fields.Many2one("new.auction", string="auction", ondelete="cascade")
    type=fields.Many2one('asset.category', string="Type", required=True)
    image_ids=fields.One2many('property.image', 'property_id', string="Images")
    address=fields.Char(string="Address", required=True)
    city=fields.Char(string="City", required=True)
    pincode=fields.Char(string="Pincode", required=True)
    district=fields.Char(string="District", required=True)
    state=fields.Char(string="State", required=True)
    price=fields.Float(string="Price", required=True)
    document=fields.Binary(string="Document",required=True)
    property=fields.Many2one('bid.logs', string="Property", ondelete="cascade")



class PropertyImage(models.Model):
    _name="property.image"
    _description=" Property Images"


    image=fields.Binary(string="Image", attachment=True)
    property_id=fields.Many2one('new.property', string="Property", ondelete="cascade")




