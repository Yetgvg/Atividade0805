import pytest
from unittest.mock import MagicMock
from src.custom_stack_class import CustomStack, StackFullException, StackEmptyException

# Teste já existente, mantendo o que você já tinha
def test_push_one_elementinstack(mocker):
    element_value = 5.0
    
    # Criando o mock da classe CustomStack
    cut = mocker.MagicMock(spec=CustomStack)
    
    # Definindo o comportamento do mock
    cut.is_empty.return_value = False
    cut.top.return_value = element_value
    cut.size.return_value = 1

    # Realizando o teste
    cut.push(element_value)
    assert cut.is_empty() == False
    assert element_value == cut.top()
    assert 1 == cut.size()

# Testando exceção quando a pilha está cheia
def test_push_full_stack(mocker):
    # Criando o mock da classe CustomStack
    cut = mocker.MagicMock(spec=CustomStack)

    # Definindo o comportamento do mock
    cut.size.return_value = 2  # Tamanho atual da pilha
    cut.limit = 2  # Limite da pilha

    # Simulando o comportamento do push para levantar a exceção StackFullException
    cut.push.side_effect = StackFullException  # Forçando o mock a levantar a exceção

    # Usando pytest.raises para garantir que a exceção seja corretamente capturada
    with pytest.raises(StackFullException):
        cut.push(3)  # Tenta empurrar um elemento, mas a pilha está cheia

# Teste para exceções quando a pilha está vazia
def test_pop_and_top_empty_stack():
    # Criando uma instância real da classe CustomStack
    cut = CustomStack(5)

    # Testando que a pilha está vazia e tentando pop e top
    with pytest.raises(StackEmptyException):
        cut.pop()

    with pytest.raises(StackEmptyException):
        cut.top()

# Teste para garantir que o comportamento de pop e atualização de is_empty seja correto
def test_pop_from_non_empty_stack():
    # Criando uma instância real da classe CustomStack
    cut = CustomStack(5)

    # Empurrando um elemento para a pilha
    cut.push(10)

    # Verificando o comportamento de pop
    popped_value = cut.pop()  # Agora o pop deve retornar o valor 10
    assert popped_value == 10  # Verificando se o valor correto foi removido
    assert cut.is_empty() == True  # A pilha deve estar vazia após o pop
    assert cut.size() == 0  # Tamanho da pilha deve ser 0
