from odoo import http
from odoo.http import request

class PropertyController(http.Controller):

    @http.route('/property/add', type='http', auth='user', website=True)
    def add_property_form(self, **kwargs):
        categories = request.env['asset.category'].sudo().search([])
        return request.render('property_management.add_property_form', {'categories': categories})

    @http.route('/property/add/submit', type='http', auth='user', methods=['POST'], website=True, csrf=False)
    def submit_property(self, **kwargs):
        name = kwargs.get('name')
        type_id = kwargs.get('type')
        address = kwargs.get('address')
        city = kwargs.get('city')
        pincode = kwargs.get('pincode')
        district = kwargs.get('district')
        state = kwargs.get('state')
        price = kwargs.get('price')
        document = kwargs.get('document')

        property_vals = {
            'name': name,
            'type': int(type_id),
            'address': address,
            'city': city,
            'pincode': pincode,
            'district': district,
            'state': state,
            'price': float(price),
            'document': document,
        }
        property_record = request.env['new.property'].sudo().create(property_vals)

        # Save property images
        for file in request.httprequest.files.getlist('images'):
            image = file.read()
            request.env['property.image'].sudo().create({
                'property_id': property_record.id,
                'image': image,
            })

        return request.redirect('/property/list')

    @http.route('/property/list', type='http', auth='user', website=True)
    def property_list(self, **kwargs):
        properties = request.env['new.property'].sudo().search([])
        return request.render('property_management.property_list', {'properties': properties})
