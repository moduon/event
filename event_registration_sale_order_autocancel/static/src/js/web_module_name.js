/* Copyright 2024 Moduon Team S.L.
 * License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl-3.0) */

odoo.define("web_module_name.objectName", function (require) {
    "use strict";

    var core = require("web.core");

    core.bus.on("web_client_ready", null, function () {
        // Script that will be loaded when document is ready
    });

    function methodToExport() {
        // This method will be exported as
        // require('module_name.object_name').methodToExport
    }

    return { methodToExport: methodToExport };
});
