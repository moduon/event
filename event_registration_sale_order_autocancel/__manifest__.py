# Copyright 2024 Moduon Team S.L.
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl-3.0)

{
    "name": "Event Registration Sale Order Autocancel",
    "summary": "Ensure sales order alignment with event registrations: Automatically cancel or adjust sales orders when event registrations are canceled.",
    "version": "16.0.1.0.0",
    "development_status": "Alpha",
    "category": "Sales/Sales",
    "website": "https://github.com/OCA/event",
    "author": "Moduon, Odoo Community Association (OCA)",
    "maintainers": ["edlopen", "rafaelbn"],
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "preloadable": True,
    "auto_install": False,
    "pre_init_hook": "pre_init_hook",
    "post_init_hook": "post_init_hook",
    "post_load": "post_load",
    "uninstall_hook": "uninstall_hook",
    "external_dependencies": {
        "python": [],
        "bin": [],
    },
    "depends": [
        "base",
    ],
    "excludes": [
        "incompatible_module_name",
    ],
    "data": [
        "security/some_model_security.xml",
        "security/ir.model.access.csv",
        "views/report_name.xml",
        "views/model_name_view.xml",
        "wizards/wizard_model_view.xml",
    ],
    "demo": [
        "demo/assets.xml",
        "demo/model_name_demo.xml",
    ],
    "assets": {
        "web.assets_backend": [
            "module/static/src/css/module_name.css",
            "module/static/src/js/module_name.js",
        ],
        "web.qunit_suite_tests": [
            "module/static/src/js/*.tour.js",
        ],
    },
}
