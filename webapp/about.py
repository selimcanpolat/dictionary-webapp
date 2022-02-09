import justpy as jp
from webapp import layout
from webapp import page


class About(page.Page):
    path = "/about"

    def serve(self):
        wp = jp.QuasarPage(tailwind=True)
        lay = layout.DefaultLayout(a=wp)
        container = jp.QPageContainer(a=lay)


        main_div = jp.Div(a=container, classes="bg-gray-800 "  # main div for background (like a canvas)
                                        "h-screen")  # covers the entire screen
        jp.Div(a=main_div,
               text="This is the About page!",
               classes="text-4xl "
                       "m-2")
        jp.Div(a=main_div,text="""
        Sed ut perspiciatis unde omnis iste natus error sit voluptatem 
        accusantium doloremque laudantium, totam rem aperiam, eaque ipsa 
        quae ab illo inventore veritatis et quasi architecto beatae vitae 
        dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit 
        aspernatur aut odit aut fugit, sed quia consequuntur magni dolores 
        eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, qui 
        dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia
        """, classes="text-lg")

        return wp
