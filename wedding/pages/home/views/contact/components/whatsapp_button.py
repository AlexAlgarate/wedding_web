from typing import Dict

import reflex as rx

from wedding.routes import IconRoutes as icon


def whatsapp_button(contact_info: Dict[str, str]) -> rx.Component:
    return rx.link(
        rx.button(
            rx.flex(
                rx.image(src=icon.ICON_WHATSAPP.value, alt="Icono de Whatsapp"),
                rx.text(
                    f"Abrir Whatsapp con {contact_info.get('name')}",
                    color="#4F1F7E",
                    text_align="center",
                    font_variant_numeric="lining-nums proportional-nums",
                ),
                padding="8px 24px 8px 16px",
                justify_content="center",
                align_items="center",
                gap="8px",
                align_self="stretch",
            ),
            border_radius=" 4px",
            border=" 2px solid #4F1F7E",
            background=" #FFF",
        ),
        href=f"https://wa.me/34{contact_info.get('phone_number').replace(' ', '')}",
        is_external=True,
    )
