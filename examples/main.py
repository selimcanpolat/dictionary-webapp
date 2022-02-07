import justpy as jp


@jp.SetRoute("/home")
def home():
    wp = jp.WebPage()
    main_div = jp.Div(a=wp, classes="bg-gray-800 "  # main div for background (like a canvas)
                               "h-screen")  # covers the entire screen
    top_div = jp.Div(a=main_div, classes="grid grid-cols-3 "
                                         "gap-4 "
                                         "p-4")
    input_1 = jp.Input(a=top_div, placeholder="Enter the first value", classes="form-input")
    input_2 = jp.Input(a=top_div, placeholder="Enter the second value", classes="form-input")

    output = jp.Div(a=top_div, text="The result goes here...", classes="text-gray-600")  # Visit tailwindcss.com for more classes
    jp.Div(a=top_div, text="Another div,", classes="text-gray-600")
    jp.Div(a=top_div, text="Yet another div...", classes="text-gray-600")

    middle_div = jp.Div(a=main_div, classes="grid grid-cols-3 "
                                            "gap-4")

    jp.Button(a=middle_div, text="Calculate",
              click=sum_up,
              in1=input_1,
              in2=input_2,
              d=output,
              classes="border "
                      "border-blue-500 "
                      "m-2 "  # margin
                      "px-4 "  # horizontal padding
                      "py-2 "  # vertical padding
                      "rounded "  # button edges rounded
                      "hover:bg-red-500 "
                      "hover:text-white")
    jp.Div(a=middle_div, text="I am a cool interactive div.")
    return wp


def sum_up(widget, msg):
    sum = float(widget.in1.value) + float(widget.in2.value)
    widget.d.text = sum


# jp.Route("/home", home)


jp.justpy()
