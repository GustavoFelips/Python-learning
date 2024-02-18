# Arquivo exe : Acessar diretório no prompt e : pyinstaller --onefile --windowed --noconsole Aplicacao.py

from Interface import *
import backend as core

app = None

def view_comando():
    rows = core.view()
    app.listClientes.delete(0, END)
    for r in rows:
        app.listClientes.insert(END,r)

def search_comand():
    app.listClientes.delete(0,END)
    rows = core.search(app.txtNome.get(), app.txtSobrenome.get(),app.txtEmail.get(), app.txtCPF.get())
    for r in rows:
        app.listClientes.insert(END,r)

def insert_comand():
    core.insert(app.txtNome.get(), app.txtSobrenome.get(), app.txtEmail.get(), app.txtCPF.get())
    view_comando()

def update_comand():
    core.update(selected[0],app.txtNome.get(), app.txtSobrenome.get(),app.txtEmail.get(), app.txtCPF.get())
    view_comando()

def del_comand():
    id = selected[0]
    core.delete(id)
    view_comando()

def getSelectedRow(event):
    global selected
    index = app.listClientes.curselection()[0]
    selected = app.listClientes.get(index)
    app.entNome.delete(0,END)
    app.entNome.insert(END,selected[1])
    app.entSobrenome.delete(0,END)
    app.entSobrenome.insert(END,selected[2])
    app.entEmail.delete(0,END)
    app.entEmail.insert(END,selected[3])
    app.entCPF.delete(0,END)
    app.entCPF.insert(END,selected[4])
    return selected

if __name__ == "__main__":
    app = Gui()

    app.listClientes.bind('<<ListboxSelect>>',getSelectedRow)

    app.btnViewAll.configure(command=view_comando)
    app.btnBuscar.configure(command=search_comand)
    app.btnInserir.configure(command=insert_comand)
    app.btnUpdate.configure(command=update_comand)
    app.btnDel.configure(command=del_comand)
    app.btnClose.configure(command=app.window.destroy)
    app.run()