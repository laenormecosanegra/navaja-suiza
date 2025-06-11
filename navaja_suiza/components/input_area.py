import reflex as rx
from navaja_suiza.states.chat_state import ChatState


def input_area() -> rx.Component:
    return rx.el.form(
        rx.el.div(
            rx.el.input(
                name="message",
                placeholder="Escribe tu mensaje...",
                default_value=ChatState.current_chat_input,
                class_name="flex-grow p-3 border border-gray-600 rounded-l-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent outline-none resize-none bg-gray-700 text-gray-100 placeholder-gray-400",
            ),
            rx.el.button(
                rx.icon(tag="send", class_name="h-5 w-5"),
                type="submit",
                is_loading=ChatState.typing,
                class_name="px-4 py-3 bg-blue-500 text-white rounded-r-lg hover:bg-blue-600 disabled:opacity-50 font-medium",
            ),
            class_name="flex",
        ),
        on_submit=ChatState.send_message,
        reset_on_submit=True,
        class_name="p-4 bg-gray-800 border-t border-gray-700",
    )