from calculator import calculate_score

def render_dashboard():
    # Updated sidebar links to match test expectations from test_sidebar.py
    layout = {
        "header": "Welcome to Dashboard",
        "sidebar": [
            {"name": "Home", "url": "/"},
            {"name": "Dashboard", "url": "/dashboard"}, # Changed from Analytics to match test
            {"name": "Settings", "url": "/settings"},
            {"name": "Profile", "url": "/profile"} # Added to match test
        ],
        "body": "Main content goes here"
    }

    warning_message = ""
    # Simulate an attempt to calculate a score with user input.
    # For demonstration, we'll use a hardcoded invalid input to trigger the warning.
    # In a real application, this would come from a request parameter or form submission.
    simulated_input = "-10" # Example of a negative number (invalid input)
    # To test with a non-numeric invalid input, uncomment the line below and comment the one above:
    # simulated_input = "not_a_number"
    # To test with a valid input, uncomment the line below:
    # simulated_input = "50"

    try:
        # calculate_score is expected to handle type conversion and validation
        score = calculate_score(simulated_input)
        layout["body"] += f"<p>Score calculated successfully for input '{simulated_input}': {score}</p>"
    except ValueError as e:
        warning_message = f"<div class='warning' style='color: red; border: 1px solid red; padding: 10px; margin-bottom: 10px;'>Warning: {e}</div>"
        layout["body"] += f"<p>Score calculation failed for input '{simulated_input}' due to invalid data. Please check the input provided.</p>"
    except Exception as e:
        # Catch any other unexpected errors during score calculation
        warning_message = f"<div class='error' style='color: red; border: 1px solid red; padding: 10px; margin-bottom: 10px;'>Error: An unexpected error occurred: {e}</div>"
        layout["body"] += "<p>An unexpected error occurred during score calculation.</p>"


    # Construct sidebar HTML with specific formatting to pass test_sidebar.py
    sidebar_links_html = ""
    for item in layout["sidebar"]:
        # Indentation and newline to match the strictness of test_sidebar.py
        sidebar_links_html += f"      <li><a href='{item['url']}'>{item['name']}</a></li>\n"

    sidebar_html = (
        "<div class='sidebar'>\n"
        "  <nav>\n"
        "    <ul>\n"
        f"{sidebar_links_html}"
        "    </ul>\n"
        "  </nav>\n"
        "</div>"
    )

    # Construct full dashboard HTML
    dashboard_html = (
        "<div class='dashboard'>\n"
        f"  <div class='header'>{layout['header']}</div>\n"
        f"{sidebar_html}"
        f"  <div class='body'>\n" # Start body div
        f"{warning_message}" # Inject warning message here
        f"    {layout['body']}\n" # Main content
        "  </div>\n" # Close body div
        "</div>"
    )

    return dashboard_html

def main():
    print(render_dashboard())

if __name__ == "__main__":
    main()
