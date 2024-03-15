import ply.lex as lex

tokens = (
    'SELECT',
    'FROM',
    'WHERE',
    'VARIABLE',
    'COMMA',
    'NUMBER',
    'EQUALS',
    'GREATER_THAN',
    'GREATER_THAN_EQUALS',
    'LESS_THAN',
    'LESS_THAN_EQUALS'
)

t_SELECT = r'SELECT'
t_FROM = r'FROM'
t_WHERE = r'WHERE'
t_COMMA = r','
t_EQUALS = r'='
t_GREATER_THAN = r'>'
t_GREATER_THAN_EQUALS = r'>='
t_LESS_THAN = r'<'
t_LESS_THAN_EQUALS = r'<='
t_NUMBER = r'\d+'
t_VARIABLE = r'[a-zA-Z_][a-zA-Z0-9_]*'

t_ignore = ' \t'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

data = 'SELECT id, nome, salario FROM empregados WHERE salario>=820'

lexer.input(data)

for tok in lexer:
    print(tok.type, tok.value, tok.lineno, tok.lexpos)