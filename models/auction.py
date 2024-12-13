from odoo import api,fields,models
from datetime import date,datetime


class NewAuction(models.Model):
    _name="new.auction"
    _description="New Auction"
    _rec_name="auction_name"

    auction_name=fields.Char(string="Auction Name", required=True, help="Enter auction name")
    auction_property=fields.Many2one("new.property", string="Property")
    initial_price=fields.Float(string="Initial Price")
    reserve_price=fields.Float(string="Reserve Price")
    start_date=fields.Datetime(string="Start DateTime")
    end_date=fields.Datetime(string="End DateTime")
    extend_by=fields.Datetime(string="Extend By")
    bid_ids=fields.One2many('bid.logs', 'auction_id', string="Bid", ondelete="cascade")
    highest_bid=fields.Float(string="Highest_bid", compute="_compute_highest_bid", default=lambda self: self.initial_price)

    status=fields.Selection([
        ('draft','Draft'),('confirmed','Confirmed'),('running','Running'),
    ('extended','Extended'),('closed','Closed'),('finished','Finished')
    ],default='draft'
    )

    @api.depends("bid_ids.bid_amount")
    def _compute_highest_bid(self):
        for rec in self:
            if rec.bid_ids:
                rec.highest_bid=max(rec.bid_ids.mapped('bid_amount'))
            else:
                rec.highest_bid=rec.initial_price
            


    def action_confirm(self):
        for rec in self:
            rec.status='confirmed'

    def action_run(self):
        for rec in self:
            print(rec)
            rec.status='running'

    @api.model
    def auto_update_status(self):
        """ Update status to 'running' if the current datetime matches start_date """
        auction_to_start = self.search([('start_date', '<=', fields.Datetime.now()), ('status', '=', 'confirmed')])
        print(f"time: {fields.Datetime.now()}")
        for auction in auction_to_start:
            auction.status = 'running'
        auction_to_end=self.search([('end_date', '<=', fields.Datetime.now()),('status', '=', 'running')])
        for auction in auction_to_end:
            auction.status='finished'

    def action_extend(self):
        for rec in self:
            rec.status='extended'

    def action_close(self):
        for rec in self:
            rec.status='closed'