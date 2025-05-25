import ipywidgets as widgets
from IPython.display import display

def show_main_ui(encrypt_callback, decrypt_callback, view_logs_callback):
    encrypt_btn = widgets.Button(description="🔐 Encrypt File")
    decrypt_btn = widgets.Button(description="🔓 Decrypt File")
    view_logs_btn = widgets.Button(description="📜 View Logs")
    
    output = widgets.Output()
    
    def on_encrypt_clicked(b):
        with output:
            output.clear_output()
            encrypt_callback()
    
    def on_decrypt_clicked(b):
        with output:
            output.clear_output()
            decrypt_callback()
    
    def on_logs_clicked(b):
        with output:
            output.clear_output()
            view_logs_callback()
    
    encrypt_btn.on_click(on_encrypt_clicked)
    decrypt_btn.on_click(on_decrypt_clicked)
    view_logs_btn.on_click(on_logs_clicked)

    display(widgets.HBox([encrypt_btn, decrypt_btn, view_logs_btn]))
    display(output)
