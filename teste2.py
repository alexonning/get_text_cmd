from pywinauto import Application
import pyautogui
import time

# Palavra que estamos procurando
palavra_procurada = "exemplo"

# Conectar à janela com o título que contém "teoff-exe"
app = Application(backend="uia").connect(title_re=".*teoff-exe.*")
janela = app.window(title_re=".*teoff-exe.*")

# Função para capturar texto de controles de texto
def get_text_from_window(window):
    texts = []
    try:
        for ctrl in window.descendants():
            if ctrl.window_text():
                texts.append(ctrl.window_text())
    except Exception as e:
        print(f"Erro ao obter o texto dos controles: {e}")
    return texts

# Função principal
def main():
    try:
        # Focar a janela
        janela.set_focus()
        time.sleep(1)  # Pequeno atraso para garantir que a janela está focada
        
        # Obtém o texto de todos os controles
        texto = "\n".join(get_text_from_window(janela))
        
        # Verifica se a palavra procurada está no texto
        if palavra_procurada in texto:
            print(f"'{palavra_procurada}' encontrado! Pressionando Enter...")
            pyautogui.press('enter')  # Pressiona Enter
        else:
            print(f"'{palavra_procurada}' não encontrado.")
    
    except Exception as e:
        print(f"Erro ao processar a janela: {e}")

if __name__ == "__main__":
    main()
