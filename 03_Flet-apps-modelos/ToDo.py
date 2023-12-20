"""
Apenas uma tradução para pt-br das variáveis e
melhor explicação de cada parte do código do aplicativo ToDo 
da galeria de modelos da documentação do Flet.
"""
import flet as ft # Importando a biblioteca 'Flet' e dando um alias para ela de 'ft'.

class Tarefa(ft.UserControl): # Nova classe, que terá todos os métodos e atributos de ft.UserControl    
    def __init__(self, nome_tarefa, troca_estado_tarefa, excluir_tarefa): 
        """
        Inicializa a tarefa com os parâmetros fornecidos.
    
        Args:
            nome_tarefa (str): O nome da tarefa.
            troca_estado_tarefa (função): Uma função que muda o estado da tarefa.
            excluir_tarefa (função): Uma função que exclui a tarefa.
        """
                
        super().__init__() # Chama o método '__init__()' da superclasse
        
        self.completado = False # Define o estado inicial da tarefa como não completada        
        self.nome_tarefa = nome_tarefa # Define o nome da tarefa
        self.troca_estado_tarefa = troca_estado_tarefa # Define a função que muda o estado da tarefa
        self.excluir_tarefa = excluir_tarefa # Define a função que exclui a tarefa
    
    def build(self): 
        """
        Este trecho de código define um método chamado 'build'(do próprio framework Flet) que constrói 
        e retorna os componentes de interface de usuário para uma tarefa. Ele cria um componente de 
        checkbox para exibir a tarefa, um componente de campo de texto para editar o nome da tarefa e 
        duas linhas de componentes para exibir a tarefa e os botões de edição. O método retorna um 
        componente de coluna que contém a linha de exibição e a linha de edição.
        """
        
        self.display_tarefa = ft.Checkbox( # Cria um componente de checkbox
            value=False, # Inicializa o checkbox como desmarcado
            label=self.nome_tarefa, # Adiciona o nome da tarefa ao checkbox
            on_change=self.mudanca_estado # Define que quando clicado o checkbox, chama a função mudança_estado
        ) # Fim do componente de checkbox
        
        self.editar_nome = ft.TextField(expand=1) # Cria um componente de campo de texto, expandido em 1 pois só tem ele com fator expand
               
        self.display_view = ft.Row( # Cria uma linha para exibir a tarefa
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN, # Alinha os componentes na linha com espaços iguais entre eles
            vertical_alignment=ft.CrossAxisAlignment.CENTER, # Centraliza os componentes na linha
            controls=[ # Adiciona os componentes na linha
                self.display_tarefa, # Adiciona o checkbox da tarefa à linha
                ft.Row( # Cria uma linha para os botões de edição
                    spacing=0, # Define o espaçamento entre os botões, no caso nenhum
                    controls=[ # Adiciona os botões
                        ft.IconButton( # Cria um botão de edição
                            icon=ft.icons.CREATE_OUTLINED, # Define o icône do botão
                            tooltip="Editar", # Define a dica do botão, que aparece ao passar o mouse sobre o botão
                            on_click=self.editar_clicado, # Define a função de clique do botão
                        ), # Fim do botão de edição
                        ft.IconButton( # Cria um botão de exclusão
                            ft.icons.DELETE_OUTLINE, # Define o icône do botão
                            tooltip="Excluir", # Define a dica do botão, que aparece ao passar o mouse sobre o botão
                            on_click=self.excluir_clicado, # Define a função de clique do botão
                        ), # Fim do botão de exclusão
                    ], # Fim dos botões
                ), # Fim da linha dos botões de edição
            ], # Fim dos componentes na linha
        ) # Fim da linha de exibição
                
        self.editar_view = ft.Row( # Cria uma linha para editar a tarefa
            visible=False, # Define que a linha não será visível
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN, # Alinha os componentes na linha com espaços iguais entre eles
            vertical_alignment=ft.CrossAxisAlignment.CENTER, # Centraliza os componentes na linha
            controls=[ # Adiciona os componentes na linha
                self.editar_nome, # Adiciona o campo de texto para editar o nome da tarefa
                ft.IconButton( # Cria um botão de atualização
                    icon=ft.icons.DONE_OUTLINE_OUTLINED, # Define o icône do botão
                    icon_color=ft.colors.GREEN, # Define a cor do icône do botão
                    tooltip="Atualizar", # Define a dica do botão, que aparece ao passar o mouse sobre o botão
                    on_click=self.salvar_clicado, # Define a função de clique do botão
                ), # Fim do botão de atualização
            ], # Fim dos componentes na linha
        ) # Fim da linha de edição
                
        return ft.Column(controls=[self.display_view, self.editar_view]) # Cria um componente de linha para exibir a tarefa e os botões de edição
    

    def editar_clicado(self, e):
        """
        Editar o nome da tarefa quando o botão de editar é clicado. 
        Ele atualiza o nome de uma tarefa, oculta a exibição da tarefa, 
        mostra o editor da tarefa e, em seguida, chama o método "update".

        Parâmetros:
            - e: O evento de clique que disparou a função.

        Tipos de retorno:
            - None
        """
                
        self.editar_nome.value = self.display_tarefa.label # Define o valor do campo de texto para o nome da tarefa
        self.display_view.visible = False # Oculta a exibição da tarefa
        self.editar_view.visible = True # Mostra o editor da tarefa
        self.update() # Chama o método "update" para atualizar a interface de usuário do Flet com as alterações

    def salvar_clicado(self, e):
        """
        Esse código define um método chamado "salvar_clicado" que salva um evento de clique. 
        Ele define o rótulo de um objeto "display_tarefa" com o valor de um objeto "editar_nome". 
        Em seguida, ele torna visível um objeto "display_view" e oculta um objeto "editar_view". 
        Por fim, ele chama um método "update". O método não possui um valor de retorno.

        Parâmetros:
            e: O evento de clique.

        Tipos de retorno:
            None
        """

        self.display_tarefa.label = self.editar_nome.value # Define o rótulo de um objeto "display_tarefa" com o valor de um objeto "editar_nome"
        self.display_view.visible = True # Torna visível um objeto "display_view"
        self.editar_view.visible = False # Oculta um objeto "editar_view"
        self.update() # Chama o método "update" para atualizar a interface de usuário do Flet com as alterações

    def mudanca_estado(self, e):
        """
        Este trecho de código define um método chamado mudanca_estado que lida com mudanças de estado. 
        Ele recebe um objeto Evento como parâmetro. 
        O método atribui o valor de self.display_tarefa.value ao atributo completado e, em seguida, 
        chama o método troca_estado_tarefa com self como argumento. Ele não retorna nada.

        Parâmetros:
            e (Evento): O objeto de evento que acionou a mudança de estado.

        Retorna:
            None
        """

        self.completado = self.display_tarefa.value # Atribui o valor de self.display_tarefa.value ao atributo completado
        self.troca_estado_tarefa(self) # Chama o método troca_lei_tarefa com self como argumento

    def excluir_clicado(self, e):
        """
        Uma função que lida com o evento quando um botão é clicado para excluir uma tarefa.

        Parâmetros:
            e: O objeto de evento que representa o clique no botão.

        Retorna:
            None.
        """

        self.excluir_tarefa(self) # Chama o método excluir_tarefa com self como argumento


