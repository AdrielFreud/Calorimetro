from tkinter import *
import tkinter.messagebox
from tkinter import ttk
import matplotlib.pyplot as plt 
import requests, sys, os

# Email Professora: jane.s.p.i@hotmail.com
menu = """

\tProff: Rosana
\tSerie: 1-B
\tPowered by C.E.S.P
"""

root = Tk()

def Creditos():
	
	cred = Tk()
	cred['bg'] = 'white'
	cred.title('Creditos')
	Label(cred, text=menu, bg='white').place(x=3,y=10)
	Frame(cred, height=3, width=200, bd=1, relief=SUNKEN).place(x=10,y=20)
	Frame(cred, height=3, width=200, bd=1, relief=SUNKEN).place(x=10,y=120)
	cred.geometry('230x150')
	cred.mainloop()

def Exit():
    sys.exit()
    exit()


header = {'User-Agent':"Mozilla /5.0 (Compatible MSIE 9.0;Windows NT 6.1;WOW64; Trident/5.0)"}
nome_calorias = ""
calorias = 0
data = [
	("Bacon", 1, 5.41),
	("Pao", 1, 3.0),
	("Ovos Fritos", 1, 2.4),
	("Pizza de Mussarela", 1, 2.45),
	("Arroz", 1, 1.28),
	("Macarrao Cozido", 1, 1.58),
	("Mortadela", 1, 2.69),
	("Frango Cozido", 1, 1.63),
	("Salame", 1, 3.98),
	("Iogurte", 1, 1.01),
	("Mandioca Cozida", 1, 1.44),
	("Tomate", 1, 0.15),
	("Mandioca Cozida", 1, 1.44),
	("Banana", 1, 0.99),
	("Carne de Porco", 1, 2.62),
	("Pao de Queijo", 1, 2.3)
]

def app_alimentos():
	alimentos = Tk()
	alimentos.title('Alimentos Listados')
	alimentos['bg'] = 'white'
	menubar = Menu(alimentos)
	alimentos.config(menu=menubar)
	filemenu = Menu(menubar)
	menubar.add_cascade(label='Menu', menu=filemenu)

	filemenu.add_command(label='Alimentos', command=app_alimentos)
	filemenu.add_command(label='Somar Calorias', command=somar_calorias)
	filemenu.add_command(label='Adicionar Alimentos', command=add_alimentos)	
	filemenu.add_command(label='Grafico', command=grafico)
	filemenu.add_command(label='Voltar', command=main)
	filemenu.add_command(label='Creditos', command=Creditos)
	filemenu.add_command(label='Exit', command=Exit)
	alimentos.grid()

	dataCols = ('Alimentos Processados', 'Peso (Kg)', '(kcal, kJ)')
	tree = ttk.Treeview(alimentos, columns=dataCols, show='headings')
	tree.grid(row=0, column=0, sticky=N + S + W + E)
	ysb = ttk.Scrollbar(alimentos, orient=VERTICAL, command=tree.yview)
	xsb = ttk.Scrollbar(alimentos, orient=HORIZONTAL, command=tree.xview)
	tree['yscroll'] = ysb.set
	tree['xscroll'] = xsb.set
	ysb.grid(row=0, column=1, sticky=N + S)
	xsb.grid(row=1, column=0, sticky=E + W)
	 
	for c in dataCols:
	    tree.heading(c, text=c.title())

	for item in data:
	    tree.insert('', 'end', values=item)

	alimentos.mainloop()

def calculate_kcal():

	Label(root, text="Entre com a Massa do Alimento:", font="Arial 10", bg='white').place(x=5, y=50)
	
	Frame(root, height=3, width=250, bd=1, relief=SUNKEN).place(x=15,y=30)
	
	massa = Entry()
	massa.place(x=10, y=90)

	Label(root, text="Entre com o calor especifico da Agua", font="Arial 10", bg='white').place(x=5, y=130)
	calor_especifico = Entry()
	calor_especifico.place(x=10, y=170)

	Label(root, text="Variacao da Temperatura da Agua: ", font="Arial 10", bg='white').place(x=5, y=210)
	temp_agua = Entry()
	temp_agua.place(x=10, y=250)

	def show_result():
		result = int(massa.get())*int(calor_especifico.get())-int(temp_agua.get())
		tkinter.messagebox.showinfo('Information', "Este alimentos possui: %s (kcal)"%float(result))

	Button(root, text="Calcular (kcal)", command=show_result).place(x=10, y=350)

	Frame(root, height=3, width=250, bd=1, relief=SUNKEN).place(x=15,y=300)

