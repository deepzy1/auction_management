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
            for x in request.session:
                print(f"re:{x}")
            return request.redirect('properties')
        else:
            return request.render('auction_management.login_template', {'error': 'Invalid email or password.'})



    @http.route('/auction/logout', type='http', auth="public", methods=['GET'], csrf=False)
    def logout_user(self):
        # Clear specific session key for auction user
        if 'auction_user_id' in request.session:
            print(f"Logging out user: {request.session['auction_user_id']}")
            request.session.pop('auction_user_id', None)  # Clear auction user session
        
        # Debug: Print remaining session keys
        for key in request.session:
            print(f"Remaining session key after logout: {key}")

        return request.redirect('/auction/login')  # Redirect to login page