"""
Utility functions for validation and string operations with regex patterns.
"""

import re
from typing import Optional, Tuple, List
from email.utils import parseaddr


# Compiled regex patterns for efficiency
class ValidationPatterns:
    """Pre-compiled regex patterns for validation."""

    # Password validation patterns
    LOWERCASE = re.compile(r'[a-z]')
    UPPERCASE = re.compile(r'[A-Z]')
    DIGIT = re.compile(r'\d')
    SYMBOL = re.compile(r'[!@#$%^&*()_+\-=\[\]{}|;:,.<>?]')

    # Email validation pattern (RFC 5322 compliant)
    EMAIL = re.compile(
        r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    )

    # Phone number patterns
    PHONE_COMMON = re.compile(r'^\+[1-9]\d{1,14}$')

    # URL validation
    URL = re.compile(
        r'^https?://'  # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?|'  # domain...
        r'localhost|'  # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE
    )

    # Common patterns
    WHITESPACE = re.compile(r'\s+')
    ALPHANUMERIC = re.compile(r'^[a-zA-Z0-9]+$')
    USERNAME = re.compile(r'^[a-zA-Z0-9_.-]{3,30}$')


def validate_password_strength(password: str) -> Tuple[bool, List[str]]:
    """
    Validate password strength using efficient regex patterns.

    Args:
        password: The password string to validate

    Returns:
        Tuple of (is_valid, error_messages)
    """
    if not password or not isinstance(password, str):
        return False, ["Password is required"]

    error_messages = []

    # Check minimum length
    if len(password) < 8:
        error_messages.append("Password must be at least 8 characters long")

    # Check maximum length for security
    if len(password) > 128:
        error_messages.append("Password must be less than 128 characters long")

    # Use regex patterns for efficient validation
    patterns_and_errors = [
        (ValidationPatterns.LOWERCASE, "At least one lowercase letter is required"),
        (ValidationPatterns.UPPERCASE, "At least one uppercase letter is required"),
        (ValidationPatterns.DIGIT, "At least one digit is required"),
        (ValidationPatterns.SYMBOL, "At least one symbol is required")
    ]

    for pattern, error_msg in patterns_and_errors:
        if not pattern.search(password):
            error_messages.append(error_msg)

    return len(error_messages) == 0, error_messages


def validate_email(email: str) -> Tuple[bool, Optional[str]]:
    """
    Validate email address using regex pattern.

    Args:
        email: Email string to validate

    Returns:
        Tuple of (is_valid, error_message)
    """
    if not email or not isinstance(email, str):
        return False, "Email is required"

    # Remove leading/trailing whitespace
    email = email.strip()

    # Check length constraints
    if len(email) > 254:  # RFC 5321 limit
        return False, "Email address is too long"

    # Basic regex validation
    if not ValidationPatterns.EMAIL.match(email):
        return False, "Invalid email format"

    # Additional validation using email.utils for RFC compliance
    parsed_name, parsed_email = parseaddr(email)
    if parsed_email != email:
        return False, "Invalid email format"

    return True, None


def validate_phone_number(phone: str, international: bool = False) -> Tuple[bool, Optional[str]]:
    """
    Validate phone number using regex patterns.

    Args:
        phone: Phone number string to validate
        international: Whether to use international format validation

    Returns:
        Tuple of (is_valid, error_message)
    """
    if not phone or not isinstance(phone, str):
        return False, "Phone number is required"

    # Remove all whitespace and common separators for validation
    clean_phone = re.sub(r'[-.\s()]', '', phone.strip())

    if international:
        if not ValidationPatterns.PHONE_COMMON.match(phone):
            return False, "Invalid international phone number format"
    else:
        if not ValidationPatterns.PHONE_COMMON.match(phone):
            return False, "Invalid phone number format"

    return True, None


def validate_url(url: str) -> Tuple[bool, Optional[str]]:
    """
    Validate URL using regex pattern.

    Args:
        url: URL string to validate

    Returns:
        Tuple of (is_valid, error_message)
    """
    if not url or not isinstance(url, str):
        return False, "URL is required"

    url = url.strip()

    if not ValidationPatterns.URL.match(url):
        return False, "Invalid URL format"

    return True, None


def validate_username(username: str) -> Tuple[bool, Optional[str]]:
    """
    Validate username using regex pattern.

    Args:
        username: Username string to validate

    Returns:
        Tuple of (is_valid, error_message)
    """
    if not username or not isinstance(username, str):
        return False, "Username is required"

    username = username.strip()

    if not ValidationPatterns.USERNAME.match(username):
        return False, "Username must be 3-30 characters and contain only letters, numbers, dots, hyphens, or underscores"

    return True, None


def clean_string(value: str, remove_whitespace: bool = True) -> str:
    """
    Clean string by removing or normalizing whitespace.

    Args:
        value: String to clean
        remove_whitespace: Whether to remove all whitespace (True) or normalize it (False)

    Returns:
        Cleaned string
    """
    if not isinstance(value, str):
        value = str(value)

    if remove_whitespace:
        # Remove all whitespace
        return ValidationPatterns.WHITESPACE.sub('', value)
    else:
        # Normalize whitespace (replace multiple spaces with single space)
        return ValidationPatterns.WHITESPACE.sub(' ', value.strip())


def sanitize_input(value: str, max_length: Optional[int] = None) -> str:
    """
    Sanitize user input by removing potentially harmful characters.

    Args:
        value: Input string to sanitize
        max_length: Maximum allowed length

    Returns:
        Sanitized string
    """
    if not isinstance(value, str):
        value = str(value)

    # Remove null bytes and other control characters
    sanitized = re.sub(r'[\x00-\x08\x0B\x0C\x0E-\x1F\x7F]', '', value)

    # Strip leading/trailing whitespace
    sanitized = sanitized.strip()

    # Truncate if max_length is specified
    if max_length and len(sanitized) > max_length:
        sanitized = sanitized[:max_length]

    return sanitized


def is_alphanumeric(value: str) -> bool:
    """
    Check if string contains only alphanumeric characters.

    Args:
        value: String to check

    Returns:
        True if alphanumeric, False otherwise
    """
    if not isinstance(value, str):
        return False

    return bool(ValidationPatterns.ALPHANUMERIC.match(value))