{
    "name":"Auction",
    "author":" ",
    "license":"LGPL-3",
    "version":"18.0.1.0",
    "sequence":"3",
    "data":[
        "security/ir.model.access.csv",
        "views/asset_category.xml",
        "views/new_property.xml",
        "views/property_template.xml",
        "views/assets.xml",
        "views/menu.xml",
    ],

    'assets': {
            'web.assets_frontend': [
                'auction_management/static/src/css/style.css',
            ],
        },

    "installable":True,
    "application":True,
    "auto_install":False,
}