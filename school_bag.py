import error

bag = {}

out = {}


def put(name):
    if name in bag:
        error.print_error_msg(f'Error: {name} is already in the school bag')
    elif name in out:
        bag[name] = out[name]
        out.pop(name)
    else:
        bag[name] = default_value(name)


def default_value(name):
    v = 0.0
    for char in name:
        if not (char.isascii()):
            error.print_error_msg('Error: Char of the name of the stuff put in school bag must be ASCII')
        else:
            if char in value_table:
                v += value_table[char]
    return v


def takeout(name):
    if name in out:
        error.print_error_msg(f'Error: {name} is already taken out')
    if name in bag:
        out[name] = bag[name]
        bag.pop(name)
    else:
        error.print_error_msg(f'Error: {name} is not inside school bag')


def speak(name):
    if name in out:
        print(out[name], end="")
    else:
        error.print_error_msg(f'Error: Loli doesn\'t know what {name} means')


def speak_int(name):
    if name in out:
        print(int(out[name]), end="")
    else:
        error.print_error_msg(f'Error: Loli doesn\'t know what {name} means')


def call(name):
    if name in out:
        print(chr(int(out[name])), end="")
    else:
        error.print_error_msg(f'Error: Loli doesn\'t know what {name} means')


def take(name, value):
    if name in out:
        error.print_error_msg(f'Error: Loli has {name} already')
    else:
        place_out(name, value)


def place_out(name, input_value):
    if is_number(input_value):
        out[name] = float(input_value)
    else:
        i = 0
        for char in input_value:
            i += ord(char)
        out[name] = i


value_table = {
    '!': 1,
    '"': 1,
    '#': 1,
    '$': 1,
    '%': 1,
    '&': 1,
    '\'': 1,
    '(': 1,
    ')': 1,
    '*': 1,
    '+': 1,
    ',': 1,
    '-': 1,
    '.': 1,
    '/': 1,
    '0': 1,
    '1': 1,
    '2': 1,
    '3': 1,
    '4': 1,
    '5': 1,
    '6': 1,
    '7': 1,
    '8': 1,
    '9': 1,
    ':': 1,
    ';': 1,
    '<': 1,
    '=': 1,
    '>': 1,
    '?': 1,
    '@': 1,
    'A': 8,
    'B': 1,
    'C': 2,
    'D': 4,
    'E': 12,
    'F': 2,
    'G': 2,
    'H': 6,
    'I': 6,
    'J': 1,
    'K': 1,
    'L': 4,
    'M': 2,
    'N': 6,
    'O': 7,
    'P': 1,
    'Q': 1,
    'R': 5,
    'S': 6,
    'T': 9,
    'U': 2,
    'V': 1,
    'W': 2,
    'X': 1,
    'Y': 2,
    'Z': 1,
    '[': 1,
    '\\': 1,
    ']': 1,
    '^': 1,
    '_': 1,
    '`': 1,
    'a': 8,
    'b': 1,
    'c': 2,
    'd': 4,
    'e': 12,
    'f': 2,
    'g': 2,
    'h': 6,
    'i': 6,
    'j': 1,
    'k': 1,
    'l': 4,
    'm': 2,
    'n': 6,
    'o': 7,
    'p': 1,
    'q': 1,
    'r': 5,
    's': 6,
    't': 9,
    'u': 2,
    'v': 1,
    'w': 2,
    'x': 1,
    'y': 2,
    'z': 1,
    '{': 1,
    '|': 1,
    '}': 1,
    '~': 1
}


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
