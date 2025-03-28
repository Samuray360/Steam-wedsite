import flet as ft
import re
import json
import os
def main(page: ft.Page):
    page.title = "3D-Helpers"
    page.bgcolor = "#FFFFFF"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.padding = 0

    # Variables from Code 1
    logo = ft.Image(src="logo(home).png", width=120, height=80)
    name_field = ft.TextField(label="Name", width=300)
    last_name_field = ft.TextField(label="Last Name", width=300)
    credit_card_field = ft.TextField(label="Credit Card Number", width=300)
    cvv_field = ft.TextField(label="CVV", width=300)
    amount_field = ft.TextField(label="Donation Amount ($)", width=300)
    feedback_text = ft.Text("", color="green", visible=False)
    donation_img = ft.Image(src="Donation_img.png", width=1900, height=950)
    bg_image = ft.Image(src="Join_bg.png", fit=ft.ImageFit.COVER, expand=True, height=600)
    logo_text = ft.Text("3D Helpers", size=24, color="white", weight=ft.FontWeight.BOLD)
    donate_text = ft.Text("Donate now!", size=48, color="white", weight=ft.FontWeight.BOLD)
    home_bg=ft.Image(src="Home.png",width=1900,height=950,)

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
    about_section = ft.Row(
        controls=[
            ft.Image(src="about_us.png", width=200, height=200,),
            ft.Text("We are 3D Helpers, an initiative that combines technology and solidarity to create a meaningful impact.\n Our project integrates graphic design, robotics, and software development to raise awareness about child poverty in the Dominican Republic. \nThrough our platform, anyone can contribute by making donations, which are directed to aid institutions and the production of 3D-printed models.\n\nAs a token of appreciation, each donor receives a 3D-printed car, symbolizing the drive toward a better future. With this effort, \nwe aim not only to alleviate poverty but also to inspire more people to be part of the change.", size=20,color="black"),
        
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=20
    )
    about_Goal = ft.Column([ft.Row(
        controls=[
            ft.Text("At 3D Helpers, our mission is to make a real difference in the fight against child poverty in the Dominican Republic. \nThrough technology and creativity, we strive not only to raise funds but also to increase public awareness of this pressing issue. ", size=20,color="black"),
            ft.Image(src="ladtop.png", width=200, height=200,)
             ],  
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=20
    ), 
            ft.Row(controls=[
                
            ft.Text("Our goal is to make a real difference in the fight against child poverty in the Dominican Republic.\n\nThrough technology and creativity, we strive not only to raise funds but also to increase public awareness of this pressing issue.", 
                    size=20,color="blue"),],spacing=15),
            ft.Image(src="engranaje.png", width=200, height=200,),
            
            ft.Row(controls=[
            ft.Text("Our primary goal is to reach at least RD$6,500 in donations, with 70% \ngoing directly to charitable organizations that support children in vulnerable situations and 30%\n used for the production of 3D-printed models that symbolize our commitment to the cause. With every donation,\n we not only provide aid but also promote innovation and design as powerful tools for social change. ", 
                    size=20,color="black"),
             ft.Image(src="impresora.png", width=200, height=200,),
        ],spacing=40) 
    ])
    
    # Gallery from Code 2
    def gallery_images():
        gallery= ft.Row([
        ft.Image(src="Diseño1.png", width=150, height=150),
        ft.Image(src="Diseño2.png", width=150, height=150),
        ft.Image(src="Diseño3.png", width=150, height=150),
        ft.Image(src="Diseño4.png", width=150, height=150),
        ], alignment=ft.MainAxisAlignment.CENTER, spacing=10)
        return gallery
    
    gallery_pick=gallery_images
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
    home_view = ft.Container(content=ft.Column(controls=[
        
        home_bg,
        top_section,
        middle_section,
        quote_section,
        title_section,
        description_text,
        key_areas,
        # gallery_pick,
        
        footer_section
        
    ],alignment=ft.MainAxisAlignment.START), visible=True)

    about_view = ft.Container(content=ft.Column([about_section,about_Goal,join_section]), visible=False)

    # Donation Form from Code 1
    def validate_credit_card(card_number: str) -> bool:
    # Remove spaces and non-digits
        card_number = re.sub(r'\D', '', card_number)
    
        if not card_number or len(card_number) < 13 or len(card_number) > 19:
            return False
        
        # Luhn Algorithm
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

    # Function to Save Donation Data and Show Feedback
    def process_donation(e):
        # Get field values
        name = name_field.value
        last_name = last_name_field.value
        credit_card = credit_card_field.value
        cvv = cvv_field.value
        amount = amount_field.value

        # Basic Validation
        if not all([name, last_name, credit_card, cvv, amount]):
            feedback_text.value = "Please fill in all fields."
            feedback_text.color = "red"
            feedback_text.visible = True
            page.update()
            return

        # Validate Credit Card
        if not validate_credit_card(credit_card):
            feedback_text.value = "Invalid credit card number."
            feedback_text.color = "red"
            feedback_text.visible = True
            page.update()
            return

        # Validate CVV (basic check: 3 or 4 digits)
        if not (len(cvv) in [3, 4] and cvv.isdigit()):
            feedback_text.value = "Invalid CVV."
            feedback_text.color = "red"
            feedback_text.visible = True
            page.update()
            return

        # Validate Amount (must be a positive number)
        try:
            amount_float = float(amount)
            if amount_float <= 0:
                raise ValueError
        except ValueError:
            feedback_text.value = "Please enter a valid donation amount."
            feedback_text.color = "red"
            feedback_text.visible = True
            page.update()
            return

        # Save Donation Data to a JSON File
        donation_data = {
            "name": name,
            "last_name": last_name,
            "credit_card": credit_card[-4:],  # Store only last 4 digits for security
            "amount": amount_float,
            "timestamp": str(page.now)
        }

        # Append to a JSON file
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
            
            # Show Success Feedback
            feedback_text.value = "Thank you for your donation!"
            feedback_text.color = "green"
            feedback_text.visible = True
            
            # Clear Form
            name_field.value = ""
            last_name_field.value = ""
            credit_card_field.value = ""
            cvv_field.value = ""
            amount_field.value = ""
            
        except Exception as ex:
            feedback_text.value = f"Error saving donation: {str(ex)}"
            feedback_text.color = "red"
            feedback_text.visible = True
        
        page.update()

# Update the Donation Form to Include the Feedback and Button Handler
    donation_form = ft.Container(
    content=ft.Column([
        ft.Text("Help our Cause by Donating!", size=20, weight=ft.FontWeight.BOLD),
        name_field,
        last_name_field,
        credit_card_field,
        cvv_field,
        amount_field,
        ft.ElevatedButton(
            "Donate",
            bgcolor="#1E90FF",
            color="white",
            width=300,
            height=50,
            style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10)),
            on_click=process_donation  # Add the click handler
        ),
        ft.Row([
            ft.Image(src="mastercard_logo.png", width=100, height=80),
            ft.Image(src="paypal_logo.png", width=100, height=80)
        ], alignment=ft.MainAxisAlignment.CENTER, spacing=10),
        feedback_text  # Add the feedback text
    ], alignment=ft.MainAxisAlignment.CENTER, spacing=15),
    bgcolor="#FFFFFF",
    padding=20,
    border=ft.border.all(1, "#D3D3D3"),
    border_radius=10,
    width=350,
    height=550,  # Increased height to accommodate feedback
    alignment=ft.alignment.center
)
    donate_view = ft.Stack([ donation_img,donation_form], visible=False)

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
    )

    # Page Assembly
    stack = ft.Stack([home_view, about_view, donate_view])
    page.add(nav_bar, stack)
    page.update()

ft.app(target=main, view=ft.WEB_BROWSER, assets_dir="assets")