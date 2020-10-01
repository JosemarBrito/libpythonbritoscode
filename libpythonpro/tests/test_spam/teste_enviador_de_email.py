from libpythonpro.spam.enviador_de_email import Enviador


def test_criar_enviador_de_email():
    enviador= Enviador()
    assert enviador is not None

def test_remetente():
    enviador = Enviador()
    resultado = enviador.enviar(
        'estudos.josemarbrito@gmail.com',
        'josemarbritosantos@gmail.com',
        'Curso Python Pro',
        'Treinamento de ferramentas Pytools'
    )
    assert 'estudos.josemarbrito@gmail.com' in resultado