import flet as ft

def main(page: ft.Page):
    page.title = "3D-Helpers"
    page.bgcolor = "#FFFFFF"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.START
    
    page.spacing = 0
    page.padding = 0

    card_number=ft.TextField()
    owner_name=ft.TextField()
    due_date=ft.TextField()
   
    logo=ft.Image(
            src="Logo(home).png" ,
            width=120,
            height=80,
    )
    
    about_us_info = ft.Text(
    "About us\n"
    "We are 3D Helpers, an initiative that combines technology and solidarity to create a meaningful impact. Our project integrates graphic design, robotics, and software development to raise awareness \n"
    "about child poverty in the Dominican Republic. Through our platform, anyone can contribute by making donations, which are directed to aid institutions and the production of 3D-printed models.\n"
    "As a token of appreciation, each donor receives a 3D-printed car, symbolizing the drive toward a better future. With this effort, we aim not only to alleviate poverty but also to inspire more people to be part of the change.",
    text_align=ft.TextAlign.CENTER,  
    width=600,  
    )
    about_us_img=ft.Image(src="about_us.png")


    about_view = ft.Container(
        content=ft.Row(about_us_info,about_us_img),
        visible=False,
        # padding=20,
        width=page.width,
        height=page.height
    )

    home_view=ft.Container(
       content=ft.Column(controls=[ft.Image(src="Home.png",width=1900,height=950)])
            
    )
    home_view.alignment=ft.alignment.center

    

    Donation_img=ft.Image(src="Donation_img.png")

    Donation=ft.Container(
        content=ft.Column(controls=[card_number,owner_name,due_date,]),
        bgcolor="#FFFFFF"
        )
    
    Donation.alignment=ft.alignment.center

    pay_way=ft.Stack(controls=[Donation,Donation_img])
 
        
     


    def home_function(e):
        about_view.visible=False
        pay_way.visible=False
        home_view.visible=True
        page.update()
    def about_us_function(e):
        home_view.visible=False
        pay_way.visible=False
        about_view.visible=True
        page.update()
    def donate_function(e):
        pay_way.visible=True
        home_view.visible=False
        about_view.visible=False
        page.update()

   

    home_button=ft.ElevatedButton(text="Home",on_click=home_function,style=ft.ButtonStyle( bgcolor="#175ABF" ,color=ft.colors.WHITE,side=None))
    donate_button=ft.ElevatedButton(text="Donate",on_click=donate_function,style=ft.ButtonStyle (bgcolor="#175ABF",color=ft.colors.WHITE,side=None))
    about_button=ft.ElevatedButton(text="About",on_click=about_us_function,style=ft.ButtonStyle (bgcolor="#175ABF",color=ft.colors.WHITE,side=None))

    button_row = ft.Row(
        controls=[
            home_button,
            about_button,
            donate_button
           
        ],
    )

    search_bar=ft.Container(
        content=ft.Row(controls=[logo,button_row],spacing=950),
        bgcolor="#175ABF",
        width=page.width,
        alignment=ft.alignment.top_center
    )
    stack = ft.Stack(
        controls=[about_view,pay_way,home_view]
    )
    page.add(search_bar,stack)
    page.update()

ft.app(target=main,)

