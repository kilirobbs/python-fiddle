def humanize_bytes(bytes, kilo=1024):
    import math
    label = [" KB", " MB" , " GB", " TB"]

    if bytes < kilo:
        return "%d" % bytes
    elif bytes > kilo and bytes < math.pow(kilo, 2):
        return "%.2F%s" % (float(bytes/kilo), label[0])
    elif bytes > math.pow(kilo, 2) and bytes < math.pow(kilo, 3):
        return "%.2F%s" % (float(bytes/math.pow(kilo, 2)), label[1])
    elif bytes > math.pow(kilo, 3) and bytes < math.pow(kilo, 4):
        return "%.2F%s" % (float(bytes/math.pow(kilo, 3)), label[2])
    elif bytes > math.pow(kilo, 4) and bytes < math.pow(kilo, 5):
        return "%.2F%s" % (float(bytes/math.pow(kilo, 4)), label[3])

print humanize_bytes(123456789)