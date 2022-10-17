import ipdb

katz_deli = []

def line(katz_deli):
    if len(katz_deli) == 0:
        print("The line is currently empty.")
    else:
        line_names = [f"{index + 1}. {name}" for index, name in enumerate(katz_deli)]
        line_names = " ".join(line_names)
        print(f"The line is currently: {line_names}")

def take_a_number(katz_deli, name):
    katz_deli.append(name)
    print(f"Welcome, {name}. You are number {len(katz_deli)} in line.")

def now_serving(katz_deli):
    if len(katz_deli) == 0:
        print("There is nobody waiting to be served!")
    else:
        current_customer = katz_deli.pop(0)
        print(f"Currently serving {current_customer}.")


