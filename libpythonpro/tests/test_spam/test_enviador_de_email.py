import pytest

from libpythonpro.spam.enviador_de_email import Enviador


def test_criar_enviador_de_email():
    enviador= Enviador()
    assert enviador is not None

@pytest.mark.parametrize(
    'destinatario',
    ['estudos.josemarbrito@gmail.com','brito.souza@hotmail.com']
)
def test_remetente(destinatario):
    enviador = Enviador()

    resultado=enviador.enviar(
        destinatario,
        'josemarbritosantos@gmail.com',
        'Teste de enviador de testes curso PythonPro',
        'Primeiro teste de envio de spam'
    )
    assert destinatario in resultado