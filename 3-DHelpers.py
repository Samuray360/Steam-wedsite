import flet as ft
import re
import json
import os
import datetime
#https://flet.dev/docs/controls/responsiverow/#run_spacing
def main(page: ft.Page):
    page.title = "3D-Helpers"
    page.bgcolor = "#FFFFFF"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.padding = 0

    # Responsive resize handler
    def on_resize(e):
        # gallery_img.width = min(120, page.width * 0.4)
        # gallery_img.height = min(80, page.height * 0.6)
        # donation_form.width = min(350, page.width * 0.3)
        # donation_form.height = min(400, page.height * 0.7)
        home_bg.width = page.width
        home_bg.height = page.height
        donation_img.width = page.width
        donation_img.height = page.height
        nav_bar.width = page.width  # Ensure nav bar spans full width
        
        page.update()

    page.on_resize = on_resize

    # Variables
    logo = ft.Image(src="logo(home).png", width=160, height=80)
    name_field = ft.TextField(label="Name", width=300, color="black")
    last_name_field = ft.TextField(label="Last Name", width=300, color="black")
    credit_card_field = ft.TextField(label="Credit Card Number", width=300, color="black")
    cvv_field = ft.TextField(label="CVV", width=300, color="black")
    amount_field = ft.TextField(label="Donation Amount ($)", width=300, color="black")
    feedback_text = ft.Text("", color="green", visible=False)
    donation_img = ft.Image(src="Donation_img.png", fit=ft.ImageFit.COVER,width=page.width, height=page.height)
    bg_image = ft.Image(src="Join_bg.png", fit=ft.ImageFit.COVER, expand=True)
    logo_text = ft.Text("3D Helpers", size=24, color="white", weight=ft.FontWeight.BOLD)
    donate_text = ft.Text("Donate now!", size=48, color="white", weight=ft.FontWeight.BOLD)
    home_bg = ft.Image(src="Home.png",fit=ft.ImageFit.COVER, width=page.width, height=page.height)
    insta_img = ft.Image(src="insta.png", width=80, height=40)
    face_img = ft.Image(src="Facebook.png", width=80, height=40)
    img_index = 1  # Simple integer for gallery
    gallery_img = ft.Image(src="Diseño1.png",width=350,height=450)
    our_work_img=ft.Image(src="diseño1",width=min(400,page.width*0.8),height=min(500,page.height*0.9))
    # Home View Components
    title_section = ft.Text("Our Work", size=24, weight=ft.FontWeight.BOLD, color="black")
    description_text = ft.Text(
        "   At 3D Helpers, we use technology and design to transform generosity into action.\nOur project is built on three key areas: graphic design, robotics, and software development.\n\n",
        size=16, color="black"
    )
    key_areas = ft.Column([
        ft.Text("   • Graphic Design -  We create visually engaging designs\n for our website and promotional materials, ensuring \n our message reaches a wider audience.",size=16,color="black"),
        ft.Text("   • Robotics & 3D Printing - Using 3D printing technology, \n we produce small car models as a token of appreciation for our donors, \n symbolizing the movement toward change.",size=16,color="black"),
        ft.Text("   • Software Development - We have built an intuitive online platform \n where people can learn about our mission, contribute to the cause, \n and track our impact.",size=16,color="black")
    ])
    
    Our_work_section=ft.Container(content=ft.Row(controls=[ft.Column(controls=[title_section,description_text,key_areas]),our_work_img]))
    
    top_section = ft.ResponsiveRow(
        controls=[
            ft.Text("\n",col={6}),
            ft.Image(src="kid.png", width=400, height=400,col={6}),
            ft.Text(" At 3D Helpers, we believe in the power of technology to drive meaningful change. \n Our mission is to raise awareness and combat child poverty in the Dominican Republic\n by merging innovation and compassio. Through graphic design, robotics, and software development\n we create a unique experience for donors—each contribution is met with a 3D-printed car, \n a symbol of the movement toward a better future. By supporting our cause, \n you’re not just making a donation; you’re joining a community dedicated to transforming lives and inspiring hope.", size=16,color="black",col={6})
        ],
        alignment=ft.alignment.center,
        spacing=20,
    )
    middle_section = ft.Row(
        controls=[
            ft.Text("  Get involved today and help us make a difference! Whether you choose to donate, spread the word, or volunteer your skills,\n every action helps us reach our goal of RD$6,500 to support vulnerable children. \n Explore our website to learn more about our work, meet the team, and see the impact your generosity makes.\n Together, we can drive change—one layer at a time.", size=16,color="black"),
            ft.Image(src="tierra.png", width=400, height=500)
        ],
        alignment=ft.alignment.center,
        spacing=20
    )
    footer_section = ft.Container(
    content=ft.Row(
        controls=[
            ft.Column([
                ft.Text("TALK TO US", size=16, weight=ft.FontWeight.BOLD),
                ft.Text("(04) 298 3985 2092 \n +1 209 1092 4095 \n info@3dhelpers.com",weight=ft.FontWeight.BOLD),ft.Text("\n\n")
            ]),
            ft.Column(
                controls=[
                    ft.Row(controls=[insta_img, ft.Text("@3dHelpersRD",size=16,weight=ft.FontWeight.BOLD)]),
                    ft.Row(controls=[face_img, ft.Text("@3dHelpersRD",size=16,weight=ft.FontWeight.BOLD)]),
                    ft.Row(controls=[logo]),ft.Text("\n\n")
                ],
                alignment=ft.alignment.center
            ),
        ],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN
    ),
    bgcolor="#175ABF",
    padding=20
)
    
    about_title = ft.Row(
        controls=[
            
            ft.Text(" We are 3D Helpers, an initiative that combines technology and solidarity to create a meaningful impact.\n Our project integrates graphic design, robotics, and software development\n to raise awareness about child poverty in the Dominican Republic. \n Through our platform, anyone can contribute by making donations, \n which are directed to aid institutions and the production of 3D-printed models.\n\n As a token of appreciation, each donor receives a 3D-printed car, \n symbolizing the drive toward a better future. With this effort, \n we aim not only to alleviate poverty but also to inspire more people to be part of the change.", size=16,color="black")
            ,ft.Image(src="about_us.png",width=200,height=250)
        ],
        spacing=20
    )
    about_content = ft.Column([ft.Row(
        controls=[
            ft.Text(" At 3D Helpers, our mission is to make a real difference in the fight against child poverty in the Dominican Republic. \n Through technology and creativity, we strive not only to raise funds but also to increase public awareness of this pressing issue. ", size=16,color="black"),
            ft.Image(src="ladtop.png", width=200, height=250,)
             ],  
        
        spacing=20
    ), 
            ft.Row(controls=[
                
            ft.Text(" Our goal is to make a real difference in the fight against child poverty in the Dominican Republic.\n\n Through technology and creativity, we strive not only to raise funds but also to increase public awareness of this pressing issue.", 
                    size=16,color="blue"),ft.Image(src="engranaje.png", width=200, height=250,)],spacing=15),
            
            
            ft.Row(controls=[
            ft.Text(" Our primary goal is to reach at least RD$6,500 in donations, with 70% \ngoing directly to charitable organizations that support children in vulnerable situations and 30%\n used for the production of 3D-printed models that symbolize our commitment to the cause. With every donation,\n we not only provide aid but also promote innovation and design as powerful tools for social change. ", 
                    size=16,color="black"),
             ft.Image(src="impresora.png", width=200 ,height=250,),
        ],spacing=40) 
    ],alignment=ft.MainAxisAlignment.SPACE_BETWEEN)

    # Gallery
    def gallery_images(change):
        nonlocal img_index
        img_index += change
        if img_index < 1:
            img_index = 5
        elif img_index > 5:
            img_index = 1
        match img_index:
            case 1: gallery_img.src = "Diseño1.png"
            case 2: gallery_img.src = "Diseño2.png"
            case 3: gallery_img.src = "Diseño3.png"
            case 4: gallery_img.src = "Diseño4.png"
            case 5: gallery_img.src = "Diseño5.png"
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
        # if e.data == "true":  # Mouse entered (hover starts)
        #     to_about_button.style = ft.ButtonStyle(
        #         bgcolor="white",
        #         color="#175ABF",
        #         border=ft.border.all(2, ft.colors.BLUE),
        #         shape=ft.RoundedRectangleBorder(radius=20)
        #     )
        # else:  # Mouse exited (hover ends)
        #     to_about_button.style = ft.ButtonStyle(
        #         bgcolor="#175ABF",
        #         color="white",
        #         shape=ft.RoundedRectangleBorder(radius=20)
        #     )
        to_about_button.style=ft.ButtonStyle(bgcolor="white",color="#175ABF",border=ft.border.all(2, ft.colors.BLUE),shape=ft.RoundedRectangleBorder(radius=20))
        to_about_button.update()


    to_about_button=ft.ElevatedButton("About us",on_click=show_about,on_hover=to_about_button_style,width=300,style=ft.ButtonStyle(bgcolor="#175ABF",color="white",shape=ft.RoundedRectangleBorder(radius=20),padding=10))


    # Join Section
    join_button = ft.ElevatedButton("Join us",on_click=show_donate ,bgcolor="#175ABF", color="white", width=120, height=40, style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=20)))
    join_section = ft.Container(content=ft.Stack([bg_image, ft.Column([logo_text, donate_text, join_button],)]))

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
        name, last_name, credit_card, cvv, amount = name_field.value, last_name_field.value, credit_card_field.value, cvv_field.value, amount_field.value
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

        donation_data = {"name": name, "last_name": last_name, "credit_card": credit_card[-4:], "amount": amount_float, "timestamp": str(datetime.datetime.now())}
        file_path = "donations.json"
        try:
            data = json.load(open(file_path, "r")) if os.path.exists(file_path) else []
            data.append(donation_data)
            with open(file_path, "w") as f:
                json.dump(data, f, indent=4)
            feedback_text.value, feedback_text.color = "Thank you for your donation!", "green"
            feedback_text.visible = True
            for field in [name_field, last_name_field, credit_card_field, cvv_field, amount_field]:
                field.value = ""
        except Exception as ex:
            feedback_text.value, feedback_text.color = f"Error saving donation: {str(ex)}", "red"
            feedback_text.visible = True
        page.update()

    donation_form = ft.Container(
        content=ft.Column([
            ft.Text("Help our Cause by Donating!", size=20, weight=ft.FontWeight.BOLD, color="black"),
            name_field, last_name_field, credit_card_field, cvv_field, amount_field,
            ft.ElevatedButton("Donate", bgcolor="#1E90FF", width=300, height=50, style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10),color="white"), on_click=process_donation),
            ft.Row([ft.Image(src="mastercard_logo.png", width=70, height=60), ft.Image(src="paypal_logo.png", width=70, height=60)], alignment=ft.alignment.center, spacing=10),
            feedback_text
        ], alignment=ft.alignment.center, spacing=15),
        bgcolor="white", padding=20, border=ft.border.all(1, "#D3D3D3"), border_radius=10, width=500, height=600, alignment=ft.alignment.center
    )
    
    about_us_section=ft.Container(content=ft.Row(controls=[ft.Column(controls=[about_title,about_content,join_section])],alignment=ft.alignment.center))
    
    # Views with Scroll
    home_view = ft.Container(
        content=ft.ListView(
            controls=[home_bg, top_section, middle_section, quote_section,Our_work_section, gallery_section,to_about_button, footer_section],
            expand=True,
            height=page.height,
        ),
        expand=True,
        visible=True
    )
    about_view = ft.Container(
        content=ft.ListView(
            controls=[about_us_section],
            expand=True,
            spacing=10,
            height=page.height,
            
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
        ft.Text("")
    ], spacing=10, wrap=True)  # Wrap buttons on small screens
    nav_bar = ft.Container(content=ft.Row([logo, nav_buttons], alignment=ft.MainAxisAlignment.SPACE_BETWEEN), bgcolor="#175ABF",)

    # Assemble Page
    page.add(nav_bar, ft.Stack([home_view, about_view, donate_view]))
    on_resize(None)  # Initial resize
    page.update()

ft.app(target=main, view=ft.WEB_BROWSER, assets_dir="assets")