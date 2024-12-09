from odoo import http
from odoo.http import request

class AuctionUserController(http.Controller):

    @http.route('/auction/register', type='http', auth='public', website=True)
    def auction_register(self, **kwargs):
        return request.render('auction_management.register_template', {})

    @http.route('/auction/register/submit', type='http', auth='public', methods=['POST'], website=True, csrf=False)
    def auction_register_submit(self, **kwargs):
        name = kwargs.get('name')
        email = kwargs.get('email')
        password = kwargs.get('password')
        phone = kwargs.get('phone')
        address = kwargs.get('address')

        if request.env['auction.user'].sudo().search([('email', '=', email)]):
            return request.render('auction_management.register_template', {'error': 'Email already exists.'})

        request.env['auction.user'].sudo().create({
            'name': name,
            'email': email,
            'password': password,
            'phone': phone,
            'address': address
        })
        return request.redirect('/auction/login')

    @http.route('/auction/login', type='http', auth='public', website=True)
    def auction_login(self, **kwargs):
        return request.render('auction_management.login_template', {})

    @http.route('/auction/login/submit', type='http', auth='public', methods=['POST'], website=True, csrf=False)
    def auction_login_submit(self, **kwargs):
        email = kwargs.get('email')
        password = kwargs.get('password')

        user = request.env['auction.user'].sudo().search([('email', '=', email), ('password', '=', password)], limit=1)
        if user:
            request.session['auction_user_id'] = user.id
            return request.redirect('properties')
        else:
            return request.render('auction_management.login_template', {'error': 'Invalid email or password.'})



    @http.route('/auction/listings', type='http', auth='public', website=True)
    def auction_listings(self, **kwargs):
        if not request.session.get('auction_user_id'):
            return request.redirect('/auction/login')
        properties = request.env['property.model'].sudo().search([])  # Replace 'property.model' with your actual model
        return request.render('auction_management.listings_template', {'properties': properties})
