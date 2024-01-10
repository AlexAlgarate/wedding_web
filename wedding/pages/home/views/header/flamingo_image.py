import reflex as rx

from wedding.routes import FileRoutes as file


def flamingo_header() -> rx.Component:
    return rx.box(
        rx.hstack(
            rx.image(src=file.FLAMINGO_RIGHT.value, opacity="0.5", height="50%", width="50%"),
            rx.image(
                src=file.FLAMINGO_LEFT.value,
                opacity="0.5",
                height="50%",
                width="50%",
            ),
            margin_inline_start="-5.5em",
            display="flex",
            align_items="center",
            flex_direction="row",
        )
    )


# def flamingo_header() -> rx.Component:
#     return rx.image(src=file.FLAMINGO.value, opacity="0.5", height="50%", width="50%")
