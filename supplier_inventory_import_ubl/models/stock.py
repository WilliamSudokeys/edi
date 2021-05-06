# -*- coding: utf-8 -*-
# © 2021 David BEAL @ Akretion
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class StockQuant(models.Model):
    _inherit = "stock.quant"

    supplier_stock = fields.Float(
        string="Supplier Stock", readonly=True, related="product_id.supplier_stock"
    )
    supplier_stock_info = fields.Char(
        string="Supplier Inventory",
        readonly=True,
        related="product_id.supplier_stock_info",
    )
