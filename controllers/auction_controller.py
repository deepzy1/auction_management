from odoo import http
from odoo.http import request

class AuctionWebsite(http.Controller):

    @http.route('/auction/home', type='http', auth='public', website=True)
    def auction_home(self):
        return request.render('auction_management.home_page_test', {})
