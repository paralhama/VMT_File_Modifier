import os
import tkinter as tk
from tkinter import filedialog, messagebox, ttk


class VMTModifierApp:
    def __init__(self, master):
        self.master = master
        master.title("VMT File Modifier")
        master.geometry("500x400")
        master.resizable(False, False)

        # Estilo
        self.style = ttk.Style()
        self.style.configure("TLabel", font=("Arial", 10))
        self.style.configure("TButton", font=("Arial", 10))

        # Frame principal
        self.main_frame = ttk.Frame(master, padding="20 20 20 20")
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        # Diretório
        ttk.Label(self.main_frame, text="Diretório de Destino:", style="TLabel").pack(anchor="w", pady=(0, 5))

        self.directory_frame = ttk.Frame(self.main_frame)
        self.directory_frame.pack(fill=tk.X, pady=(0, 10))

        self.directory_entry = ttk.Entry(self.directory_frame, width=50)
        self.directory_entry.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=(0, 10))

        self.directory_button = ttk.Button(
            self.directory_frame,
            text="Selecionar Diretório",
            command=self.select_directory
        )
        self.directory_button.pack(side=tk.RIGHT)

        # String de Busca
        ttk.Label(self.main_frame, text="String para Buscar:", style="TLabel").pack(anchor="w", pady=(0, 5))
        self.search_entry = ttk.Entry(self.main_frame, width=50)
        self.search_entry.pack(fill=tk.X, pady=(0, 10))

        # String de Substituição
        ttk.Label(self.main_frame, text="String para Substituir:", style="TLabel").pack(anchor="w", pady=(0, 5))
        self.replace_entry = ttk.Entry(self.main_frame, width=50)
        self.replace_entry.pack(fill=tk.X, pady=(0, 10))

        # Botão Processar
        self.process_button = ttk.Button(
            self.main_frame,
            text="Processar Arquivos VMT",
            command=self.process_files
        )
        self.process_button.pack(pady=20)

        # Log de Processamento
        ttk.Label(self.main_frame, text="Log de Processamento:", style="TLabel").pack(anchor="w", pady=(0, 5))
        self.log_text = tk.Text(self.main_frame, height=8, width=50, state='disabled')
        self.log_text.pack(fill=tk.X)

    def select_directory(self):
        directory = filedialog.askdirectory(title="Selecione o diretório para modificação")
        if directory:
            self.directory_entry.delete(0, tk.END)
            self.directory_entry.insert(0, directory)

    def process_files(self):
        # Validações
        directory = self.directory_entry.get()
        search_string = self.search_entry.get()
        replace_string = self.replace_entry.get()

        if not directory:
            messagebox.showerror("Erro", "Selecione um diretório!")
            return

        if not search_string:
            messagebox.showerror("Erro", "Digite a string para buscar!")
            return

        if not replace_string:
            messagebox.showerror("Erro", "Digite a string para substituir!")
            return

        # Limpa log anterior
        self.log_text.config(state='normal')
        self.log_text.delete(1.0, tk.END)

        # Processamento
        modified_files_count = 0
        try:
            for root, dirs, files in os.walk(directory):
                for filename in files:
                    if filename.lower().endswith('.vmt'):
                        filepath = os.path.join(root, filename)

                        try:
                            with open(filepath, 'r', encoding='utf-8') as file:
                                content = file.read()

                            # Verifica se a string de busca está exatamente no arquivo
                            # e se já não foi substituída anteriormente
                            if search_string in content and replace_string not in content:
                                new_content = content.replace(search_string, replace_string)

                                with open(filepath, 'w', encoding='utf-8') as file:
                                    file.write(new_content)

                                modified_files_count += 1
                                log_message = f"Modificado: {filepath}\n"
                                self.log_text.insert(tk.END, log_message)
                                self.log_text.see(tk.END)
                                self.master.update_idletasks()

                            # Adiciona log de não modificação quando relevante
                            elif replace_string in content:
                                log_message = f"Já modificado: {filepath}\n"
                                self.log_text.insert(tk.END, log_message)
                                self.log_text.see(tk.END)
                                self.master.update_idletasks()

                        except Exception as e:
                            error_message = f"Erro em {filepath}: {e}\n"
                            self.log_text.insert(tk.END, error_message)
                            self.log_text.see(tk.END)
                            self.master.update_idletasks()

        except Exception as e:
            messagebox.showerror("Erro", f"Erro durante processamento: {e}")

        # Finalização
        self.log_text.config(state='disabled')
        messagebox.showinfo(
            "Concluído",
            f"Processo finalizado!\nArquivos VMT modificados: {modified_files_count}"
        )


def main():
    root = tk.Tk()
    app = VMTModifierApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
