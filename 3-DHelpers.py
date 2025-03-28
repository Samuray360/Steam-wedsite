import flet as ft

def main(page: ft.Page):
    page.title = "3D-Helpers"
    page.bgcolor = "#FFFFFF"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.padding = 0

    # Variables from Code 1
    logo = ft.Image(src="logo(home).png", width=120, height=80)
    donation_img = ft.Image(src="Donation_img.png", width=1900, height=950)
    card_number = ft.TextField(label="Card Number",color="black")
    owner_name = ft.TextField(label="Owner Name",color="black")
    due_date = ft.TextField(label="Due Date",color="black")
    bg_image = ft.Image(src="Join_bg.png", fit=ft.ImageFit.COVER, expand=True, height=600)
    logo_text = ft.Text("3D Helpers", size=24, color="white", weight=ft.FontWeight.BOLD)
    donate_text = ft.Text("Donate now!", size=48, color="white", weight=ft.FontWeight.BOLD)

    # Home View Components from Code 2
    title_section = ft.Text("Our Work", size=24, weight=ft.FontWeight.BOLD,color="black")
    description_text = ft.Text(
        "At 3D Helpers, we use technology and design to transform generosity into action.\n Our project is built on three key areas: graphic design,robotics, and software development. \nEach of these fields plays a crucial role in our initiative:",
        size=16,color="black"
    )
    key_areas = ft.Column([
        ft.Text("• Graphic Design -  We create visually engaging designs \nfor our website and promotional materials, ensuring \nour message reaches a wider audience.",color="black"),
        ft.Text("• Robotics & 3D Printing - Using 3D printing technology, \nwe produce small car models as a token of appreciation for our donors, \nsymbolizing the movement toward change.",color="black"),
        ft.Text("• Software Development - We have built an intuitive online platform \nwhere people can learn about our mission, contribute to the cause, \nand track our impact.",color="black")
    ])

    # Combined Top and Middle Sections
    top_section = ft.Row(
        controls=[
            ft.Image(src="kid.png", width=200, height=200,),
            ft.Text("Help us make a difference", size=20,color="black")
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=20
    )
    
    middle_section = ft.Row(
        controls=[
            ft.Text("Join our mission to create positive change", size=20,color="black"),
            ft.Image(src="tierra.png", width=200, height=200)
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=20
    )

    # Gallery from Code 2
    def gallery_images():
        gallery= ft.Row([
        ft.Image(src="Diseño1.png", width=150, height=150),
        ft.Image(src="Diseño2.png", width=150, height=150),
        ft.Image(src="Diseño3.png", width=150, height=150),
        ft.Image(src="Diseño4.png", width=150, height=150),
        ], alignment=ft.MainAxisAlignment.CENTER, spacing=10)
        return gallery
    
    # Join Section from Code 1
    join_button = ft.ElevatedButton(
        "Join us",
        bgcolor="#6495ED",
        color="white",
        width=120,
        height=40,
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=20))
    )
    join_section = ft.Container(
        content=ft.Stack([
            bg_image,
            ft.Column([
                logo_text,
                donate_text,
                join_button,
            ], alignment=ft.MainAxisAlignment.CENTER)
        ])
    )

    # Quote Section (shared between both)
    quote_section = ft.Container(
        content=ft.Column([
            ft.Text(
                "\"The purpose of ideals, are to be able to shape them to make a change\"",
                size=20,
                italic=True,
                color="white"
            ),
            ft.Text("- Ethan Tamarez", size=16, color="white")
        ], alignment=ft.MainAxisAlignment.CENTER),
        bgcolor="#6495ED",
        padding=20,
        alignment=ft.alignment.center
    )

    # Footer from Code 2
    footer_section = ft.Container(
        content=ft.Column([
            ft.Text("TALK TO US", size=16, weight=ft.FontWeight.BOLD),
            ft.Text("(04) 2365 9855 | info@3dhelpers.com"),
            ft.Row([
                ft.Text("@3dHelpersRD"),
                ft.Text("3D Helpers")
            ])
        ], alignment=ft.MainAxisAlignment.CENTER),
        bgcolor="#175ABF",
        padding=20
    )

    # Views
    home_view = ft.Container(content=ft.Column([
        title_section,
        description_text,
        key_areas,
        top_section,
        middle_section,
        gallery_images,
        join_section,
        quote_section,
        footer_section
    ]), visible=True)

    about_view = ft.Container(content=ft.Image(src="about_us.png"), visible=False)

    # Donation Form from Code 1
    donation_form = ft.Container(
        content=ft.Column([card_number, owner_name, due_date]),
        bgcolor="#FFFFFF",
        width=600,
        height=800
    )
    donate_view = ft.Stack([donation_form, donation_img], visible=False)

    # Navigation Functions
    def show_home(e):
        home_view.visible = True
        about_view.visible = False
        donate_view.visible = False
        page.update()

    def show_about(e):
        home_view.visible = False
        about_view.visible = True
        donate_view.visible = False
        page.update()

    def show_donate(e):
        home_view.visible = False
        about_view.visible = False
        donate_view.visible = True
        page.update()

    # Navigation Bar with Logo from Code 1
    nav_buttons = ft.Row([
        ft.ElevatedButton("Home", on_click=show_home, style=ft.ButtonStyle(bgcolor="#175ABF", color="white")),
        ft.ElevatedButton("About", on_click=show_about, style=ft.ButtonStyle(bgcolor="#175ABF", color="white")),
        ft.ElevatedButton("Donate", on_click=show_donate, style=ft.ButtonStyle(bgcolor="#175ABF", color="white"))
    ])
    nav_bar = ft.Container(
        content=ft.Row([logo, nav_buttons], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
        bgcolor="#175ABF",
        padding=10
    )

    # Page Assembly
    stack = ft.Stack([home_view, about_view, donate_view])
    page.add(nav_bar, stack)
    page.update()

ft.app(target=main, view=ft.WEB_BROWSER, assets_dir="assets")