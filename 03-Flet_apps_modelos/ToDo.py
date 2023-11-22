# Apenas uma tradução para pt-br das variáveis e melhor explicação de cada parte do código do aplicativo ToDo da galeria 
# de modelos da documentação do Flet.

# Importando a biblioteca Flet e dando um alias para ela de 'ft'
import flet as ft 

class Tarefa(ft.UserControl):        
    def __init__(self, nome_tarefa, troca_estado_tarefa, excluir_tarefa):
    
        super().__init__()
        self.completado = False        
        self.nome_tarefa = nome_tarefa
        self.troca_estado_tarefa = troca_estado_tarefa
        self.excluir_tarefa = excluir_tarefa

    
    def build(self):
           
        self.display_tarefa = ft.Checkbox(
            value=False, 
            label=self.nome_tarefa, 
            on_change=self.mudanca_estado
        )
                
        self.editar_nome = ft.TextField(expand=1)
       
        self.display_view = ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                self.display_tarefa,
                ft.Row(
                    spacing=0,
                    controls=[
                        ft.IconButton(
                            icon=ft.icons.CREATE_OUTLINED,
                            tooltip="Editar",
                            on_click=self.editar_clicado,
                        ),
                        ft.IconButton(
                            ft.icons.DELETE_OUTLINE,
                            tooltip="Excluir",
                            on_click=self.excluir_clicado,
                        ),
                    ],
                ),
            ],
        )
        
        self.editar_view = ft.Row(
            visible=False,
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                self.editar_nome,
                ft.IconButton(
                    icon=ft.icons.DONE_OUTLINE_OUTLINED,
                    icon_color=ft.colors.GREEN,
                    tooltip="Atualizar",
                    on_click=self.salvar_clicado,
                ),
            ],
        )
       
        return ft.Column(controls=[self.display_view, self.editar_view])

    def editar_clicado(self, e):
        self.editar_nome.value = self.display_tarefa.label
        self.display_view.visible = False
        self.editar_view.visible = True
        self.update()

    def salvar_clicado(self, e):
        self.display_tarefa.label = self.editar_nome.value
        self.display_view.visible = True
        self.editar_view.visible = False
        self.update()

    def mudanca_estado(self, e):
        self.completado = self.display_tarefa.value
        self.troca_estado_tarefa(self)

    def excluir_clicado(self, e):
        self.excluir_tarefa(self)


class TodoApp(ft.UserControl):
    def build(self):
        self.nova_tarefa = ft.TextField(
            hint_text="O que fazer?", 
            on_submit=self.adicionar_clicado, 
            expand=True
        )
        self.tarefas = ft.Column()

        self.filtro = ft.Tabs(
            scrollable=False,
            selected_index=0,
            on_change=self.mudanca_aba,
            tabs=[
                ft.Tab(text="todas"), 
                ft.Tab(text="ativas"), 
                ft.Tab(text="completado")
                ],
        )

        self.itens_restantes = ft.Text("0 itens restantes")

        # application's root control (i.e. "view") containing all other controls
        return ft.Column(
            width=600,
            controls=[
                ft.Row(
                    [ft.Text(value="Fazer", style=ft.TextThemeStyle.HEADLINE_MEDIUM)],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),

                ft.Row(
                    controls=[
                        self.nova_tarefa,
                        ft.FloatingActionButton(
                            icon=ft.icons.ADD, 
                            on_click=self.adicionar_clicado
                        ),
                    ],
                ),
                
                ft.Column(
                    spacing=25,
                    controls=[
                        self.filtro,
                        self.tarefas,
                        ft.Row(
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                            vertical_alignment=ft.CrossAxisAlignment.CENTER,
                            controls=[
                                self.itens_restantes,
                                ft.OutlinedButton(
                                    text="Limpar", 
                                    on_click=self.limpar_clicado
                                ),
                            ],
                        ),
                    ],
                ),
            ],
        )

    def adicionar_clicado(self, e):
        if self.nova_tarefa.value:
            tarefa = Tarefa(self.nova_tarefa.value, self.troca_estado_tarefa, self.excluir_tarefa)
            self.tarefas.controls.append(tarefa)
            self.nova_tarefa.value = ""
            self.nova_tarefa.focus()
            self.atualizar()

    def troca_estado_tarefa(self, tarefa):
        self.atualizar()

    def excluir_tarefa(self, tarefa):
        self.tarefas.controls.remove(tarefa)
        self.atualizar()

    def mudanca_aba(self, e):
        self.atualizar()

    def limpar_clicado(self, e):
        for tarefa in self.tarefas.controls[:]:
            if tarefa.completado:
                self.excluir_tarefa(tarefa)

    def atualizar(self):
        status = self.filtro.tabs[self.filtro.selected_index].text
        count = 0
        for tarefa in self.tarefas.controls:
            tarefa.visible = (
                status == "todas"
                or (status == "ativas" and not tarefa.completado)
                or (status == "completado" and tarefa.completado)
            )
            if not tarefa.completado:
                count += 1
        self.itens_restantes.value = f"{count} itens ativos restantes"
        super().update()


def main(page: ft.Page):
    page.title = "ToDo App"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.scroll = ft.ScrollMode.ADAPTIVE

    # create app control and add it to the page
    page.add(TodoApp())
 
ft.app(main)

