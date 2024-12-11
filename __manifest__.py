{
    "name":"Auction",
    "author":" ",
    "license":"LGPL-3",
    "version":"18.0.1.0",
    "sequence":"3",
    "data":[
        "security/ir.model.access.csv",
        "data/crone.xml",
        "base.xml",
        "views/asset_category.xml",
        "views/new_property.xml",
        "views/property_template.xml",
        "views/assets.xml",
        "views/auction_user_views.xml",
        "views/user_registartion.xml",
        "views/login.xml",
        "views/add_property.xml",
        "views/bid_rules_views.xml",
        "views/home.xml",
        "views/new_auction.xml",
        "views/bid_logs.xml",

        # "views/auctions.xml",
        "views/menu.xml",
    ],

    'assets': {
            'web.assets_frontend': [
                'auction_management/static/src/css/style.css',
                'auction_management/static/src/js/script.js',
                'auction_management/static/src/js/auction.js',
                'auction_management/static/src/css/auction.css',
                'auction_management/static/src/css/auction_style.css',
                'auction_management/static/src/js/auction_script.js',
                'auction_management/static/src/js/home.js',
            ],
        },

    "installable":True,
    "application":True,
    "auto_install":False,
}