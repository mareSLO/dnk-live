#!/usr/bin/env python
import os
import jinja2
import webapp2


template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=False)


class BaseHandler(webapp2.RequestHandler):

    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))

    def render_template(self, view_filename, params=None):
        if not params:
            params = {}
        template = jinja_env.get_template(view_filename)
        self.response.out.write(template.render(params))


class MainHandler(BaseHandler):
    def get(self):
        self.render_template("hello.html")

class DNAHandler(BaseHandler):
    def post(self):
        polje = self.request.get("polje")

        Crni_lasje = "CCAGCAATCGC"
        Rjavi_lasje = "GCCAGTGCCG"
        Korencek = "TTAGCTATCGC"

        Moski = "TGCAGGAACTTC"
        Zenska = "TGAAGGACCTTC"

        Belec = "AAAACCTCA"
        Crnec = "CGACTACAG"
        Azijec = "CGCGGGCCG"

        Modre_oci = "TTGTGGTGGC"
        Zelene_oci = "GGGAGGTGGC"
        Rjave_oci = "AAGTAGTGAC"

        Kvadraten_obraz = "GCCACGG"
        Okrogel_obraz = "ACCACAA"
        Ovalen_obraz = "AGGCCTCA"

        if polje.find(Crni_lasje) != -1:
            lasje = "Barva las je crna"
        elif polje.find(Rjavi_lasje) != -1:
            lasje = "Barva las je rjava"
        elif polje.find(Korencek) != -1:
            lasje = "Barva las je oranzna"

        if polje.find(Kvadraten_obraz) != -1:
            obraz = "Obraz je kvadraten"
        elif polje.find(Okrogel_obraz) != -1:
            obraz = "Obraz je okrogel"
        elif polje.find(Ovalen_obraz) != -1:
            obraz = "Obraz je ovalen"

        if polje.find(Modre_oci) != -1:
            oci = "Barva oci je modra"
        elif polje.find(Zelene_oci) != -1:
            oci = "Barva oci je zelena"
        elif polje.find(Rjave_oci) != -1:
            oci = "Barva oci je rjava"

        if polje.find(Moski) != -1:
            spol = "Moski spol"
        elif polje.find(Zenska) != -1:
            spol = "Zenski spol"

        if polje.find(Belec) != -1:
            rasa = "Belec"
        elif polje.find(Crnec) != -1:
            rasa = "Crnec"
        elif polje.find(Azijec) != -1:
            rasa = "Azijec"

        params = {"polje": polje, "lasje": lasje, "obraz": obraz, "oci": oci, "spol": spol, "rasa": rasa}
        self.render_template("tat.html", params)

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/tat', DNAHandler)
], debug=True)
