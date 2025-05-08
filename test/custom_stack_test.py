import pytest
from src.custom_stack_class import CustomStack, StackFullException, StackEmptyException

# Teste já existente, mantendo o que você já tinha
def test_push_one_elementinstack():
    element_value = 5.0

    cut = CustomStack(5)
    cut.push(element_value)
    assert cut.is_empty() == False
    assert element_value == cut.top()
    assert 1 == cut.size()

# Testando exceção quando a pilha está cheia
def test_push_full_stack():
    cut = CustomStack(2)
    cut.push(1)
    cut.push(2)
    
    # Usando pytest.raises para garantir que a exceção seja corretamente capturada
    with pytest.raises(StackFullException):
        cut.push(3)

# Testando exceções quando a pilha está vazia
def test_pop_and_top_empty_stack():
    cut = CustomStack(5)
    
    # Testando pop e top em pilha vazia
    with pytest.raises(StackEmptyException):
        cut.pop()

    with pytest.raises(StackEmptyException):
        cut.top()

# Testando o comportamento de pop em pilha não vazia
def test_pop_from_non_empty_stack():
    cut = CustomStack(5)
    cut.push(10)
    
    popped_value = cut.pop()  # Agora o pop deve retornar um valor
    assert popped_value == 10  # Verificando se o valor correto foi removido
    assert cut.is_empty() == True  # A pilha deve estar vazia após o pop
    assert cut.size() == 0  # Tamanho da pilha deve ser 0
