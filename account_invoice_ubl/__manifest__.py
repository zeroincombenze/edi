# -*- coding: utf-8 -*-
# © 2016-2018 Akretion (Alexis de Lattre <alexis.delattre@akretion.com>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Account Invoice UBL',
    'version': '10.0.1.1.0',
    'category': 'Accounting & Finance',
    'license': 'AGPL-3',
    'summary': 'Generate UBL XML file for customer invoices/refunds',
    'author': 'Akretion,Odoo Community Association (OCA)',
    'website': 'http://www.akretion.com',
    'depends': [
        'account_e-invoice_generate',
        'account_payment_partner',
        'base_ubl_payment',
        ],
    'data': [
        'views/account_invoice.xml',
        'views/account_config_settings.xml',
        ],
    'post_init_hook': 'set_xml_format_in_pdf_invoice_to_ubl',
    'installable': True,
}
