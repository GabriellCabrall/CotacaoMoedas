import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry


def pegar_cotacao():
    pass


lista_moedas = ['USD', 'EUR']

janela = tk.Tk()

janela.title('Ferramenta de Cotação de Moedas')

# Cotação de moeda específica
label_cotacaomoeda = tk.Label(text='Cotação de 1 Moeda Específica', borderwidth=2, relief='solid')
label_cotacaomoeda.grid(row=0, column=0, padx=10, pady=10, sticky='nswe', columnspan=3)

label_selecionarmoeda = tk.Label(text='Selecionar Moeda')
label_selecionarmoeda.grid(row=1, column=0, padx=10, pady=10, sticky='nswe', columnspan=2)

combobox_selecionarmoeda = ttk.Combobox(values=lista_moedas)
combobox_selecionarmoeda.grid(row=1, column=2, padx=10, pady=10, sticky='nswe')

label_selecionardia = tk.Label(text='Selecione o dia que deseja pegar a cotação')
label_selecionardia.grid(row=2, column=0, padx=10, pady=10, sticky='nswe', columnspan=2)

calendario_moeda = DateEntry(year=2023, locale='pt_br')
calendario_moeda.grid(row=2, column=2, padx=10, pady=10, sticky='nswe')

label_textocotacao = tk.Label(text='')
label_textocotacao.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky='nswe')

botao_pegarcotacao = tk.Button(text='Pegar Cotação', command=pegar_cotacao)
botao_pegarcotacao.grid(row=3, column=2, padx=10, pady=10, sticky='nswe')

# Cotação de várias moedas
label_cotacaovariasmoedas = tk.Label(text='Cotação de 1 Múltiplas Moedas', borderwidth=2, relief='solid')
label_cotacaovariasmoedas.grid(row=4, column=0, padx=10, pady=10, sticky='nswe', columnspan=3)

janela.mainloop()