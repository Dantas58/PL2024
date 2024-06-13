### Símbolos Terminais
```
T = {'+', '-', '*', '/', '=', '!', '?', '(', ')', var, num }
```
### Símbolos Não Terminais
```
N = {S, exp1, exp2, exp3, op1, op2}
```
### Símbolo Inicial
```
S = S
```

### Regras de Produção
```
P = {
    S -> '?' var           LookAhead = {'?'}
       | var '=' exp1      LookAhead = {var}
       | '!' exp1          LookAhead = {'!'}

    exp1 -> exp2 op1       LookAhead = {'(', var, num}

    op1 -> '+' exp1        LookAhead = {'+'}
         | '-' exp1        LookAhead = {'-'}
         | ε               LookAhead = {')', $}

    exp2 -> exp3 op2       LookAhead = {'(', var, num}

    op2 -> '*' exp1        LookAhead = {'*'}
         | '/' exp1        LookAhead = {'/'}
         | ε               LookAhead = {')', $}

    exp3 -> '(' exp1 ')'   LookAhead = {'('}
          | num            LookAhead = {var}
          | var            LookAhead = {num}
}
```


