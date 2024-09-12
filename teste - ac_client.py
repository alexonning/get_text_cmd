from botcity.core import DesktopBot, Backend

var_desktop = DesktopBot()

# Tentar conectar à primeira janela que corresponde aos critérios
try:
    var_desktop.connect_to_app(Backend.WIN_32, title_re='.*teoff-exe.*', class_name='ConsoleWindowClass')
except Exception as e:
    print(f"Erro ao conectar à janela: {e}")

# Obter a janela conectada
jn_siac = var_desktop.find_app_window(class_name='ConsoleWindowClass', title_re='.*teoff-exe.*')

# Pressionar Control + Shift + A
jn_siac.type_keys("^+a")

var_desktop.wait(500)

jn_siac.type_keys("^c")
# var_desktop.wait(1000)
var_strSicor = var_desktop.get_clipboard()

print(str(var_strSicor).split("Quantidade/Area ....:")[1].split("│")[0])