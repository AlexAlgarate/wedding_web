import reflex as rx

from wedding.routes import IconRoutes
from wedding.styles import Color, Size


def send_whastapp_icon(number: str) -> rx.Component:
    """
    Create a WhatsApp icon link component.

    Parameters:
    - number (str): The phone number to which the WhatsApp message should be sent.

    Returns:
    - rx.Component: A Reflex component representing the WhatsApp icon link.
    """

    return rx.link(
        rx.button(
            rx.image(src=IconRoutes.ICON_WHATSAPP.value, alt="Icono de Whatsapp"),
            background=Color.BACKGROUND.value,
            _hover={"background": Color.BACKGROUND.value},
            margin=Size.ZERO.value,
            padding=Size.ZERO.value,
        ),
        href=f"https://wa.me/34{number}",
        is_external=True,
    )
