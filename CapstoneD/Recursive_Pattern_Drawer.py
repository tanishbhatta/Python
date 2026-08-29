"""
Capstone 8: RECURSIVE PATTERN DRAWER
"""
def build_chars(count:int) -> str:
    if count == 0:
        return ""
    return "*" + build_chars(count-1)

def draw_fractal(depth:int) -> None:
    if depth == 0:
        return
    draw_fractal(depth-1)
    print(build_chars(depth))
    


draw_fractal(5)



        