import flet as ft

def main(page: ft.Page):
    page.title = "3-D Helpers"
    page.bgcolor = "white"
    page.window.height = 1200
    page.window.width = 1200
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER


    tittle = ft.Text("3D-Helpers",size=30,color="blue")




     
    page.add(tittle)
    page.update()

ft.app(target=main)

