from odoo import http
from odoo.http import request
from datetime import datetime

class AuctionWebController(http.Controller):

    @http.route('/auction/list', auth='public', website=True)
    def auction_listing(self, **kwargs):
        # Fetch all live auctions
        auctions = request.env['new.auction'].search([
            ('status', '=', 'running'),
            ('end_date', '>=', datetime.now())
        ])
        return request.render('auction_management.auction_list_template', {
            'auctions': auctions
        })

    # @http.route('/auction/<int:auction_id>/place_bid', type='json', auth='public', methods=['POST'])
    # def place_bid(self, auction_id, **kwargs):
    #     auction = request.env['new.auction'].sudo().browse(auction_id)
    #     bid_amount = float(kwargs.get('bid_amount'))

    #     if not auction.exists():
    #         return {'error': 'Auction not found'}

    #     if bid_amount <= auction.highest_bid:
    #         return {'error': 'Bid amount must be higher than the current highest bid'}

    #     # Create the bid log
    #     user_id = request.env.user.id
    #     auction.env['bid.logs'].create({
    #         'auction_id': auction.id,
    #         'user_id': user_id,
    #         'bid_amount': bid_amount,
    #     })

    #     # Update the highest bid
    #     auction.highest_bid = bid_amount

    #     return {'new_highest_bid': auction.highest_bid}

    @http.route('/auction/place_bid', type='json', auth='public', methods=['POST'], csrf=False)
    def place_bid(self, auction_id, bid_amount):
        auction = request.env['new.auction'].sudo().browse(auction_id)
        
        if not auction:
            return {'success': False, 'error_message': 'Auction not found'}

        # Convert bid_amount to float if passed as string
        try:
            bid_amount = float(bid_amount)
        except ValueError:
            return {'success': False, 'error_message': 'Invalid bid amount'}

        # Check if the bid is greater than the current highest bid
        if bid_amount <= auction.highest_bid:
            return {'success': False, 'error_message': 'Bid amount must be higher than the current highest bid'}

        # Update the auction's highest bid
        auction.write({'highest_bid': bid_amount})

        # Log the bid in bid.logs model
        user_id = request.env.user.id  # Get the current user ID
        request.env['bid.logs'].sudo().create({
            'auction_id': auction.id,
            'user_id': user_id,
            'bid_amount': bid_amount,
        })

        # Return the new highest bid to the client-side to update the UI
        return {
            'success': True,
            'new_highest_bid': bid_amount
        }
