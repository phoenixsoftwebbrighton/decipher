import json
from rich.console import Console
from rich.panel import Panel
from rich.rule import Rule

console = Console()

# --- 1. THE TOOLS ---
def load_json(filename):
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return None

def save_config(config):
    with open('config.json', 'w') as f:
        json.dump(config, f, indent=2)

# This is the "Sanity Check" logic
def is_likely_code(text):
    # A list of keywords that strongly suggest the user pasted code instead of an error
    code_keywords = ['import ', 'def ', 'class ', 'elif ', 'print(', 'if __name__']
    # If any of these words are in the text, we flag it
    return any(keyword in text for keyword in code_keywords)

# --- 2. THE DATA LOADERS ---
error_database = load_json('errors.json')
user_config = load_json('config.json')

# --- 3. THE SETUP (Friendly Onboarding) ---
if not user_config or user_config.get("brain_mode") == "none":
    console.print(Rule("[bold cyan]Decipher[/bold cyan]"))
    onboarding_content = "Welcome to **Decipher**. Let's get you set up.\n\n**1. Local Mode**\n**2. Cloud Mode**"
    console.print(Panel(onboarding_content, title="Welcome!", border_style="cyan", expand=False))
    choice = input("\nPlease enter 1 or 2: ")
    user_config = {"brain_mode": "local" if choice == '1' else "cloud"}
    save_config(user_config)
    console.print(Rule("[bold cyan]Decipher is ready.[/bold cyan]\n"))

# --- 4. THE MAIN INTERFACE (The Mentor) ---
console.rule("[bold cyan]Decipher // Active[/bold cyan]")
console.print(f"[dim]Mode: {user_config['brain_mode'].capitalize()}[/dim]\n")
console.print("👉 *Paste the error message you are seeing below (or type 'exit' to quit)*\n")

while True:
    user_input = input("Paste error here: ")

    if user_input.lower() == 'exit':
        console.print("\n[bold cyan]Happy coding! Goodbye.[/bold cyan]")
        break

    # --- THE SANITY CHECK ---
    if is_likely_code(user_input):
        console.print("\n[bold yellow]⚠️  Wait a second...[/bold yellow]")
        console.print("[dim]It looks like you might have pasted a block of code instead of an error message.[/dim]")
        console.print("[dim]Please try pasting just the error text (e.g., 'SyntaxError: ...')[/dim]\n")
        continue # This skips the rest of the loop and goes back to the prompt

    found = False
    search_term = user_input.lower()

    for entry in error_database:
        if entry['robot_error'].lower() in search_term:
            steps_formatted = ""
            for i, step in enumerate(entry['fix_steps'], 1):
                steps_formatted += f"{i}. {step}\n"

            message = f"[bold]What this means:[/bold] {entry['human_truth']}\n\n" \
                      f"[bold]How to fix it:[/bold]\n{steps_formatted}"
            
            console.print(Panel(message, title="[bold cyan]Translation Found[/bold cyan]", border_style="cyan"))
            found = True
            break

    if not found:
        console.print("[yellow]I don't recognize that error in my notes yet. I'm still learning![/yellow]\n")