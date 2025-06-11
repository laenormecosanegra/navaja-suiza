import reflex as rx
from navaja_suiza.states.chat_state import ChatState
from navaja_suiza.components.typing_indicator import typing_indicator


def ai_bubble(
    message_text: str, is_last_ai_message: bool
) -> rx.Component:
    return rx.el.div(
        rx.icon(
            tag="bot",
            class_name="h-6 w-6 text-blue-400 mr-3 flex-shrink-0",
        ),
        rx.el.div(
            rx.cond(
                (message_text == "")
                & is_last_ai_message
                & ChatState.typing,
                typing_indicator(),
                rx.el.p(
                    message_text,
                    class_name="text-gray-200 whitespace-pre-wrap",
                ),
            ),
            class_name="bg-gray-700 p-3 rounded-lg rounded-bl-none shadow-sm max-w-xl",
        ),
        class_name="flex items-start mb-4",
    )


def user_bubble(message_text: str) -> rx.Component:
    return rx.el.div(
        rx.el.p(
            message_text,
            class_name="text-white whitespace-pre-wrap",
        ),
        class_name="bg-blue-600 p-3 rounded-lg rounded-br-none shadow-sm self-end max-w-xl",
    )


def message_bubble(
    message: dict, index: int
) -> rx.Component:
    is_last_ai_message = message["is_ai"] & (
        index == ChatState.messages.length() - 1
    )
    return rx.cond(
        message["is_ai"],
        ai_bubble(message["text"], is_last_ai_message),
        user_bubble(message["text"]),
    )