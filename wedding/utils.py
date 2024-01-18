import os
from typing import List

from dotenv import load_dotenv

from wedding import url
from wedding.routes import Route

load_dotenv()


# Menu items
menu_items: List[str] = ["Fotos", "Confirmación", "Contacto"]
url_list: List[str] = [url.GOOGLE_FOTOS_URL, url.CONFIRMATION_URL, Route.CONTACT.value]
is_external: List[bool] = [True, True, False]


# Web descriptions
title_main: str = "Web de la boda de Vicky y Álex"
title_contact: str = "Página de contacto de la web de la boda"
description_main: str = (
    "Ruta principal de la web de la boda de los novios para gestionar las invitaciones"
)
description_contact: str = "Ruta donde aparece cómo contactar con los novios"


# Initials navbar
initials_navbar: str = "V & Á"

# Header texts
title_header: str = "¡Nos casamos!"
wedding_date: List[str] = [
    "30",
    "agosto",
    "2024",
    " de ",
]


# Countdown texts
countdown_title: str = "¡Cuenta atrás!"


# Contact texts
contact_header: str = "¿Quieres contactar con nosotros?"


# Contact Info
contact_bride = dict(
    text="Vicky",
    email=os.getenv("VICKY_EMAIL"),
    phone_number=os.getenv("VICKY_PHONE"),
)
contact_groom = dict(
    text="Álex",
    email=os.getenv("ALEX_EMAIL"),
    phone_number=os.getenv("ALEX_PHONE"),
)


# Image descriptions
alt_image_one = "Foto de Vicky"
alt_image_two = "Foto de Vicky"
alt_image_home = "Icono de una casa para redireccionar a la página de inicio."
alt_image_menu = "Icono de una hamburguesa que abre el menú desplegable."
alt_flamingo_right = "Flamingo looking right"
alt_flamingo_left = "Flamingo looking left"
alt_celebration = "Foto del comedor al aire libre de La Agripina."

# SECTION TEXTS

# Confirmation
confirmation_title = "Confirmación"
confirmation_button = "Confirmar asistencia"
confirmation_text = """Seguro que tienes muchas ganas de compartir este día con nosotros.\n
    ¿Confirmas la asistencia?"""


# Celebration
celebration_title = "¿Dónde nos casamos"
celebration_button = "Abrir en Google Maps"
celebration_text = "Hemos elegido un sitio muy especial para celebrar este gran día."
wedding_place = "La Agripina"
wedding_address_street = "Callejón los Romanos, 1"
wedding_address_province = "Punta Umbría, Huelva"
wedding_schedule = "18:00"


# Bus
but_title = "Servicio de autobús"
bus_text = "Para facilitar la asistencia habrá un servicio de autobuses tanto a la ida como a la vuelta."
bus_origin_title = "Ida a la ceremonia"
bur_origin_address = "Av. Martín Alonso Pinzón, 34"
origin_address = "El Punto, Av. Martín Alonso Pinzón, 34"
origin_bus_schedule = "17:00"

bus_destination_title = "Regreso a casa"
# bus_destination_title = "Vuelta a descansar"
bus_destination_text = "Salidas de La Agripina a las 02:00 y a las 05:00 con destino en"

destination = "Destino"
destination_address = "Cjón. los Romanos, 1 (Punta Umbría, Huelva)"
destination_bus_schedule = "02:00 y 05:00"


# Photo Album
title_photo = "Álbum de Fotos"
photo_section = "¿Quieres recordar este día para siempre?"
photo_section_2 = (
    "Comparte tus fotos de la boda subiéndolas al albúm compartido de Google Fotos."
)
button_google_photo = "Abrir álbum"


# Gift
gift = "Vuestra presencia es nuestro mayor regalo, pero si queréis hacer una aportacion este es nuestro número de cuenta"
account_number = os.getenv("ACCOUNT_NUMBER")


# Contact Info
contact_bride = dict(
    text="Vicky",
    email=os.getenv("VICKY_EMAIL"),
    phone_number=os.getenv("VICKY_PHONE"),
)
contact_groom = dict(
    text="Álex",
    email=os.getenv("ALEX_EMAIL"),
    phone_number=os.getenv("ALEX_PHONE"),
)
