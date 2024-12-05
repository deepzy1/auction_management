from odoo import api,models,fields

class AssetCategory(models.Model):
    _name="asset.category"
    _description="Asset Category"


    name=fields.Char(string="Name",required=True,help="Create asset category type", placeholder="Ex.Commercial")