{
    "name":"Auction",
    "author":" ",
    "license":"LGPL-3",
    "version":"18.0.1.0",
    "sequence":"3",
    "data":[
        "security/ir.model.access.csv",
        "data/cron.xml",
        "views/asset_category.xml",
        "views/new_property.xml",
        "views/new_auction.xml",
        "views/bid_logs.xml",
        "views/bid_rules_view.xml",
        # "views/property_template.xml",
        # "views/assets.xml",
        "views/auction_user_views.xml",
        # "views/user_registartion.xml",
        # "views/login.xml",
        # "views/add_property.xml",
        "views/template/home.xml",
        "views/template/user_registration.xml",
        "views/template/login.xml",
        "views/template/properties.xml",
        "views/menu.xml",
    ],

    'assets': {
            'web.assets_frontend': [
                'auction_management/static/src/css/home.css',
                'auction_management/static/src/css/user.css',
            ],
        },

    "installable":True,
    "application":True,
    "auto_install":False,
}