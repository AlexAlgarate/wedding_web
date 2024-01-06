import reflex as rx

from wedding.styles import style
from wedding.styles.style import Size


def contact_box(
    text: str,
    email: str,
    phone_number: str,
) -> rx.Component:
    return rx.box(
        rx.text(text, text_align="center"),
        contact_email(email=email),
        contact_phone(phone_number=phone_number),
        # border=".5px solid",
        style=style.shadow_style,
        width="auto",
        margin_bottom="30px",
    )


def contact_email(email: str):
    return rx.hstack(
        rx.link(
            rx.span(
                rx.icon(tag="email", margin=Size.DEFAULT.value),
                rx.span(email),
            ),
            href=f"mailto:{email}",
        ),
        width="100%",
    )


def contact_phone(phone_number: str):
    return rx.hstack(
        rx.span(
            rx.icon(tag="phone", margin=Size.DEFAULT.value),
            rx.span(phone_number),
        ),
    )


def contact_box_(text: str, email: str, phone_number: str) -> rx.Component:
    return rx.box(
        rx.text(text, text_align="center"),
        contact_info(icon="email", info=email),
        contact_info(icon="phone", info=phone_number),
        style=style.shadow_style,
        width="auto",
        margin_bottom="30px",
    )


def contact_info(icon: str, info: str) -> rx.Component:
    href_contact = f"mailto:{info}" if icon == "email" else ""
    return rx.hstack(
        rx.link(
            rx.span(
                rx.icon(tag=icon, margin=Size.DEFAULT.value),
                rx.span(info),
            ),
            href=href_contact,
        ),
        width="100%",
    )
