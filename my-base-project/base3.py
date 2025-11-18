# Main application file
from calculator import add
from utils import format_name

def run_app():
    print("Running the main application...")
    
    # Simple demo
    user_name = format_name("john", "doe")
    print(f"User: {user_name}")
    
    # Sum
    total = add(10, 5)
    print(f"10 + 5 = {total}")

if __name__ == "__main__":
    run_app()
