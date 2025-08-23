"""
Utility functions for password validation and other common operations.
"""

def validate_password_strength(password: str) -> tuple[bool, list[str]]:
    """
    Validate password strength according to the same rules as Django backend.
    Returns (is_valid, error_messages)
    """
    if len(password) < 8:
        return False, ["Password must be at least 8 characters long"]
    
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" 
    symbols = "!@#$%^&*()_+-=[]{}|;:,.<>?"
    digits = "0123456789"
    
    status_queue = [0, 0, 0, 0]  # [lower, upper, symbols, digits]
    
    for char in password:
        if char in lower:
            status_queue[0] = 1
        elif char in upper:
            status_queue[1] = 1
        elif char in symbols:
            status_queue[2] = 1
        elif char in digits:
            status_queue[3] = 1
        
        if status_queue == [1, 1, 1, 1]:
            break
    
    error_messages = []
    if status_queue[0] == 0:
        error_messages.append("At least one lowercase letter is needed")
    if status_queue[1] == 0:
        error_messages.append("At least one uppercase letter is needed")
    if status_queue[2] == 0:
        error_messages.append("At least one symbol is needed")
    if status_queue[3] == 0:
        error_messages.append("At least one digit is needed")
    
    return len(error_messages) == 0, error_messages

def clean_string(value: str) -> str:
    """Remove spaces from string (replicating Django logic)."""
    return "".join(str(value).split(" "))