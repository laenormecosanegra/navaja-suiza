import reflex as rx
from navaja_suiza.states.chat_state import ChatState
from navaja_suiza.components.message_bubble import message_bubble
from navaja_suiza.components.input_area import input_area


def chat_page() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.h1(
                "Chat IA",
                class_name="text-3xl font-bold text-gray-100",
            ),
            rx.el.button(
                rx.icon(
                    tag="trash-2", class_name="mr-2 h-4 w-4"
                ),
                "Limpiar Chat",
                on_click=ChatState.clear_messages,
                class_name="px-3 py-1.5 text-sm bg-red-500 text-white rounded-md hover:bg-red-600 font-medium",
                disabled=ChatState.messages.length() == 0,
            ),
            class_name="flex justify-between items-center p-4 border-b border-gray-700 bg-gray-800",
        ),
        rx.el.div(
            rx.cond(
                ChatState.messages.length() == 0,
                rx.el.div(
                    rx.icon(
                        tag="message-circle",
                        class_name="h-16 w-16 text-gray-500 mb-4",
                    ),
                    rx.el.p(
                        "Aún no hay mensajes. ¡Comienza una conversación!",
                        class_name="text-gray-400 text-lg",
                    ),
                    class_name="flex flex-col items-center justify-center h-full text-center p-8",
                ),
                rx.el.div(
                    rx.foreach(
                        ChatState.messages,
                        lambda msg, idx: message_bubble(
                            msg, idx
                        ),
                    ),
                    class_name="flex-grow p-4 space-y-4 overflow-y-auto",
                ),
            ),
            class_name="flex-grow overflow-y-auto",
        ),
        input_area(),
        class_name="h-full flex flex-col bg-gray-900",
    )