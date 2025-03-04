# import flet as ft

# def main(page: ft.Page):
#     page.title = "3-D Helpers"
#     page.bgcolor = "white"
#     page.window.height = 1200
#     page.window.width = 1200
#     page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
#     page.vertical_alignment = ft.MainAxisAlignment.CENTER
#     img = ft.Image(
#         src="",  
#         width=300,  
#         height=200,  
#         fit=ft.ImageFit.CONTAIN  
#     )

#     def home_function():
#         pass
#     def about_us_function():
#         pass
#     def donate_function():
#         pass

#     home_button=ft.ElevatedButton(text="Home",on_click=home_function)
#     donate_button=ft.ElevatedButton(text="Home",on_click=donate_function)
#     about_button=ft.ElevatedButton(text="Home",on_click=about_us_function)

#     button_row = ft.Row(
#         controls=[
#             home_button,
#             donate_button,
#             about_button
#         ],
#         alignment=ft.MainAxisAlignment.END  
#     )

  
#     button_container = ft.Container(
#         content=button_row,  
#         bgcolor="blue",
#         padding=10, 
#         width=page.width, 
#         alignment=ft.alignment.top_right
#     )

#     page.add(button_container,img)
#     page.update()

# ft.app(target=main)

import flet as ft

def main(page: ft.Page):
    page.title = "3-D Helpers"
    page.bgcolor = "white"
    page.window.height = 1200
    page.window.width = 1200
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # Define an image (empty source as placeholder)
    img = ft.Image(
        src="",  
        width=300,  
        height=200,  
        fit=ft.ImageFit.CONTAIN  
    )

    # Functions for buttons
    def home_function(e):
        print("Home button clicked!")

    def about_us_function(e):
        print("About Us button clicked!")

    def donate_function(e):
        print("Donate button clicked!")

    # Correctly define buttons without the trailing commas
    home_button = ft.ElevatedButton(text="Home", on_click=home_function)
    donate_button = ft.ElevatedButton(text="Donate", on_click=donate_function)
    about_button = ft.ElevatedButton(text="About Us", on_click=about_us_function)

    # Create a row to hold the buttons
    button_row = ft.Row(
        controls=[
            home_button,
            donate_button,
            about_button
        ],
        alignment=ft.MainAxisAlignment.START  # Align buttons to the start (left side within the row)
    )

    # Wrap the row inside a container and align it to the top-right of the page
    button_container = ft.Container(
        content=button_row,  # Correctly use 'content' to wrap the row
        bgcolor="blue",
        padding=10, 
        width=page.width,  # Set the container width to fill the page
        alignment=ft.alignment.top_right  # Align the container to the top-right of the page
    )

    # Add both the button container and image to the page
    page.add(button_container, img)
    page.update()

ft.app(target=main)
