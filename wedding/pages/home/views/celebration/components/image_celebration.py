import reflex as rx

from wedding.styles import Size


def image_celebration(image: str, alt: str) -> rx.Component:
    return rx.hstack(
        rx.center(
            rx.image(
                src=image,
                border_radius="12px 50px",
                box_shadow="""
                    inset 0 -3em 3em rgba(0, 0, 0, 0.1),
                    0.3em 0.3em 1em rgba(0, 0, 0, 0.3)
                """,
                alt=alt,
                width="70%",
                margin=Size.DEFAULT.value,
            ),
            align_items="center",
        )
    )
