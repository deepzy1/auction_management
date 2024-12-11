from odoo import models, api, fields
from odoo.exceptions import ValidationError
from datetime import  date,datetime
import os

import logging

_logger = logging.getLogger(__name__)


class BidRules(models.Model):
    _name = "bid.rules"
    _description = "Bidding rules and description"

    name = fields.Char(string="Bid Name", required=True)
    active = fields.Boolean(default=True)
    from_price = fields.Float()
    to_price = fields.Float()
    increment_by = fields.Float()

    minimum_increment=fields.Float(string="Increment amount")

    @api.model
    def create(self, vals):
        # Ensure from_price is less than to_price on record creation
        if vals.get('from_price', 0.0) >= vals.get('to_price', 0.0):
            raise ValidationError("Start price must be less than end price.")
        return super(BidRules, self).create(vals)

    def write(self, vals):
        # Ensure from_price is less than to_price on record update
        if 'from_price' in vals and 'to_price' in vals:
            if vals['from_price'] >= vals['to_price']:
                raise ValidationError("Start price must be less than end price.")
        elif 'from_price' in vals:
            if vals['from_price'] >= self.to_price:
                raise ValidationError("Start price must be less than end price.")
        elif 'to_price' in vals:
            if self.from_price >= vals['to_price']:
                raise ValidationError("Start price must be less than end price.")
        return super(BidRules, self).write(vals)




class BidLogs(models.Model):
    _name = "bid.logs"
    _description = "Captures all the bidding information"

    user_id = fields.Many2one('res.users', string="Bidder", required=True)
    auction_id = fields.Many2one('new.auction', string="Auction", required=True)
    property_id = fields.Many2one('new.property', string="Property", related="auction_id.auction_property", store=True)
    bid_amount = fields.Float(string="Bid Amount", required=True)
    bid_time = fields.Datetime(string="Bid Time", default=lambda self: fields.Datetime.now())
    is_highest = fields.Boolean(string="Is Highest Bid", default=False)

    @api.model
    def log_bid(self, user_id, auction_id, bid_amount):
        """Logs a new bid and updates the highest bid."""
        # Check if the bid is higher than the current highest
        existing_logs = self.search([('auction_id', '=', auction_id)], order="bid_amount desc", limit=1)
        if existing_logs and bid_amount <= existing_logs.bid_amount:
            raise ValidationError("Bid amount must be higher than the current highest bid.")

        # Log the bid
        new_log = self.create({
            'user_id': user_id,
            'auction_id': auction_id,
            'bid_amount': bid_amount,
            'is_highest': True
        })

        # Update previous highest bid
        if existing_logs:
            existing_logs.is_highest = False

        # Save log to a file
        self.save_log_to_file(new_log)
        return new_log

    def save_log_to_file(self, log):
        """Save log details to a designated file."""
        log_directory = "/home/user/odoo18/custom_addons/auction_management"  # Replace with your desired path
        if not os.path.exists(log_directory):
            os.makedirs(log_directory)
        log_file_path = os.path.join(log_directory, f"auction_{log.auction_id.id}_logs.txt")

        with open(log_file_path, "a") as log_file:
            log_file.write(f"Time: {log.bid_time}, Bidder: {log.user_id.name}, "
                           f"Auction: {log.auction_id.auction_name}, "
                           f"Property: {log.property_id.name}, "
                           f"Bid: {log.bid_amount}\n")

        return log_file_path








