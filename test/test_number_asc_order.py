import pytest
from src.custom_stack_class import CustomStack
from src.number_asc_order import NumberAscOrder  # Importando a nova classe

def test_sort_numbers():
    # Criando uma pilha com 6 números sorteados
    custom_stack = CustomStack(6)
    custom_stack.push(10)
    custom_stack.push(2)
    custom_stack.push(30)
    custom_stack.push(5)
    custom_stack.push(7)
    custom_stack.push(1)

    # Criando a instância de NumberAscOrder
    number_asc = NumberAscOrder()
    sorted_numbers = number_asc.sort(custom_stack)

    assert sorted_numbers == [1, 2, 5, 7, 10, 30]  # Verificando se os números estão ordenados corretamente

def test_empty_stack_sort():
    # Testando uma pilha vazia
    custom_stack = CustomStack(6)
    number_asc = NumberAscOrder()
    sorted_numbers = number_asc.sort(custom_stack)

    assert sorted_numbers == []  # A pilha está vazia, então o retorno deve ser uma lista vazia
