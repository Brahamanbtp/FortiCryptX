import ipywidgets as widgets
from IPython.display import display

def challenge_response_auth(expected_answer, callback_on_success):
    question = "What is your decryption passphrase?"
    input_box = widgets.Text(description="Passphrase:", placeholder='Enter passphrase...', layout=widgets.Layout(width='50%'))
    button = widgets.Button(description="✔️ Submit")
    output = widgets.Output()
    
    def on_click(b):
        with output:
            output.clear_output()
            if input_box.value == expected_answer:
                print("✅ Authenticated. Proceeding...")
                callback_on_success()
            else:
                print("❌ Incorrect passphrase.")
    
    button.on_click(on_click)
    display(widgets.VBox([widgets.Label(question), input_box, button, output]))
