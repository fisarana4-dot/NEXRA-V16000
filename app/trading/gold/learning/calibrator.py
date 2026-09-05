def adjust(c,ok):
    return min(1,c+.01) if ok else max(0,c-.02)
