def say(pattern):
    print(escape(pattern), end="")


def escape(pattern: str):
    return pattern.replace('\\n', '\n')\
        .replace('\\r', '\r')\
        .replace('\\t', '\t')\
        .replace('\\b', '\b')\
        .replace('\\0', '\0')\
        .replace('\\\\', '\\')
