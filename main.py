import flet as ft


def main(page: ft.Page):
    ft.Page.window_height = 740
    ft.Page.window_width = 360
    page.add(ft.SafeArea(ft.Text("Hello, Flet!")))


ft.app(main)
