# Copyright 2024 Moduon Team S.L.
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl-3.0)

from odoo import api, models


class WizardModel(models.TransientModel):
    _name = "module.wizard_model"
    _description = "Wizard Name"

    @api.multi
    def action_accept(self):
        self.ensure_one()
        self.do_something_useful()
