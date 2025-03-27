import flet as ft

def main(page: ft.Page):
    page.title = "3D-Helpers"
    page.bgcolor = "#FFFFFF"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.spacing = 0
    page.padding = 0

    # Input Fields
    card_number = ft.TextField(label="Card Number")
    owner_name = ft.TextField(label="Owner Name")
    due_date = ft.TextField(label="Due Date")

    
    logo = ft.Image(
    src="C:/Users/ethan/OneDrive/Desktop/Java/Steam-wedsite/logo(home).png",
    width=120,
    height=80,
)

   
    bg_image = ft.Image(
        src="C:/Users/ethan/OneDrive/Desktop/Java/Steam-wedsite/Join_bg.png",
        fit=ft.ImageFit.COVER,
        width=page.width,
        height=600
    )

    logo_text = ft.Text(
        "3D Helpers",
        size=24,
        color="white",
        weight=ft.FontWeight.BOLD
    )

    # Donate Now Text
    donate_text = ft.Text(
        "Donate now!",
        size=48,
        color="white",
        weight=ft.FontWeight.BOLD
    )
   
    # Donate Function
    def donate_function(e):
        pay_way.visible = True
        home_view.visible = False
        about_view.visible = False
        page.update()

    # Join Us Button
    join_button = ft.ElevatedButton(
        "Join us",
        bgcolor="#6495ED",
        color="white",
        width=120,
        height=40,
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=20)
        ),
        on_click=donate_function
    )

    # Join Section
    join_section = ft.Container(
        content=ft.Stack(
            [
                bg_image,
                ft.Column(
                    [
                        logo_text,
                        donate_text,
                        join_button,
                    ],
                    
                )
            ]
        )
    )

    # About Us Image
    about_us_img = ft.Image(src="C:/Users/ethan/OneDrive/Desktop/Java/Steam-wedsite/about_us.png")
    about_view = ft.Container(visible=False)

   
    home_view = ft.Container(
        content=ft.Column(
            controls=[ft.Image(src="C:/Users/ethan/OneDrive/Desktop/Java/Steam-wedsite/Home.png", width=1900, height=950), join_section]
        ),
        alignment=ft.alignment.center
    )

    # Donation Form
    Donation_img = ft.Image(src="C:/Users/ethan/OneDrive/Desktop/Java/Steam-wedsite/Donation_img.png")

    Donation = ft.Container(
        content=ft.Column(controls=[card_number, owner_name, due_date]),
        bgcolor="#FFFFFF"
    )
    pay_way = ft.Stack(controls=[Donation, Donation_img], visible=False)
    # Page Navigation Functions
    def home_function(e):
        about_view.visible = False
        Donation.visible = False
        home_view.visible = True
        page.update()

    def about_us_function(e):
        home_view.visible = False
        pay_way.visible = False
        about_view.visible = True
        page.update()

    # Navigation Buttons
    home_button = ft.ElevatedButton(
        text="Home", on_click=home_function,
        style=ft.ButtonStyle(bgcolor="#175ABF", color=ft.Colors.WHITE)
    )

    donate_button = ft.ElevatedButton(
        text="Donate", on_click=donate_function,
        style=ft.ButtonStyle(bgcolor="#175ABF", color=ft.Colors.WHITE)
    )

    about_button = ft.ElevatedButton(
        text="About", on_click=about_us_function,
        style=ft.ButtonStyle(bgcolor="#175ABF", color=ft.Colors.WHITE)
    )

    # Navigation Bar
    button_row = ft.Row(controls=[home_button, about_button, donate_button])
    search_bar = ft.Container(
        content=ft.Row(controls=[logo, button_row], spacing=950),
        bgcolor="#175ABF",
        width=page.width,
        alignment=ft.alignment.top_center
    )

    # Page Content Stack
    stack = ft.Stack(controls=[about_view, pay_way, home_view])
    page.add(search_bar, stack)
    page.update()

ft.app(target=main,view=ft.WEB_BROWSER)
