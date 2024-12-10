from odoo import api,fields,models
from datetime import date,datetime


class NewAuction(models.Model):
    _name = "new.auction"
    _description = "New Auction"

    auction_name = fields.Char(string="Auction Name", required=True, help="Enter auction name")
    auction_property = fields.Many2one("new.property", string="Select Property", required=True)
    initial_price = fields.Float(string="Initial Price", required=True)
    reserve_price = fields.Float(string="Reserve Price", required=True)
    start_date = fields.Datetime(string="Start DateTime", required=True)
    end_date = fields.Datetime(string="End DateTime", required=True)
    extend_by = fields.Datetime(string="Extend By")
    # highest_bid = fields.Float(string="Highest Bid", default=0.0, readonly=True)
    bids = fields.One2many('bid.logs', 'auction_id', string="Bid Logs")

    highest_bid = fields.Float(string="Highest Bid", compute="_compute_highest_bid", store=True)

    @api.depends('bid_logs_ids')
    def _compute_highest_bid(self):
        for auction in self:
            highest_bid = auction.bid_logs_ids.filtered(lambda log: log.is_highest).mapped('bid_amount')
            auction.highest_bid = highest_bid[0] if highest_bid else 0.0

    bid_logs_ids = fields.One2many('bid.logs', 'auction_id', string="Bid Logs")


