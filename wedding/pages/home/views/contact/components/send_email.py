import reflex as rx

from wedding import utils
from wedding.styles import Color, style


def send_email() -> rx.Component:
    return rx.box(
        rx.popover(
            rx.popover_trigger(
                rx.button(utils.contact_button, style=style.contact_button_style)
            ),
            rx.popover_content(
                rx.popover_body(
                    rx.link(
                        rx.text(utils.contact_popover_bride),
                        href=f"mailto:{utils.contact_bride.get('email')}",
                        is_external=True,
                    ),
                ),
                rx.popover_body(
                    rx.link(
                        rx.text(utils.contact_popover_groom),
                        href=f"mailto:{utils.contact_groom.get('email')}",
                        is_external=True,
                    ),
                ),
                rx.popover_body(
                    rx.link(
                        rx.text(utils.contact_popover_both),
                        href=f"mailto:{utils.contact_bride.get('email')},{utils.contact_groom.get('email')}?Subject=Asistencia boda Vicky-Álex",
                        is_external=True,
                    )
                ),
                rx.popover_close_button(),
                background=Color.BACKGROUND.value,
            ),
        ),
        is_lazy=True,
    )
