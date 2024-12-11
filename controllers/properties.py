# controllers/property_controller.py
from odoo import http
from odoo.http import request


class PropertyController(http.Controller):
    @http.route('/properties', type='http', auth='public', website=True)
    def property_list(self, **kwargs):
        properties = request.env['new.property'].sudo().search([])
        return request.render('auction_management.property_list_template', {
            'properties': properties,
        })



