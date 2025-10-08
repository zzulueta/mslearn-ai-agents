import json
from pathlib import Path
import uuid
from typing import Any, Callable, Set

# Create a function to submit a support ticket
def submit_support_ticket(email_address: str, description: str) -> str:
    script_dir = Path(__file__).parent  # Get the directory of the script
    ticket_number = str(uuid.uuid4()).replace('-', '')[:6]
    file_name = f"ticket-{ticket_number}.txt"
    file_path = script_dir / file_name
    text = f"Support ticket: {ticket_number}\nStatus: Submitted\nSubmitted by: {email_address}\nDescription:\n{description}"
    file_path.write_text(text)

    message_json = json.dumps({"message": f"Support ticket {ticket_number} submitted. The ticket file is saved as {file_name}"})
    return message_json

# Function to get the status of a support ticket
def get_ticket_status(ticket_number: str) -> str:
    script_dir = Path(__file__).parent
    file_name = f"ticket-{ticket_number}.txt"
    file_path = script_dir / file_name
    if not file_path.exists():
        return json.dumps({
            "error": f"Ticket {ticket_number} not found."
        })
    with file_path.open() as f:
        for line in f:
            if line.startswith("Status:"):
                status = line.split(":", 1)[1].strip()
                return json.dumps({
                    "ticket_number": ticket_number,
                    "status": status
                })
    return json.dumps({
        "error": f"Status not found in ticket {ticket_number}."
    })


# Define a set of callable functions
user_functions: Set[Callable[..., Any]] = {
    submit_support_ticket,
    get_ticket_status
}


