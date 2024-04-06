# Twitter API authentication tokens
access_token = ""
access_token_secret = ""
bearer_token = ""
api_key = ""
api_key_secret = ""

# Function to retrieve Twitter API authentication tokens and keys
def get_key(key_name: str):
    """
    Function to retrieve Twitter API authentication tokens and keys.

    Args:
    - key_name (str): The name of the key to retrieve.

    Returns:
    - str: The value of the specified key.
    """
    # Retrieve the corresponding token or key based on the input key name
    if key_name == "access_token":
        return access_token
    elif key_name == "access_token_secret":
        return access_token_secret
    elif key_name == "bearer_token":
        return bearer_token
    elif key_name == "api_key":
        return api_key
    elif key_name == "api_key_secret":
        return api_key_secret
    else: 
        return ""