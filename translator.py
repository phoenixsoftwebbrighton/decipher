import json
from rich.console import Console
from rich.panel import Panel
from rich.rule import Rule
from rich.prompt import Prompt
from datetime import datetime

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

def save_unknown_error(error_text, context, tool):
    """Saves an unrecognised error to the unknown_errors queue"""
    unknown = load_json('unknown_errors.json') or []
    
    entry = {
        "id": len(unknown) + 1,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "error": error_text,
        "context": context,
        "tool": tool,
        "status": "pending"
    }
    
    unknown.append(entry)
    
    with open('unknown_errors.json', 'w') as f:
        json.dump(unknown, f, indent=2)
    
    return len(unknown)

def is_likely_code(text):
    """Sanity check — detects if user pasted code instead of an error"""
    code_keywords = ['import ', 'def ', 'class ', 'elif ', 'print(', 'if __name__']
    return any(keyword in text for keyword in code_keywords)

def show_unknown_error_queue():
    """Shows how many unrecognised errors are waiting to be added"""
    unknown = load_json('unknown_errors.json') or []
    pending = [e for e in unknown if e.get('status') == 'pending']
    if pending:
        console.print(f"\n[dim]📬 {len(pending)} unrecognised error(s) in the queue — ready to grow the database[/dim]\n")

# --- 2. THE DATA LOADERS ---
error_database = load_json('errors.json') or []
user_config = load_json('config.json')

# --- 3. THE SETUP (Friendly Onboarding) ---
if not user_config or user_config.get("brain_mode") == "none":
    console.print(Rule("[bold cyan]Decipher[/bold cyan]"))
    onboarding_content = (
        "Welcome to **Decipher** — your plain English error translator.\n\n"
        "How would you like to run it?\n\n"
        "**1. Local Mode** — works offline using your own database\n"
        "**2. Cloud Mode** — connects to an AI for errors it doesn't recognise"
    )
    console.print(Panel(onboarding_content, title="Welcome!", border_style="cyan", expand=False))
    choice = input("\nPlease enter 1 or 2: ").strip()
    user_config = {"brain_mode": "local" if choice == '1' else "cloud"}
    save_config(user_config)
    console.print(Rule("[bold cyan]Decipher is ready.[/bold cyan]\n"))

# --- 4. THE MAIN INTERFACE ---
console.rule("[bold cyan]Decipher // Active[/bold cyan]")
console.print(f"[dim]Mode: {user_config['brain_mode'].capitalize()}[/dim]")
console.print(f"[dim]Errors in database: {len(error_database)}[/dim]")
show_unknown_error_queue()
console.print("👉 Paste the error message you are seeing below (or type 'exit' to quit)\n")

while True:
    user_input = input("Paste error here: ").strip()

    if user_input.lower() == 'exit':
        console.print("\n[bold cyan]Keep going. Goodbye. 🙂[/bold cyan]")
        break

    if not user_input:
        continue

    # --- SANITY CHECK ---
    if is_likely_code(user_input):
        console.print("\n[bold yellow]⚠️  Hold on...[/bold yellow]")
        console.print("[dim]That looks like code rather than an error message.[/dim]")
        console.print("[dim]Try pasting just the error line — e.g. 'Permission denied (publickey)'[/dim]\n")
        continue

    # --- SEARCH THE DATABASE ---
    found = False
    search_term = user_input.lower()

    for entry in error_database:
        if entry['robot_error'].lower() in search_term:
            steps_formatted = ""
            for i, step in enumerate(entry['fix_steps'], 1):
                steps_formatted += f"  {i}. {step}\n"

            message = (
                f"[bold]What this means:[/bold]\n  {entry['human_truth']}\n\n"
                f"[bold]How to fix it:[/bold]\n{steps_formatted}"
            )

            console.print(Panel(
                message,
                title="[bold cyan]✅ Translation Found[/bold cyan]",
                border_style="cyan"
            ))
            found = True
            break

    # --- NOT FOUND — COLLECT IT ---
    if not found:
        console.print(Panel(
            "I don't recognise that error yet — but I want to learn it.\n\n"
            "Answer 2 quick questions and I'll save it to the queue.\n"
            "Every unknown error you submit makes Decipher smarter for the next person.",
            title="[bold yellow]🤔 Not In My Database Yet[/bold yellow]",
            border_style="yellow"
        ))

        context = input("\n1. What were you trying to do when this happened?\n   → ").strip()
        
        console.print("\n2. Which tool is this error from?")
        console.print("   1. Ansible    2. Docker    3. Python    4. SSH    5. Other")
        tool_choice = input("   → ").strip()
        
        tool_map = {
            "1": "Ansible",
            "2": "Docker", 
            "3": "Python",
            "4": "SSH",
            "5": "Other"
        }
        tool = tool_map.get(tool_choice, "Other")

        if context:
            entry_number = save_unknown_error(user_input, context, tool)
            console.print(Panel(
                f"Saved as entry #{entry_number} in the queue. ✅\n\n"
                f"Error: {user_input[:80]}...\n"
                f"Tool: {tool}\n"
                f"Context: {context}\n\n"
                "This will be added to the database so it helps the next person too.",
                title="[bold green]📬 Submitted — Thank You[/bold green]",
                border_style="green"
            ))
        else:
            console.print("[dim]No problem — skipped. Come back if you figure out what it was.[/dim]\n")
