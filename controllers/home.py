from odoo import http
from odoo.http import request

class AuctionUserController(http.Controller):
    @http.route('/home', type='http', auth='public', website=True)
    def homepage(self, **kwargs):
        return request.render('auction_management.home_template',{})
