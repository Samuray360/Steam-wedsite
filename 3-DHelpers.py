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

    about_view = ft.Container(
        bgcolor="black",
        content=ft.Text("About Us: Here is some information."),
        visible=False,
        padding=20,
        width=800,
        height=800
    )
    def home_function(about_view):
        about_view.visible=False
        page.update
    def about_us_function(about_view):
        about_view.visible=True
        page.update
    def donate_function():

        page.update


    home_button=ft.ElevatedButton(text="Home",on_click=home_function)
    donate_button=ft.ElevatedButton(text="Donate",on_click=donate_function)
    about_button=ft.ElevatedButton(text="About",on_click=about_us_function)

    button_row = ft.Row(
        controls=[
            home_button,
            about_button,
            donate_button
           
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

    page.add(button_container,img,about_view)
    page.update()

ft.app(target=main)

