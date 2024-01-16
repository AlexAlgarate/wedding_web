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


# Web descriptions
title_main: str = "Web de la boda de los novios"
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
countdown_heading: str = "¡Cuenta atrás!"
save_date_button: str = "Guardar fecha"


# Contact texts
contact_header: str = "¿Quieres contactar con nosotros?"
contact_one: str = "Vicky"
contact_two: str = "Álex"


# Contact Info
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


# Image descriptions
alt_image_one = "Foto de Vicky"
alt_image_two = "Foto de Vicky"
alt_image_home = "Icono de una casa para redireccionar a la página de inicio."
alt_image_menu = "Icono de una hamburguesa que abre el menú desplegable."
alt_flamingo_right = "Flamingo looking right"
alt_flamingo_left = "Flamingo looking left"
alt_celebration = "Foto del comedor al aire libre de La Agripina."

# SECTION TEXTS

# Celebration
wedding_place = "La Agripina"
wedding_address = "Cjón. los Romanos, 1 (Punta Umbría, Huelva)"
wedding_schedule = "18:00"

# Gift
gift = "Vuestra presencia es nuestro mayor regalo, pero si queréis hacer una aportacion este es nuestro número de cuenta"
account_number = os.getenv("ACCOUNT_NUMBER")

# Confirmation
button_confirmation = "Se ruega confirmación"
main_text_confirmation = (
    "Sabemos que tienes muchas ganas de venir, pero antes...¿confirmas la asistencia?"
)

# Photo
title_photo = "Álbum de Fotos"
photo_section = (
    "Publica fotos subiéndolas al albúm compartido de Google Fotos de los novios."
)
button_google_photo = "Abrir álbum"

# Bus destination

destination = "Destino"
destination_address = "Cjón. los Romanos, 1 (Punta Umbría, Huelva)"
destination_bus_schedule = "02:00 y 05:00"

# Bus origin
origin = "Origen"
origin_address = "El Punto, Av. Martín Alonso Pinzón, 34"
origin_bus_schedule = "17:00"
