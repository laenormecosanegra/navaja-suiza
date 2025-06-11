import reflex as rx


def typing_indicator() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            class_name="h-2 w-2 bg-gray-500 rounded-full animate-bounce delay-75"
        ),
        rx.el.div(
            class_name="h-2 w-2 bg-gray-500 rounded-full animate-bounce delay-150"
        ),
        rx.el.div(
            class_name="h-2 w-2 bg-gray-500 rounded-full animate-bounce delay-225"
        ),
        class_name="flex space-x-1 p-2 items-center",
    )