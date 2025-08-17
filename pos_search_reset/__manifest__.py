{
    "name": "POS – Reset Search & Clear Filters",
    "version": "1.0",
    "category": "Point of Sale",
    "summary": "Instantly clear product search and filters in the POS interface for faster product navigation.",
    "description": """ This module enhances the Odoo Point of Sale (POS) interface by adding a convenient "Reset Search" button.
        It allows POS operators to quickly clear any active product search terms and filters, instantly displaying the full product catalog again without manual effort.
        
        Key Features:
        Instantly clears product search terms and resets the product listing.
        Improves POS usability for cashiers, especially during high-traffic periods.
        Seamless integration with the standard Odoo POS interface.
        No configuration needed—install and use immediately.
        
        Ideal for:
            Retail stores, supermarkets, and any high-volume POS environments where product searches are frequent.
    """,

    "author": "Hi Spark Solutions",
    "company": "Hi Spark Solutions",
    "maintainer": "Hi Spark Solutions",
    "website": "https://www.hisparksolutions.com/",

    "depends": ["point_of_sale"],
    "demo": [],
    "data": [],
    "assets": {
        "point_of_sale._assets_pos": [
            "pos_search_reset/static/src/js/ProductScreen.js",
        ],
    },

    "images": ["static/description/banner.gif"],
    "qweb": [],
    "live_test_url": "",

    "license": "OPL-1",
    "application": True,
    "auto_install": False,
    "installable": True,
    "price": "5",
    "currency": "USD",
}
