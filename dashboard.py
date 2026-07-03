def render_dashboard():
    layout = {
        "header": "Welcome to Dashboard",
        "body": "Main content goes here"
    }
    return layout

def main():
    print(render_dashboard())

if __name__ == "__main__":
    main()
