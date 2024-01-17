import reflex as rx

from wedding import url


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
