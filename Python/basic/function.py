def coba_fungsi():
    print("Hello World!")

coba_fungsi()

def fungsi_dua(fname):
    print(fname + " walawe")

fungsi_dua("byon")
fungsi_dua("linux")
fungsi_dua("mata")

def fungsi_dua_argumen(fname, comm):
    print(fname + " " + comm)

fungsi_dua_argumen("mana", "ada")

def fungsi_tiga(*kids):
    print("anak kecil itu " + kids[2])

fungsi_tiga("putra", "putri", "putre")
