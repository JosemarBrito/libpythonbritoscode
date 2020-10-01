import pytest

from libpythonpro.spam.enviador_de_email import Enviador, EmailInvalido


def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None


@pytest.mark.parametrize(
    'destinatario',
    ['estudos.josemarbrito@gmail.com', 'brito.souza@hotmail.com']
)
def test_remetente(destinatario):
    enviador = Enviador()

    resultado = enviador.enviar(
        destinatario,
        'josemarbritosantos@gmail.com',
        'Curso Python Pro',
        'Treinamento de ferramentas Pytools')
    assert destinatario in resultado


@pytest.mark.parametrize(
    'remetente',
    ['estudos.josemarbrito', '.com']
)
def test_remetente_invalido(remetente):
    enviador = Enviador()
    with pytest.raises(EmailInvalido):
        enviador.enviar(
            remetente,
            'josemarbritosantos@gmail.com',
            'Curso Python Pro',
            'Treinamento de ferramentas Pytools'
        )
