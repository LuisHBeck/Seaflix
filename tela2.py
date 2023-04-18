from tkinter import *
from tkinter import ttk
from create import creat_user
from read import read_user, search_user
from delete import delete_user
from update import modify_user
from matplotlib import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt

janela = Tk()

users_plot = []
ages_plot = []

class ApplicationY():
    def __init__(self):
        self.janela = janela
        self.tela()
        self.frames()
        self.botoes()
        self.labels()
        self.inputs()
        self.lista_frame2()
        self.plot()
        janela.mainloop()

    def tela(self):
        self.janela.title("SEA-FLIX")
        self.janela.geometry('700x700')
        self.janela.configure(background="#333333")
        self.janela.resizable(False, False)
        # self.janela.maxsize(width='700', height='500')
        self.janela.minsize(width='700', height='500')

    def frames(self):
        self.frame_0 = Frame(self.janela, bg='#686868',
                             highlightthickness=0.5, highlightbackground="white", )
        self.frame_0.place(relx=0.03, rely=0.03, relwidth=0.94, relheight=0.09)

        self.frame_1 = Frame(self.janela, bg='#686868',
                             highlightthickness=0.5, highlightbackground="white", )
        self.frame_1.place(relx=0.03, rely=0.13, relwidth=0.94, relheight=0.20)

        self.frame_2 = Frame(self.janela, bg='#686868',
                             highlightthickness=0.5, highlightbackground="white", )
        self.frame_2.place(relx=0.03, rely=0.3, relwidth=0.94, relheight=0.25)

    def botoes(self):
        self.bt_buscar = Button(self.frame_0, text='Buscar', bg="#1F4788", foreground='white', command=self.select_user)
        self.bt_buscar.place(relx=0.29, rely=0.25, relwidth=0.1, relheight=0.5)

        self.bt_limpar = Button(self.frame_0, text='Limpar', bg="#1F4788", foreground='white', command=self.limpar)
        self.bt_limpar.place(relx=0.41, rely=0.25, relwidth=0.1, relheight=0.5)

        # CRUD
        self.bt_create = Button(self.frame_0, text='Create', bg="#1F4788", foreground='white', command=self.insert_user)
        self.bt_create.place(relx=0.53, rely=0.25, relwidth=0.1, relheight=0.5)

        self.bt_read = Button(self.frame_0, text='Read', bg="#1F4788", foreground='white', command=self.show_user)
        self.bt_read.place(relx=0.65, rely=0.25, relwidth=0.1, relheight=0.5)

        self.bt_update = Button(self.frame_0, text='Update', bg="#1F4788", foreground='white', command=self.update_user_2)
        self.bt_update.place(relx=0.77, rely=0.25, relwidth=0.1, relheight=0.5)

        self.bt_delete = Button(self.frame_0, text='Delete', bg="#1F4788", foreground='white', command=self.user_delete)
        self.bt_delete.place(relx=0.89, rely=0.25, relwidth=0.1, relheight=0.5)

    def labels(self):
        self.lb_id_user = Label(self.frame_0, text="ID", background='#19B5FE')
        self.lb_id_user.place(relx=0.005, rely=0.25, relwidth=0.1, relheight=0.5)

        self.lb_name_user = Label(self.frame_1, text="Name", background='#19B5FE')
        self.lb_name_user.place(relx=0.005, rely=0.05, relwidth=0.1, relheight=0.15)

        self.lb_email_user = Label(self.frame_1, text="Email", background='#19B5FE')
        self.lb_email_user.place(relx=0.005, rely=0.25, relwidth=0.1, relheight=0.15)

        self.lb_plan_user = Label(self.frame_1, text="Plan", background='#19B5FE')
        self.lb_plan_user.place(relx=0.005, rely=0.45, relwidth=0.1, relheight=0.15)

        self.lb_type_user = Label(self.frame_1, text="Type", background='#19B5FE')
        self.lb_type_user.place(relx=0.35, rely=0.45, relwidth=0.1, relheight=0.15)

        self.lb_age_user = Label(self.frame_1, text="Age", background='#19B5FE')
        self.lb_age_user.place(relx=0.69, rely=0.45, relwidth=0.1, relheight=0.15)

        self.lb_update_user = Label(self.frame_1, text="UPDATE", background='#19B5FE')
        self.lb_update_user.place(relx=0.005, rely=0.65, relwidth=0.1, relheight=0.15)

        self.lb_update1_user = Label(self.frame_1, text="NEW VALUE", background='#19B5FE')
        self.lb_update1_user.place(relx=0.35, rely=0.65, relwidth=0.1, relheight=0.15)

    def inputs(self):
        self.input_id_user = Entry(self.frame_0)
        self.input_id_user.place(relx=0.11, rely=0.25, relwidth=0.1, relheight=0.5)

        self.input_name_user = Entry(self.frame_1)
        self.input_name_user.place(relx=0.12, rely=0.05, relwidth=0.87, relheight=0.15)

        self.input_email_user = Entry(self.frame_1)
        self.input_email_user.place(relx=0.12, rely=0.25, relwidth=0.87, relheight=0.15)

        self.input_plan_user = Entry(self.frame_1)
        self.input_plan_user.place(relx=0.12, rely=0.45, relwidth=0.19, relheight=0.15)

        self.input_type_user = Entry(self.frame_1)
        self.input_type_user.place(relx=0.46, rely=0.45, relwidth=0.19, relheight=0.15)

        self.input_age_user = Entry(self.frame_1)
        self.input_age_user.place(relx=0.80, rely=0.45, relwidth=0.19, relheight=0.15)

        self.input_update_user = Entry(self.frame_1)
        self.input_update_user.place(relx=0.12, rely=0.65, relwidth=0.19, relheight=0.15)

        self.input_update1_user = Entry(self.frame_1)
        self.input_update1_user.place(relx=0.46, rely=0.65, relwidth=0.19, relheight=0.15)

    def lista_frame2(self):
        self.lista_cliente = ttk.Treeview(self.frame_2, height=3,
                                          columns=('col1', 'col2', 'col3', 'col4', 'col5', 'col6', 'col7'))
        self.lista_cliente.heading('#0', text='')
        self.lista_cliente.heading('#1', text='idUsers')
        self.lista_cliente.heading('#2', text='user_name')
        self.lista_cliente.heading('#3', text='user_age')
        self.lista_cliente.heading('#4', text='user_email')
        self.lista_cliente.heading('#5', text='user_plan')
        self.lista_cliente.heading('#6', text='user_type')

        self.lista_cliente.column("#0", width=1)
        self.lista_cliente.column("#1", width=10)
        self.lista_cliente.column("#2", width=180)
        self.lista_cliente.column("#3", width=50)
        self.lista_cliente.column("#4", width=180)
        self.lista_cliente.column("#5", width=70)
        self.lista_cliente.column("#6", width=50)

        self.lista_cliente.place(relx=0.01, rely=0.1, relwidth=0.98, relheight=0.85)

        self.scroll_lista = Scrollbar(self.frame_2, orient='vertical')
        self.lista_cliente.configure(yscrollcommand=self.scroll_lista.set)
        self.scroll_lista.place(relx=0.96 , rely=0.1, relwidth=0.04, relheight=0.85)

        self.show_user()

    def insert_user(self):
        creat_user(self.input_name_user.get(),
                 self.input_age_user.get(),
                 self.input_email_user.get(),
                 self.input_plan_user.get(),
                 self.input_type_user.get()
                 )
        self.show_user()
        self.plot()

    def show_user(self):
        self.limpar()
        users = read_user()
        for i in users:
            self.lista_cliente.insert("", "end", values=i)
            users_plot.append(i[1])
            ages_plot.append(i[2])

    def limpar(self):
        self.lista_cliente.delete(*self.lista_cliente.get_children())
        self.input_email_user.delete(0, END)
        self.input_name_user.delete(0, END)
        self.input_id_user.delete(0, END)
        self.input_plan_user.delete(0, END)
        self.input_type_user.delete(0, END)
        self.input_age_user.delete(0, END)
        self.input_update_user.delete(0, END)
        self.input_update1_user.delete(0, END)
        

    def user_delete(self):
        delete_user(
            self.input_id_user.get()
        )
        self.show_user()

    def update_user(self):
        modify_user(
            self.input_update_user.get(),
            self.input_update1_user.get(),
            self.input_id_user.get()
        )
        self.show_user()

    def update_user_2(self):
        if self.input_name_user.get():
            self.input_id_user.update()
            self.input_name_user.update()
            self.input_age_user.update()
            self.input_email_user.update()
            self.input_plan_user.update()
            self.input_type_user.update()
            modify_user(
                self.input_id_user.get(),
                self.input_name_user.get(),
                self.input_age_user.get(),
                self.input_email_user.get(),
                self.input_plan_user.get(),
                self.input_type_user.get()
            )
        self.show_user()


    def select_user(self):
        self.lista_cliente.delete(*self.lista_cliente.get_children())
        user = search_user(self.input_id_user.get())
        self.lista_cliente.insert(parent='', index=0, values=user[0])
        self.input_name_user.insert(0, user[0][1])
        self.input_age_user.insert(0, user[0][2])
        self.input_email_user.insert(0, user[0][3])
        self.input_plan_user.insert(0, user[0][4])
        self.input_type_user.insert(0, user[0][5])

    def plot(self):
        figure = plt.Figure(figsize=(13, 5), dpi=50)
        ax = figure.add_subplot(111)
        canva = FigureCanvasTkAgg(figure, self.janela)
        canva.get_tk_widget().place(relx=0.03, rely=0.57)
        data = ages_plot
        def func(pct, allvals):
            pass
        wedges, texts, autotexts = ax.pie(data, autopct=lambda pct: func(pct, data),
                                        textprops=dict(color="w"))

        plt.setp(autotexts, size=8, weight="bold")
        ax.set_title("Matplotlib ages: SEAFLIX")