values = {
    '->': 'import',
    'PT': 'print',
    'IT': 'input',
    'IF': 'if',
    'EF': 'elif',
    'EE': 'else',
    'FR': 'for',
    'RG': 'range',
    '*-': 'in',
    '!!': 'not',
    '$': 'int',
    '|': 'str',
    '~': 'float',
    'TY': 'try',
    'EX': 'expect',
    'RT': 'return',
    'WE': 'while',
    'RM': 'random',
    'RI': 'randint',
    'RC': 'choice',
    'BR': 'break',
    'AN': 'and',
    'TM': 'time',
    'SP': 'sleep',
    'DF >> ': 'def',
    'FL': 'False',
    'TR': 'True',
    '<->': 'or',
    'LW': 'lower',
    'UP': 'upper',
    'ON': 'open',
    'AS': 'as',
    'CH': 'choice',
    '<': '(',
    '>': ')',
    '.>': '>',
    '.<': '<',
    '??': '#',
    'MA': 'math',
    '&': 'as',
    'COS': 'cos',
    'SIN': 'sin',
    'TAN': 'tan',
    'ER': 'Exeption'
}

def func_replace(target, values):
    for i, j in values.items():
        target = target.replace(i, j)
    return target

with open('main.bj', 'r') as f:
    code = f.read()
    py = func_replace(code, values)
    exec(py)