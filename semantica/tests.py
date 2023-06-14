import regex
import ply.lex as lex

passString = 'Test case pasado ✅'
failString = 'Test case fallado ❌'

lexer = lex.lex(module=regex)


def test(data):
    lexer.input(data)
    while True:
        tok = lexer.token()
        if not tok:
            break


test('Goku + 4 * < Programa')
