
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont, QCursor
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
                               QLineEdit, QMainWindow, QPushButton, QWidget, QMessageBox)
from Login_e_cadastro import Ui_MainWindow

def login():
    return

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = Ui_MainWindow()
    window.showMaximized()
    sys.exit(app.exec())



    # def open_image(self):
    #     file_dialog = QFileDialog()
    #     file_path, _ = file_dialog.getOpenFileName(self, "Open Image", "", "Images(*.png *.xpm *.jpg *.jpeg *.bmp);;All Files (*)")

    #     if file_path:
    #         # Criar diretório de destino se não existir
    #         save_dir = "images"
    #         if not os.path.exists(save_dir):
    #             os.makedirs(save_dir)

    #         # Definir novo nome para a imagem (exemplo: usando o nome do usuário)
    #         user_name = self.tela_formulario.input_nome.text().replace(" ", "_")
    #         new_file_name = f"{user_name}.jpg"  # Salvar sempre como .jpg para padronização

    #         # Caminho completo do arquivo de destino
    #         self.new_file_path = os.path.join(f"projeto_pyside/", save_dir, new_file_name)

    #         # Copiar a imagem para a pasta de destino
    #         shutil.copy(file_path, self.new_file_path)

    #         # Exibir a imagem na interface
    #         pixmap = QPixmap(self.new_file_path)
    #         self.tela_formulario.layout_img.setPixmap(pixmap)
    #         self.tela_formulario.layout_img.setScaledContents(True)
    #         self.tela_formulario.layout_img.setPixmap(pixmap)
