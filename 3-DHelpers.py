import flet as ft

def main(page: ft.Page):
    page.title = "3-D Helpers"
    page.bgcolor = "white"
    page.window.height = 1200
    page.window.width = 1200
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    img = ft.Image(
        src="",  
        width=300,  
        height=200,  
        fit=ft.ImageFit.CONTAIN  
    )

    def home_function():
        pass
    def about_us_function():
        pass
    def donate_function():
        pass

    home_button=ft.ElevatedButton(text="Home",on_click=home_function)
    donate_button=ft.ElevatedButton(text="Home",on_click=donate_function)
    about_button=ft.ElevatedButton(text="Home",on_click=about_us_function)

    button_row = ft.Row(
        controls=[
            home_button,
            donate_button,
            about_button
        ],
        alignment=ft.MainAxisAlignment.END  
    )

  
    button_container = ft.Container(
        content=button_row,  
        bgcolor="blue",
        padding=10, 
        width=page.width, 
        alignment=ft.alignment.top_right
    )

    page.add(button_container,img)
    page.update()

ft.app(target=main)

