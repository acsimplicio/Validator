from validate_docbr import CPF, CNPJ


def validate_cpf(number: str):
    cpf = CPF()
    return cpf.validate(number)


def validate_cnpj(number: str):
    cnpj = CNPJ()
    return cnpj.validate(number)
