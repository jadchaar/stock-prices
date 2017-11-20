def clean_input(i):
    return i.lower()

def clean_ticker(i):
    return i.lower().replace("^", "-")