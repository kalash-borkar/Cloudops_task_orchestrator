def print_banner():
    banner = """
    ======================================
       🚀 CloudOps Task Orchestrator
    ======================================
    """
    print(banner)

def validate_choice(choice):
    if choice.isdigit():
        num = int(choice)
        return 1 <= num <= 6
    return False
