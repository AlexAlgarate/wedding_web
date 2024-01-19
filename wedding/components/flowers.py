import reflex as rx


def flowers() -> rx.Component:
    return rx.image(
        src="/images/lavanda_abajo.png",
        width="100%",
        height="100%",
        flex_shrink="10",
        alt="Imagen de flores al pie de página",
    )
