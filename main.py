import flet as ft
from flet import View, Page, AppBar, ElevatedButton, Text, app
from flet import RouteChangeEvent, ViewPopEvent, CrossAxisAlignment, MainAxisAlignment



def main(page: Page) -> None:
    page.title = 'My Store'
    page.window_height = 740
    page.window_width = 360
    
    def route_change(e: RouteChangeEvent) -> None:
        page.views.clear()

        # Home view
        page.views.append(
            View(
                route="/",
                controls=[
                    AppBar(title=Text("Home"), bgcolor='green'),
                    Text(value='home', size=30),
                    ElevatedButton(text="Got to Store", on_click=lambda _: page.go('/store'))
                ],
                vertical_alignment=MainAxisAlignment.CENTER,
                horizontal_alignment=CrossAxisAlignment.CENTER,
                spacing=26
            )
        )

        if page.route == '/store':
            page.views.append(
                View(
                    route="/store",
                    controls=[
                        AppBar(title=Text("Store"), bgcolor='pink'),
                        Text(value='Store', size=30),
                        ElevatedButton(text="Got to Home", on_click=lambda _: page.go('/'))
                    ],
                    vertical_alignment=MainAxisAlignment.CENTER,
                    horizontal_alignment=CrossAxisAlignment.CENTER,
                    spacing=26
                    )
                )
        page.update()

    def view_pop(e: ViewPopEvent) -> None:
        page.views.pop()
        top_view: View = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)

app(main)
