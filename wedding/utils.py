import os
from typing import List

from dotenv import load_dotenv

from wedding import urls as url
from wedding.routes import Route

load_dotenv()
# Menu items
menu_items: List[str] = ["Fotos", "Confirmación", "Contacto"]
url_list: List[str] = [url.GOOGLE_FOTOS_URL, url.CONFIRMATION_URL, Route.CONTACT.value]
is_external: List[bool] = [True, True, False]


# TEXTs
title_main: str = "Web de la boda de los novios"
title_contact: str = "Página de contacto de la web de la boda"
description_main: str = "Parte principal de la web de la boda de los novios para gestionar las invitaciones"
description_contact: str = "Parte de la web donde aparece cómo contactar con los novios"

main_text: str = """
Lorem Ipsum es simplemente el texto de relleno de las imprentas y archivos de texto.
Lorem Ipsum ha sido el texto de relleno estándar de las industrias desde el año 1500,
cuando un impresor (N. del T. persona que se dedica a la imprenta) desconocido usó una
galería de textos y los mezcló de tal manera que logró hacer un libro de textos especimen.
No sólo sobrevivió 500 años, sino que tambien ingresó como texto de relleno en documentos
electrónicos, quedando esencialmente igual al original. Fue popularizado en los 60s
con la creación de las hojas "Letraset", las cuales contenian pasajes de Lorem Ipsum,
y más recientemente con software de autoedición,
como por ejemplo Aldus PageMaker, el cual incluye versiones de Lorem Ipsum.
"""

initials_navbar: str = "V & Á"
title_header: str = "¡Nos casamos!"

wedding_date: List[str] = [
    "30",
    "agosto",
    "2024",
    " de ",
]
countdown_heading: str = "¡Cuenta atrás!"
save_date_button: str = "Guardar fecha"


contact_header: str = "¿Quieres contactar con nosotros?"
contact_one: str = "Vicky"
contact_two: str = "Álex"

contact_1 = dict(
    text="Vicky",
    email=os.getenv("VICKY_EMAIL"),
    phone_number=os.getenv("VICKY_PHONE"),
)

contact_2 = dict(
    text="Álex",
    email=os.getenv("ALEX_EMAIL"),
    phone_number=os.getenv("ALEX_PHONE"),
)
alt_image_one = "Foto de Vicky"
alt_image_two = "Foto de Vicky"
alt_image_home = "Icono de una casa para redireccionar a la página de inicio."
alt_image_menu = "Icono de una hamburguesa que abre el menú desplegable."
