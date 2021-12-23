# Copyright 2021 Akretion (https://www.akretion.com).
# @author Sébastien BEAU <sebastien.beau@akretion.com>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).


from odoo.addons.component.core import Component


class InputReceive(Component):
    _inherit = "edi.component.input.mixin"
    _name = "edi.input.receive"
    _usage = "webservice.receive"

    def receive(self):
        adapter = self.collection.webservice_backend_id._get_adapter()
        return adapter.get(path=self.work.path)
