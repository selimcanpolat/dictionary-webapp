import justpy as jp
import definition
from webapp import layout
from webapp import page
import requests


class Dictionary(page.Page):
    path = "/dictionary"

    @classmethod
    def serve(cls, req):
        wp = jp.QuasarPage(tailwind=True)
        lay = layout.DefaultLayout(a=wp)
        container = jp.QPageContainer(a=lay)


        main_div = jp.Div(a=container, classes="bg-gray-800 "  # main div for background (like a canvas)
                                        "h-screen")  # covers the entire screen
        jp.Div(a=main_div,
               text="Instant English dictionary",
               classes="text-4xl "
                       "m-2")
        jp.Div(a=main_div,
               text="Get the definition of an English word instantly as you type.",
               classes="text-lg")

        input_div = jp.Div(a=main_div, classes="grid grid-cols-2")
        output_div = jp.Div(a=main_div, classes="grid grid-cols-2")
        input_box = jp.Input(a=input_div,
                 placeholder="Type in a word here...", outputdiv=output_div,
                 classes="m-2 "
                         "bg-gray-200 "
                         "border-2 "
                         "border-gray-200 "
                         "rounded "
                         "w-64 "
                         "focus:bg-white"
                         "focus:outline-none "
                         "focus:border-purple-500 "
                         "py-2 "
                         "px-4")
        input_box.on("input", cls.get_definition)

        return wp

    @staticmethod
    def get_definition(widget, msg):
        req = requests.get(f"http://127.0.0.1:8000/api?w={widget.value}")
        data = req.json()
        definition_of_the_word = data["definition"]
        widget.outputdiv.text = definition_of_the_word

