import justpy as jp
from webapp import layout


class Home:

    path = "/"

    @classmethod
    def serve(cls, req):
        wp = jp.QuasarPage(tailwind=True)

        lay = layout.DefaultLayout(a=wp)

        container = jp.QPageContainer(a=lay)

        div = jp.Div(a=container, classes="bg-gray-200 h-screen p-2")
        jp.Div(a=div, text="This is the home page!", classes="text-4xl m-2")
        jp.Div(a=div, text="""
        Contrary to popular belief, Lorem Ipsum is not simply 
        random text. It has roots in a piece of classical 
        Latin literature from 45 BC, making it over 2000 
        years old. Richard McClintock, a Latin professor 
        at Hampden-Sydney College in Virginia, looked up one 
        """)

        return wp

