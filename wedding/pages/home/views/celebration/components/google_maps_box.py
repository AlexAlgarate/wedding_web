import reflex as rx

from wedding import urls as url


def google_maps_box() -> rx.Component:
    return rx.hstack(
        rx.center(
            rx.html(
                url.maps,
                width="100%",
            ),
        ),
        align_items="center",
    )
