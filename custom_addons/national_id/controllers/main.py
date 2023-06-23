from odoo import http
from odoo.http import request

class NationalId(http.Controller):
    @http.route("/national_id/apply_form/", type="http", website=True, auth="public")
    def national_id_apply(self,  **post):
        # national_id_applicants = request.env['national.id'].sudo().search([])
        # print("national_id_applicants")
        # print(national_id_applicants)
        return "Hi our dear applicant"
        # return http.request.render('national_id.apply_form', {})
        # return request.render('apply_form', {})

    # @http.route("/national_id/create_applicant/", type="http", website=True, auth="public")
    # def national_id_create_application(self, **post):
    #     request.env['national.id'].sudo().create(post)
    #
    #     return request.render('national_id.apply_form', {})
    #  return success message

