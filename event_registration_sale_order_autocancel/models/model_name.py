# Copyright 2024 Moduon Team S.L.
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl-3.0)

from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = "sale.order"

    def event_registration_canceled(self, registration_id, **kwargs):
        # Get the canceled event registration
        registration = self.env['event.event_registration'].browse(registration_id)

        # Check if the order is already invoiced
        if self.invoice_ids:
            return

        # Check if the cancellation affects the entire order
        if len(registration.event_id.event_registration_ids) == 1:
            # Cancel the sales order
            self.cancel()
            self.message_post(
                body=f"Sales order canceled due to cancellation of event registration: {registration.id}"
            )
        else:
            # Reduce the quantity of the canceled registration's product
            order_line = self.order_line.filtered(
                lambda line: line.product_id == registration.event_id.product_id
            )
            if order_line:
                order_line.quantity -= 1
                self.message_post(
                    body=f"Sales order quantity reduced due to cancellation of event registration: {registration.id}"
                )
