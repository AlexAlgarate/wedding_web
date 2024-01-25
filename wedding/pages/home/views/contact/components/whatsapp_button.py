from typing import Dict

import reflex as rx

from wedding import utils
from wedding.routes import IconRoutes as icon
from wedding.styles import style


def whatsapp_button(contact_info: Dict[str, str]) -> rx.Component:
    return rx.link(
        rx.button(
            rx.flex(
                rx.image(src=icon.ICON_WHATSAPP.value, alt=utils.alt_whatsapp),
                rx.text(
                    f"Abrir Whatsapp con {contact_info.get('name')}",
                    style=style.TEXT_WHATSAPP_STYLE,
                ),
                style=style.WHATSAPP_COMP_STYLE,
            ),
            style=style.BUTTON_WHATSAPP_STYLE,
        ),
        href=f"https://wa.me/34{contact_info.get('phone_number').replace(' ', '')}",
        is_external=True,
    )