class TodoApp(ft.UserControl): # Nova classe, que terá todos os métodos e atributos de ft.UserControl
    def build(self):
        """
        Este trecho de código define um método build que constrói uma interface do usuário.
        A interface consiste em vários controles, como campos de texto, botões, abas e colunas. 
        Os controles são organizados em uma estrutura hierárquica usando linhas e colunas. 
        A interface do usuário resultante possui um cabeçalho, um campo de entrada de texto com um botão
        "Adicionar", um controle de abas para filtrar tarefas, uma coluna para exibir as tarefas 
        e uma linha na parte inferior mostrando o número de itens restantes e um botão "Limpar". 
        O método retorna o controle raiz da interface do usuário.
        """

        self.nova_tarefa = ft.TextField( # Cria um componente de campo de texto
            hint_text="O que fazer?", # Define a dica do campo de texto que aparece ao fundo do campo de texto
            on_submit=self.adicionar_clicado, # Chama a função adicionar_clicado quando o botão for clicado
            expand=True # Expande o campo de texto para a largura do conteiner, pois nesse caso não tem um fator específico
        )
        self.tarefas = ft.Column() # Cria uma coluna para exibir as tarefas

        self.filtro = ft.Tabs( # Cria uma aba para filtrar as tarefas
            scrollable=False, # Desabilita a rolagem
            selected_index=0, # Define a aba selecionada
            on_change=self.mudanca_aba, # Chama a função mudanca_aba quando uma aba for selecionada
            tabs=[ # Cria as abas
                ft.Tab(text="todas"), # Cria uma aba com o texto "todas"
                ft.Tab(text="ativas"), # Cria uma aba com o texto "ativas"
                ft.Tab(text="completado") # Cria uma aba com o texto "completado"
                ], # Fim das abas
        ) # Fim do controle de aba

        self.itens_restantes = ft.Text("0 itens restantes") # Cria um texto para exibir o número de itens restantes

        # application's root control (i.e. "view") containing all other controls
        return ft.Column( # Retorna uma coluna
            width=600, # Define a largura da coluna
            controls=[ # Adiciona os controles na coluna
                ft.Row( # Cria uma linha
                    [ft.Text( # Cria um texto
                        value="Fazer", # Exibe o texto "Fazer"
                        style=ft.TextThemeStyle.HEADLINE_MEDIUM # Define o estilo do texto
                        ) # Fim dos atributos do texto
                    ], # Fim do controle de texto
                    alignment=ft.MainAxisAlignment.CENTER, # Centraliza os componentes na linha
                ), # Fim da linha

                ft.Row( # Cria uma linha
                    controls=[ # Adiciona os controles na linha
                        self.nova_tarefa, # Adiciona a variavel nova_tarefa na linha
                        ft.FloatingActionButton( # Cria um botão flutuante
                            icon=ft.icons.ADD, # Define o icône do botão
                            on_click=self.adicionar_clicado # Chama a função adicionar_clicado ao clique do botão
                        ), # Fim do botão flutuante
                    ], # Fim dos controles
                ), # Fim da linha
                
                ft.Column( # Cria uma coluna
                    spacing=25, # Define o espaçamento entre os componentes
                    controls=[ # Adiciona os controles na coluna
                        self.filtro, # Adiciona a variavel filtro na coluna
                        self.tarefas, # Adiciona a variavel tarefas na coluna
                        ft.Row( # Cria uma linha
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN, # Alinha os componentes na linha com espaços iguais entre eles
                            vertical_alignment=ft.CrossAxisAlignment.CENTER, # Centraliza os componentes na linha
                            controls=[ # Adiciona os controles na linha
                                self.itens_restantes, # Adiciona a variavel itens_restantes na linha
                                ft.OutlinedButton( # Cria um botão com contorno
                                    text="Limpar", # Define o texto do botão como "Limpar"
                                    on_click=self.limpar_clicado # Chama a função limpar_clicado ao clique do botão
                                ), # Fim do botão com contorno
                            ], # Fim dos controles
                        ), # Fim da linha
                    ], # Fim dos controles
                ), # Fim da coluna
            ], # Fim dos controles
        ) # Fim da coluna

    def adicionar_clicado(self, e):
        """
        Uma função para lidar com o evento de adicionar um item clicado.

        Args:
            e: O objeto de evento que representa o evento de clique.

        Returns:
            None
        """

        if self.nova_tarefa.value: # Verifica se o campo de nova tarefa não é vazio
            tarefa = Tarefa(self.nova_tarefa.value, self.troca_estado_tarefa, self.excluir_tarefa) # Chama a função Tarefa para criar uma nova tarefa com o nome fornecido pelo usuário
            self.tarefas.controls.append(tarefa) # Adiciona a tarefa na lista de tarefas na interface
            self.nova_tarefa.value = "" # Limpa o campo de nova tarefa
            self.nova_tarefa.focus() # Coloca o foco no campo de nova tarefa
            self.atualizar() # Atualiza a interface

    def troca_estado_tarefa(self, tarefa):
        """
        Essa função é responsável por trocar o estado de uma tarefa específica.

        Parâmetros:
            tarefa (any): O objeto da tarefa a ser atualizada.

        Retorna:
            None
        """
        self.atualizar() # Atualiza a interface

    def excluir_tarefa(self, tarefa):
        """
        Este trecho de código define um método chamado excluir_tarefa que recebe um parâmetro tarefa. 
        Dentro do método, ele remove a tarefa de uma lista chamada controls no objeto self.tarefas. 
        Após remover a tarefa, ele chama um método chamado atualizar para realizar a operação de atualização.
        
        Args:
+            tarefa: A tarefa a ser removida.
+
+        Returns:
+            None        
        """
        
        self.tarefas.controls.remove(tarefa) # Remove a tarefa da lista
        self.atualizar() # Atualiza a interface

    def mudanca_aba(self, e):
        """
        Altera a aba na interface do usuário.

        Parâmetros:
            e (Event): O objeto de evento que desencadeou a função.

        Retorna:
            None
        """
        self.atualizar() # Atualiza a interface

    def limpar_clicado(self, e):
        """
        Um método para remover tarefas concluídas da lista de tarefas.

        Parâmetros:
            e (Evento): O evento que desencadeou a função.

        Retorna:
            None
        """

        for tarefa in self.tarefas.controls[:]: # Percorre a lista de tarefas
            if tarefa.completado: # Verifica se a tarefa está na lista de completada
                self.excluir_tarefa(tarefa) # Chama o método excluir_tarefa para remover a tarefa

    def atualizar(self):
        """
        Atualiza a visibilidade das tarefas com base no status selecionado no filtro.
        Calcula a contagem das tarefas ativas e atualiza o valor da variável 'itens_restantes'.
        Chama o método 'update' da classe pai.

        Retorna:
            Nenhum
        """

        status = self.filtro.tabs[self.filtro.selected_index].text # Seleciona o texto do filtro
        count = 0 # Cria um contador

        for tarefa in self.tarefas.controls: # Percorre a lista de tarefas
            tarefa.visible = ( # Define a visibilidade da tarefa com base no status selecionado no filtro
                status == "todas" # Todas as tarefas
                or (status == "ativas" and not tarefa.completado) # Tarefas ativas
                or (status == "completado" and tarefa.completado) # Tarefas completadas
            ) # Fim da condição
            if not tarefa.completado: # Verifica se a tarefa não está completada
                count += 1 # Incrementa o contador
        self.itens_restantes.value = f"{count} itens ativos restantes" # Atualiza o valor da variável 'itens_restantes'
        super().update() # Chama o método 'update' da classe pai


def main(page: ft.Page):
    """
    Esse código define uma função chamada main que recebe um objeto ft.Page como argumento. 
    Ele define as propriedades da página principal, como o título, alinhamento horizontal e modo de rolagem. 
    Em seguida, ele cria uma instância do controle TodoApp e o adiciona à página. A função não retorna nada.
    
    Args:
        page (ft.Page): O objeto da página principal.

    Returns:
        None
    """
    page.title = "ToDo App" # Define o título da página
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER # Define o alinhamento horizontal como central
    page.scroll = ft.ScrollMode.ADAPTIVE # Define o modo de rolagem como adaptivo (ajusta automaticamente)
    
    page.add(TodoApp()) # Cria uma instância do controle TodoApp e o adiciona à página
 
ft.app(main) # Chama a função main

