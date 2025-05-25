import ipywidgets as widgets
from IPython.display import display

USER_PROFILES = {
    "User A": {"email": "usera@example.com", "role": "admin"},
    "User B": {"email": "userb@example.com", "role": "viewer"}
}

def simulate_user():
    dropdown = widgets.Dropdown(
        options=list(USER_PROFILES.keys()),
        description="User Profile:"
    )
    
    output = widgets.Output()
    
    def on_change(change):
        with output:
            output.clear_output()
            selected = change["new"]
            profile = USER_PROFILES[selected]
            print(f"Selected: {selected}")
            print(f"Email: {profile['email']}")
            print(f"Role: {profile['role']}")

    dropdown.observe(on_change, names="value")
    display(dropdown, output)
    return dropdown
