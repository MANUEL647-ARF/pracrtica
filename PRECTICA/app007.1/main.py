import flet as ft
import random

def verificar_adivinanza(e,page):
    adivinanza_usuario=int(entrada_numero.value)
    
    if adivinanza_usuario==adivina_el_numero:
        text_resultado.value="¡Felicidades! Adivinaste el numero secreto"
        button_adivinar.disabled=True
        page.add(ft.Image(src="feliz.png"))
    
    elif adivinanza_usuario < adivina_el_numero:
        text_resultado.value="¡Fallaste! El numero secreto es mayor"
        page.add(ft.Image(src="triste.png"))
    
    else:
        text_resultado.value="¡Fallastes! El numerosecreto es meno"
        page.add(ft.Image(src="triste.png"))
        
        entrada_numero.value=""
        page.update()



def main(page: ft.Page):

    global adivina_el_numero,entrada_numero,button_adivinar,text_resultado

    page.title="adivina el numero"

    adivina_el_numero=random.randint(1,100)
    
    titulo=ft.Text("adivina el numero",size=25,color="red")
    entrada_numero=ft.TextField(label="tu adivinanza entre 1 y 100",width=300)
    button_adivinar=ft.ElevatedButton("adivinar",on_click=lambda e: verificar_adivinanza(e,page))
    text_resultado=ft.Text("",color="blue")

    contenedor_principal=ft.Container(
        content=ft.Column(
            controls=[
                titulo,
                entrada_numero,
                button_adivinar,
                text_resultado,
                ft.Image(
                    src="https://www.icegif.com/wp-content/uploads/2022/05/icegif-421.gif",
                    fit=ft.ImageFit.COVER,
                    width=350,
                    height=200
                )
            ],alignment="CENTER",
            horizontal_alignment="CENTER",
            spacing=20
        ),
        bgcolor="whithe",
        width=page.window.width,    
        height=page.window.height,
        padding=20
            
        
    )
    page.add(contenedor_principal)

ft.app(main)
