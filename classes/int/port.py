def valid(v):
    return str(v).isdigit() and 0 <= int(v) <= 65535

print valid(1)
