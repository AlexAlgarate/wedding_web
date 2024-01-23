import reflex as rx

from wedding.routes import IconRoutes
from wedding.styles import Color, Size


def send_email_icon(email: str) -> rx.Component:
    """
    Create an email icon link component.

    Parameters:
    - email (str): The email address to which the email should be sent.

    Returns:
    - rx.Component: A Reflex component representing the email icon link.
    """

    return rx.link(
        rx.button(
            rx.image(src=IconRoutes.ICON_EMAIL.value, alt="Icono de Whatsapp"),
            background=Color.BACKGROUND.value,
            _hover={"background": Color.BACKGROUND.value},
            margin=Size.ZERO.value,
            padding=Size.ZERO.value,
        ),
        href=f"mailto:{email}",
        is_external=True,
    )
