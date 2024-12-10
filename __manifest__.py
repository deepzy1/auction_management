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
        "views/auction_user_views.xml",
        "views/user_registartion.xml",
        "views/login.xml",
        "views/add_property.xml",
        "views/bid_rules_views.xml",
        "views/new_auction.xml",
        "views/bid_logs.xml",
        "views/auctions.xml",
        "views/menu.xml",
    ],

    'assets': {
            'web.assets_frontend': [
                'web/static/lib/owl/owl.js',  # Ensure core dependencies are included
                'web/static/src/js/framework/jquery.js',  # Include jQuery if needed
                'web/static/src/js/core/ajax.js',  # Required for AJAX
                'auction_management/static/src/css/style.css',
                'auction_management/static/src/js/script.js',
                'auction_management/static/src/js/auction.js',
            'auction_management/static/src/css/auction.css',
            ],
        },

    "installable":True,
    "application":True,
    "auto_install":False,
}