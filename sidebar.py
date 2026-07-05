def create_sidebar_component(current_page=None):
    """
    Creates a sidebar component with navigation links as an HTML string.

    Args:
        current_page (str, optional): The name of the current active page.
                                      Used to highlight the active link.

    Returns:
        str: An HTML string representing the sidebar structure.
    """
    # Updated navigation links to match test expectations from test_sidebar.py
    nav_links_data = [
        {"name": "Home", "url": "/"},
        {"name": "Dashboard", "url": "/dashboard"},
        {"name": "Settings", "url": "/settings"},
        {"name": "Profile", "url": "/profile"}
    ]

    # Build the list items for the navigation
    list_items = []
    for link in nav_links_data:
        # Determine if the current link is active based on the page name
        is_active = (link["name"].lower() == current_page.lower()) if current_page else False
        active_class = " class='active'" if is_active else ""
        list_items.append(f"      <li{active_class}><a href='{link['url']}'>{link['name']}</a></li>")

    # Join the list items with a newline
    links_html = "\n".join(list_items)

    # Construct the full sidebar HTML string
    # Ensure indentation matches the test's expectation for "<nav>\n    <ul>"
    sidebar_html = f"""<div class='sidebar'>
  <nav>
    <ul>
{links_html}
    </ul>
  </nav>
</div>"""
    return sidebar_html

if __name__ == "__main__":
    # Example usage
    print("--- Sidebar HTML (Dashboard active) ---")
    sidebar_html = create_sidebar_component(current_page="Dashboard")
    print(sidebar_html)

    print("\n--- Sidebar HTML (Home active) ---")
    sidebar_html_home = create_sidebar_component(current_page="Home")
    print(sidebar_html_home)

    print("\n--- Sidebar HTML (No active page) ---")
    sidebar_html_no_active = create_sidebar_component()
    print(sidebar_html_no_active)
