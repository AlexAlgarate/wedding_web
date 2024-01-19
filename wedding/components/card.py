import reflex as rx

from wedding.styles import Size


def card(*components: rx.Component) -> rx.Component:
    return rx.flex(
        *components,
        direction="column",
        align="center",
        gap="8px",
        padding="16px 12px",
        margin_x=Size.MEDIUM.value,
        justify_content="center",
        border_radius="12px",
        box_shadow="0px 2px 4px 0px rgba(0, 0, 0, 0.25)",
    )
