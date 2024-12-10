from odoo import http
from odoo.http import request
from datetime import datetime, timedelta
import json


class AuctionController(http.Controller):

    @http.route('/auctions', type='http', auth="public", website=True)
    def list_auctions(self, **kwargs):
        """Render the auction list page."""
        auctions = request.env['new.auction'].search([])
        return request.render('auction_management.auction_list', {'auctions': auctions})

    @http.route('/auction/<int:auction_id>', type='http', auth="public", website=True)
    def auction_details(self, auction_id, **kwargs):
        """Render the auction details page."""
        auction = request.env['new.auction'].browse(auction_id)
        if not auction.exists():
            return request.not_found()
        return request.render('auction_management.auction_detail', {'auction': auction})

    @http.route('/auction/place_bid', type='json', auth="user")
    def place_bid(self, auction_id, bid_amount):
        """Handle placing a bid."""
        try:
            auction = request.env['new.auction'].browse(auction_id)
            if not auction.exists():
                return {"error": "Auction not found"}

            user_id = request.env.user.id
            bid_log = request.env['bid.logs'].sudo().log_bid(user_id, auction_id, float(bid_amount))

            return {"success": True, "highest_bid": bid_log.bid_amount}
        except Exception as e:
            return {"error": str(e)}
