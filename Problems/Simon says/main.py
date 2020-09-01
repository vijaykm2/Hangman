def what_to_do(instructions):
    wish = "I won't do it!"

    if instructions.startswith("Simon says") or instructions.endswith("Simon says"):
        wish = "I "
        if instructions.startswith("Simon says"):
            wish += instructions[11:]
        else:
            wish += instructions[:instructions.rfind("Simon says") -1]

    return wish

# print(what_to_do("Simon says make a wish"))