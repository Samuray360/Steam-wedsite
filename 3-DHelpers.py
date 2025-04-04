import flet as ft
import re
import json
import os
import datetime

    # explicacion del algoritmo de lunh
    
# Desde la derecha, toma todos los dígitos en posiciones pares (0-index, desde la derecha) y dóblalos (multiplícalos por 2).

# Si al doblar un número obtienes algo mayor a 9 (por ejemplo, 2 × 7 = 14), súmale sus dígitos (14 → 1 + 4 = 5).

# Suma todos los dígitos transformados (los doblados con ajustes) y los que no se doblaron.

# Si el total es múltiplo de 10, entonces el número es válido según Luhn.
#https://www.youtube.com/watch?v=qjHgRwQHD3s
def main(page: ft.Page):
    page.title = "3D-Helpers"
    page.bgcolor = "#FFFFFF"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.padding = 0

    # Responsive resize handler
    def on_resize(e):
        home_bg.width = page.width
        home_bg.height = page.height
        donation_img.width = page.width
        donation_img.height = page.height
        gallery_img.width = min(350, page.width * 0.9 if page.width < 600 else page.width * 0.4)
        gallery_img.height = min(450, page.height * 0.6)
        our_work_img.width = min(200, page.width * 0.9 if page.width < 600 else page.width * 0.25)
        our_work_img.height = min(300, page.height * 0.4)

        
        # Containers and forms
        nav_bar.width = page.width
        donation_form.width = min(300, page.width * 0.3)
        donation_form.height=min(600,page.width*0.4)
        join_section.width = page.width
        
        # Views
        home_view.width = page.width
        home_view.height = page.height
        about_view.width = page.width
        about_view.height = page.height
        donate_view.width = page.width
        donate_view.height = page.height
        
        title_section.size = 24 if page.width > 600 else 18
        description_text.size = 16 if page.width > 600 else 12
        for text in key_areas.controls: text.size = 16 if page.width > 600 else 12
        donate_text.size = 48 if page.width > 600 else 24
        logo_text.size = 40 if page.width > 600 else 18
        page.update()

    # page.on_resize = on_resize  # Changed from on_event to on_resize

    page.on_event= lambda _: on_resize()

    # Variables
    logo = ft.Image(src="logo(home).png",width=120,height=80)

    name_field = ft.TextField(label="Name", width=250,height=40, color="black")
    last_name_field = ft.TextField(label="Last Name", width=250,height=40, color="black")
    credit_card_field = ft.TextField(label="Credit Card Number", width=250,height=40, color="black")
    cvv_field = ft.TextField(label="CVV", width=250,height=40,color="black")
    amount_field = ft.TextField(label="Donation Amount ($)", width=250,height=40,color="black")
    feedback_text = ft.Text("", color="green", visible=False)
    donation_img = ft.Image(src="Donation_img.png", fit=ft.ImageFit.COVER,)
    bg_image = ft.Image(src="Join_bg.png", fit=ft.ImageFit.COVER,width=page.width)
    logo_text = ft.Text("3D Helpers", size=24, color="white", weight=ft.FontWeight.BOLD)
    donate_text = ft.Text("Donate now!", size=120, color="white", weight=ft.FontWeight.BOLD)
    home_bg = ft.Image(src="Home.png",fit=ft.ImageFit.COVER, width=page.width, height=page.height)
    insta_img = ft.Image(src="insta.png", width=80, height=40)
    face_img = ft.Image(src="Facebook.png", width=80, height=40)
    img_index = 1  # Simple integer for gallery
    gallery_img = ft.Image(src="diseño1.png",width=350,height=450)
    our_work_img=ft.Image(src="diseño1.png",width=200,height=300)

    # Home View Components
    title_section = ft.Text(" Our Work", size=24, weight=ft.FontWeight.BOLD, color="black")
    description_text = ft.Text(
        "  At 3D Helpers, we use technology and design to transform generosity into action.\n Our project is built on three key areas: graphic design, robotics, and software development.\n\n",
        size=16, color="black"
    )
    key_areas = ft.ResponsiveRow([
        ft.Text(" 🔹 Graphic Design -  We create visually engaging designs\n for our website and promotional materials, ensuring \n our message reaches a wider audience.",size=16,color="black"),
        ft.Text(" 🔹 Robotics & 3D Printing - Using 3D printing technology, \n we produce small car models as a token of appreciation for our donors, \n symbolizing the movement toward change.",size=16,color="black"),
        ft.Text(" 🔹 Software Development - We have built an intuitive online platform \n where people can learn about our mission, contribute to the cause, \n and track our impact.",size=16,color="black")
        ,ft.Text("\n")
    ])
    
    Our_work_section=ft.ResponsiveRow([ft.Row(controls=[ft.Column(controls=[title_section,description_text]),ft.Image(src="carronegro.png",width=350,height=350)],spacing=300)],col=6,)
    
    top_section = ft.ResponsiveRow(
        [ft.Row(controls=[
            ft.Text("\n\n"),
            ft.Image(src="kid.png", width=400, height=400),
            ft.Text(" At 3D Helpers, we believe in the power of technology to drive meaningful change. \n Our mission is to raise awareness and combat child poverty\n in the Dominican Republic\n by merging innovation and compassio. Through graphic design, robotics,\n and software development we create a unique experience for donors—each\n contribution is met with a 3D-printed car, a symbol of the movement toward a better future.\n By supporting our cause, you’re not just making a donation;\n you’re joining a community dedicated to transforming lives and inspiring hope.", size=16,color="black")
            
        ],
        alignment=ft.alignment.center,
        spacing=20,
    )],col=6)
    middle_section = ft.ResponsiveRow([
        ft.Row(controls=[
            ft.Text("\n\n"),
            ft.Text(" Get involved today and help us make a difference! Whether you choose to donate, spread the word, or volunteer your skills,\n every action helps us reach our goal of RD$6,500 to support vulnerable children. \n Explore our website to learn more about our work, meet the team, and see the impact your generosity makes.\n Together, we can drive change—one layer at a time.", size=16,color="black",col=6),
            ft.Image(src="tierra.png", width=300, height=400,col=6)
        ],
        alignment=ft.alignment.center,
        spacing=20
    )])
    
    footer_section = ft.Container(
    content=ft.ResponsiveRow([ft.Row(
        controls=[

            ft.Column([
                ft.Text("TALK TO US", size=16, weight=ft.FontWeight.BOLD,col=6),
                ft.Text("(04) 298 3985 2092 \n +1 209 1092 4095 \n info@3dhelpers.com",weight=ft.FontWeight.BOLD,col=6),ft.Text("\n\n")
            ]),
            ft.Column(
                controls=[
                    ft.Row(controls=[insta_img, ft.Text("@3dHelpersRD",size=16,weight=ft.FontWeight.BOLD,col=6)]),
                    ft.Row(controls=[face_img, ft.Text("@3dHelpersRD",size=16,weight=ft.FontWeight.BOLD,col=6)]),
                    ft.Row(controls=[logo]),ft.Text("\n\n")
                ],
                alignment=ft.alignment.center
            )],alignment=ft.MainAxisAlignment.SPACE_BETWEEN)
        ],
        
    ),
    bgcolor="#175ABF",
    padding=20
)
    
    about_title = ft.Row(
        controls=[
            ft.Text(""),
            ft.Text(" We are 3D Helpers, an initiative that combines technology and solidarity to create a meaningful impact.\n Our project integrates graphic design, robotics, and software development\n to raise awareness about child poverty in the Dominican Republic. \n Through our platform, anyone can contribute by making donations, \n which are directed to aid institutions and the production of 3D-printed models.\n\n As a token of appreciation, each donor receives a 3D-printed car, \n symbolizing the drive toward a better future. With this effort, \n we aim not only to alleviate poverty but also to inspire more people to be part of the change.", size=16,color="black")
            ,ft.Image(src="about_us.png",width=300,height=430)
        ],
        spacing=100
    )
    
    about_content = ft.ResponsiveRow(
        controls=[
            ft.Column(
                controls=[
                    ft.Row(
                        controls=[
                            ft.Text(""),
                            ft.Text(""),
                            ft.Text(
                            " At 3D Helpers, our mission is to make a real difference\n in the fight against child poverty in the Dominican Republic. \n Through technology and creativity, we strive not only to raise funds\n but also to increase public awareness of this pressing issue.",
                            size=16,
                            color="black",
                                ),
                            ft.Image(src="gente.webp", width=300, height=430),
                        ],
                        spacing=100,
                        alignment=ft.alignment.center,
                    ),
                    ft.Row(
                        controls=[
                            ft.Text(""),
                            ft.Text(""),
                            ft.Text(
                            " Our goal is to make a real difference\n in the fight against child poverty in the Dominican Republic.\n\n Through technology and creativity, we strive not only to raise funds\n but also to increase public awareness of this pressing issue.",
                            size=16,
                            color="blue",
                            ),
                            ft.Image(src="engranaje.png", width=300, height=430),
                        ],
                        spacing=100,
                        alignment=ft.alignment.center,
                    ),
                    ft.Row(
                        controls=[
                            ft.Text(""),
                            ft.Text(""),
                            ft.Text(
                            " Our primary goal is to reach at least RD$6,500 in donations, with 70% \n going directly to charitable organizations that support children in\n vulnerable situations and 30% used for the production of 3D-printed models\n that symbolize our commitment to the cause. With every donation,\n we not only provide aid but also promote innovation and design as powerful \ntools for social change.",
                            size=16,
                            color="black",
                            ),
                            ft.Image(src="impresora.png", width=300, height=430),
                        ],
                        spacing=100,
                        alignment=ft.alignment.center,
                    ),
                ],
                alignment=ft.alignment.center,
            )
        ],
        alignment=ft.alignment.center,
        expand=True,

    )
    # Gallery
    def gallery_images(change):
        nonlocal img_index
        img_index += change
        if img_index < 1:
            img_index = 8
        elif img_index > 8:
            img_index = 1
        match img_index :
            case 1: gallery_img.src = "Diseño1.png"
            case 2: gallery_img.src = "Diseño2.png"
            case 3: gallery_img.src = "Diseño3.png"
            case 4: gallery_img.src = "Diseño4.png"
            case 5: gallery_img.src = "Diseño5.png"
            case 6: gallery_img.src = "carroblanco.png"
            case 7: gallery_img.src = "carrorojo.png"
            case 8: gallery_img.src = "ferrari.png"
        page.update()

    gallery_section = ft.Row(
        controls=[
            ft.ElevatedButton("←", on_click=lambda e: gallery_images(-1),style=ft.ButtonStyle(bgcolor="#175ABF", color="white")),
            gallery_img,
            ft.ElevatedButton("→", on_click=lambda e: gallery_images(1),style=ft.ButtonStyle(bgcolor="#175ABF", color="white"))
        ],
        alignment=ft.MainAxisAlignment.CENTER, spacing=10
    )

    # Navigation
    def show_home(e): home_view.visible, about_view.visible, donate_view.visible = True, False, False; page.update()
    def show_about(e): home_view.visible, about_view.visible, donate_view.visible = False, True, False; page.update()
    def show_donate(e): home_view.visible, about_view.visible, donate_view.visible = False, False, True; page.update()
    
    def to_about_button_style(e:ft.ControlEvent):
        if e.data == "true":  # Mouse enters the button (hover starts)
                to_about_button.style = ft.ButtonStyle(
                bgcolor="white",
                color="#175ABF",    
                shape=ft.RoundedRectangleBorder(radius=20),
                padding=10
                    )
        elif e.data == "false":  # Mouse leaves the button (hover ends)
                to_about_button.style = ft.ButtonStyle(
                bgcolor="#175ABF",
                color="white",
                shape=ft.RoundedRectangleBorder(radius=20),
                padding=10
            )
        to_about_button.update()           

    to_about_button=ft.Row([ft.ElevatedButton("About us",on_click=show_about,on_hover=to_about_button_style,width=200,height=50,style=ft.ButtonStyle(bgcolor="#175ABF",color="white",shape=ft.RoundedRectangleBorder(radius=20),padding=10))])
   
    # Join Section
    join_button = ft.ElevatedButton("Join us",on_click=show_donate, width=200, height=60, style=ft.ButtonStyle(bgcolor="#175ABF", color="white",shape=ft.RoundedRectangleBorder(radius=20)))
    join_section = ft.Stack(controls=[bg_image, ft.Column([logo_text, donate_text, join_button],)],expand=True,alignment=ft.alignment.center)

    # Quote Section
    quote_section = ft.Container(
        content=ft.Column([
            ft.Text(
                "\"The purpose of ideals, are to be able to shape them to make a change\"",
                size=20,
                italic=True,
                color="white"
            ),
            ft.Text("- Ethan Tamarez", size=16, color="white")
        ], alignment=ft.alignment.center),
        bgcolor="#6495ED",
        padding=20,
        alignment=ft.alignment.center
    )
    # Donation Form
    def validate_credit_card(card_number: str) -> bool:
        card_number = re.sub(r'\D', '', card_number)
        if not card_number or len(card_number) < 13 or len(card_number) > 19:
            return False
        digits = [int(x) for x in card_number]
        checksum = 0
        is_even = False
        for i in range(len(digits) - 1, -1, -1):
            if is_even:
                digits[i] *= 2
                if digits[i] > 9:
                    digits[i] -= 9
            checksum += digits[i]
            is_even = not is_even
        return checksum % 10 == 0

    def process_donation(e):
        name, last_name, credit_card, cvv, amount = (
            name_field.value.strip(),
            last_name_field.value.strip(),
            credit_card_field.value,
            cvv_field.value,
            amount_field.value
        )
        if not all([name, last_name, credit_card, cvv, amount]):
            feedback_text.value, feedback_text.color = "Please fill in all fields.", "red"
            feedback_text.visible = True
            page.update()
            return
        if not validate_credit_card(credit_card):
            feedback_text.value, feedback_text.color = "Invalid credit card number.", "red"
            feedback_text.visible = True
            page.update()
            return
        if not (len(cvv) in [3, 4] and cvv.isdigit()):
            feedback_text.value, feedback_text.color = "Invalid CVV.", "red"
            feedback_text.visible = True
            page.update()
            return
        try:
            amount_float = float(amount)
            if amount_float <= 0:
                raise ValueError
        except ValueError:
            feedback_text.value, feedback_text.color = "Please enter a valid donation amount.", "red"
            feedback_text.visible = True
            page.update()
            return

        donation_data = {
            "name": name,
            "last_name": last_name,
            "credit_card": credit_card[-4:],
            "amount": round(amount_float, 2),
            "timestamp": str(datetime.datetime.now())
        }
        file_path = "donations.json"
        try:
            if os.path.exists(file_path):
                with open(file_path, "r") as f:
                    data = json.load(f)
            else:
                data = []
            data.append(donation_data)
            with open(file_path, "w") as f:
                json.dump(data, f, indent=4)
            feedback_text.value, feedback_text.color = "Thank you for your donation!", "green"
            feedback_text.visible = True
            for field in [name_field, last_name_field, credit_card_field, cvv_field, amount_field]:
                field.value = ""
        except (json.JSONDecodeError, IOError) as ex:
            feedback_text.value, feedback_text.color = f"Error saving donation: {str(ex)}", "red"
            feedback_text.visible = True
        page.update()

    donation_form = ft.Container(
        content=ft.Column(
            controls=[
                ft.Text("Help our Cause by Donating!", size=16, weight=ft.FontWeight.BOLD, color="black"),
                name_field,
                last_name_field,
                credit_card_field,
                cvv_field,
                amount_field,
                ft.ElevatedButton("Donate", bgcolor="#1E90FF", width=250, height=50, style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10), color="white"), on_click=process_donation),
                ft.Row([ft.Image(src="mastercard_logo.png", width=100, height=80), ft.Image(src="paypal_logo.png", width=100, height=80)]),
                feedback_text
            ],
            spacing=5,
            auto_scroll=False
        ),
        bgcolor="white",
        padding=20,
        border=ft.border.all(1, "#D3D3D3"),
        border_radius=10,
        alignment=ft.alignment.center,
            )
    
    about_us_section=ft.Container(content=ft.Row(controls=[ft.Column(controls=[about_title,about_content,join_section])],alignment=ft.alignment.center))
    
    # Views with Scroll
    home_view = ft.Container(
        content=ft.ListView(
            controls=[home_bg, top_section, middle_section, quote_section,Our_work_section,key_areas,to_about_button,gallery_section,footer_section],
            visible=True,
            
        ),
        expand=True,
        
    )
    about_view = ft.Container(
        content=ft.ListView(
            controls=[about_us_section],
            expand=True,
            spacing=10,
            
            
        ),
        expand=True,
        visible=False
    )
    donate_view =ft.Stack(
        controls=[donation_img, donation_form],
        
        expand=True,alignment=ft.alignment.center,
        visible=False
    )

    nav_buttons = ft.Row([
        ft.ElevatedButton("Home", on_click=show_home, style=ft.ButtonStyle(bgcolor="#175ABF", color="white")),
        ft.ElevatedButton("About", on_click=show_about, style=ft.ButtonStyle(bgcolor="#175ABF", color="white")),
        ft.ElevatedButton("Donate", on_click=show_donate, style=ft.ButtonStyle(bgcolor="#175ABF", color="white")),
    
    ], spacing=15, wrap=True,alignment=ft.MainAxisAlignment.END, 
        vertical_alignment=ft.CrossAxisAlignment.CENTER,    )
    
    nav_controls=ft.Row(controls=[logo, nav_buttons],alignment=ft.MainAxisAlignment.SPACE_BETWEEN,expand=True,height=80)

    nav_bar = ft.Container(content=ft.ResponsiveRow(controls=[nav_controls],col=6),bgcolor="#175ABF",padding=ft.padding.symmetric(vertical=0,horizontal=20),height=80,margin=0)

    
    # Assemble Page
    page.add(ft.Column([  # Wrap in Column to ensure tight stacking
            nav_bar,
            ft.Stack([home_view, about_view, donate_view])
        ], spacing=0)
    )
    on_resize(None)  # Initial resize
    page.update()

ft.app(target=main, view=ft.WEB_BROWSER, assets_dir="assets", port=3000)