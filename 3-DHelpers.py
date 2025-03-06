import flet as ft

def main(page: ft.Page):
    page.title = "3-D Helpers"
    page.bgcolor = "white"
    page.window.height = 1200
    page.window.width = 1200
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.START

   

    about_view = ft.Container(
       
        bgcolor="black",
        content=ft.Text("About Us: Here is some information."),
        visible=False,
        padding=20,
        width=800,
        height=800
    )

    home_view=ft.Container(
    #    img
            
    )
    pay_way=ft.Container(
        # card=ft.Column(control=[
        # # card_number,
        # # owner_name,
        # # due_date,
        # ])
    ) 

    def home_function(e):
        about_view.visible=False
        home_view=True
        page.update()
    def about_us_function(e):
        home_view=False
        about_view.visible=True
        page.update()
    def donate_function(e):

        page.update()

    card_number=ft.TextField,
    owner_name=ft.TextField,
    due_date=ft.TextField,
    home_button=ft.ElevatedButton(text="Home",on_click=home_function,bgcolor="")
    donate_button=ft.ElevatedButton(text="Donate",on_click=donate_function,bgcolor="")
    about_button=ft.ElevatedButton(text="About",on_click=about_us_function,bgcolor="")

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
        alignment=ft.alignment.top_center
    )
    stack = ft.Stack(
        controls=[home_view,about_view,pay_way]
    )
    page.add(button_container,stack)
    page.update()

ft.app(target=main)

