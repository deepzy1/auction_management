from odoo import api,fields,models
from datetime import date,datetime


class NewAuction(models.Model):
    _name="new.auction"
    _description="New Auction"

    auction_name=fields.Char(string="Auction Name", required=True, help="Enter auction name")
    auction_property=fields.Many2one("new.property", string="Auction Type")
    initial_price=fields.Float(string="Initial Price")
    reserve_price=fields.Float(string="Reserve Price")
    start_date=fields.Datetime(string="Start DateTime")
    end_date=fields.Datetime(string="End DateTime")
    extend_by=fields.Datetime(string="Extend By")