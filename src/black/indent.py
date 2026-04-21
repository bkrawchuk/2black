from black.const import INDENT_WIDTH

def get_indent(depth: int) -> str:
    return " " * (depth * INDENT_WIDTH)