def add_alimentos():

	add = Tk()
	add['bg'] = 'white'
	add.title("Adicionar Alimentos")

	Label(add, text="Alimento", bg='white').place(x=10, y=20)
	alimento = Entry(add)
	alimento.place(x=100, y=20)

	Label(add, text="Gramas", bg='white').place(x=10, y=60)
	gramas = Entry(add)
	gramas.place(x=100, y=60)

	Label(add, text="Calorias", bg='white').place(x=10, y=100)
	calorias = Entry(add)
	calorias.place(x=100, y=100)

	def right():
		data.append((str(alimento.get()), int(gramas.get()), float(calorias.get())))
		tkinter.messagebox.showinfo('Information', "Adicionado com Sucesso!")

	Button(add, text="Adicionar", command=right).place(x=10, y=160)

	add.geometry("300x200")
	add.mainloop()

def somar_calorias():

	root.destroy()
	somador = Tk()
	somador['bg'] = 'white'
	somador.title('Somar Calorias')
	menubar = Menu(somador)
	somador.config(menu=menubar)
	filemenu = Menu(menubar)
	menubar.add_cascade(label='Menu', menu=filemenu)

	filemenu.add_command(label='Alimentos', command=app_alimentos)
	filemenu.add_command(label='Somar Calorias', command=somar_calorias)
	filemenu.add_command(label='Adicionar Alimentos', command=add_alimentos)	
	filemenu.add_command(label='Grafico', command=grafico)
	filemenu.add_command(label='Voltar', command=main)
	filemenu.add_command(label='Creditos', command=Creditos)
	filemenu.add_command(label='Exit', command=Exit)


	Label(somador, text="Entre com o Nome do Alimento:", font="Arial 10", bg='white').place(x=5, y=50)
	nome_alimento = Entry()
	nome_alimento.place(x=10, y=90)

	Label(somador, text="Quantidade: ", font="Arial 10", bg='white').place(x=5, y=130)
	quantidade = Entry()
	quantidade.place(x=10, y=170)


	def total_calorias():
		global nome_calorias, calorias
		for alimentos in data:
			if alimentos[0].lower() == nome_alimento.get().lower():
				nome_calorias += "%s: %s(kcal)\n"%(nome_alimento.get().lower(), float(alimentos[2])*float(quantidade.get()))
				calorias += float(alimentos[2])*float(quantidade.get())
				Label(somador, text="Calorias Ingeridas: %s (kcal)"%calorias, font="Arial 14", bg='white').place(x=10, y=230)
		
		tkinter.messagebox.showinfo('Information', "%s\nVoce ingeriu: %s (kcal)\n\n"%(nome_calorias, calorias))


	Button(somador, text="Somar", command=total_calorias).place(x=10, y=290)


	somador.geometry("300x350")
	somador.mainloop()


def grafico():
	x = []
	y = []

	for i in data:
		y.append(i[0])
		x.append(i[2])

	plt.title("Calorimetria")

	plt.xlabel("(kcal)")
	plt.ylabel("Alimentos")

	plt.barh(y, x, label="Grupo Massas")
	plt.legend()

	plt.show()

def main():

	root.title("Calorias - 1B")

	root['bg'] = 'white'

	menubar = Menu(root)
	root.config(menu=menubar)
	filemenu = Menu(menubar)
	menubar.add_cascade(label='Menu', menu=filemenu)

	filemenu.add_command(label='Alimentos', command=app_alimentos)
	filemenu.add_command(label='Somar Calorias', command=somar_calorias)
	filemenu.add_command(label='Adicionar Alimentos', command=add_alimentos)	
	filemenu.add_command(label='Grafico', command=grafico)
	filemenu.add_command(label='Voltar', command=main)
	filemenu.add_command(label='Creditos', command=Creditos)
	filemenu.add_command(label='Exit', command=Exit)
	
	calculate_kcal()

	root.geometry("300x400")
	root.mainloop()

main()
