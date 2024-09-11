from pywinauto import Application
from pywinauto import Desktop

# Conectar à janela com o título que contém "teoff-exe"
app = Application(backend="uia").connect(title_re=".*system32*")

# Encontrar a janela pelo título
janela = app.window(title_re=".*system32*")

# Função para capturar texto de controles de texto
def get_text_from_window(window):
    texts = []
    try:
        # Itera sobre todos os controles na janela
        for ctrl in window.descendants():
            if ctrl.window_text():
                texts.append(ctrl.window_text())
    except Exception as e:
        print(f"Erro ao obter o texto dos controles: {e}")
    return texts

try:
    # Obtém o texto de todos os controles
    texto = "\n".join(get_text_from_window(janela))
    print("Texto da janela:")
    for item in texto.split("\n"):
        if "AlexO>" in item:
            print(texto.split("AlexO>")[1].split("Onning")[0])
    print(texto)
except Exception as e:
    print(f"Erro ao obter o texto da janela: {e}")
