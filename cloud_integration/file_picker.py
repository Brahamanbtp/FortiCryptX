from google.colab import drive
import ipywidgets as widgets
import os

def mount_drive():
    drive.mount('/content/drive')

def select_file_from_drive():
    files = [f for f in os.listdir("/content/drive/MyDrive") if not f.startswith('.')]
    dropdown = widgets.Dropdown(options=files, description='Select file:')
    display(dropdown)
    return dropdown
