import pytest
from unittest.mock import MagicMock
from src.number_asc_order import NumberAscOrder  # Importando a nova classe

def test_sort_numbers():
    # Criando um mock para o CustomStack
    mock_custom_stack = MagicMock()
    
    # Definindo o comportamento do mock para retornar uma lista específica
    mock_custom_stack.is_empty.return_value = False
    mock_custom_stack.elements = [10, 2, 30, 5, 7, 1]
    
    # Criando a instância de NumberAscOrder
    number_asc = NumberAscOrder()
    sorted_numbers = number_asc.sort(mock_custom_stack)

    # Verificando se a lista foi ordenada corretamente
    assert sorted_numbers == [1, 2, 5, 7, 10, 30]

def test_empty_stack_sort():
# Criando um mock para o CustomStack
    mock_custom_stack = MagicMock()
    
    # Definindo o comportamento do mock para retornar uma pilha vazia
    mock_custom_stack.is_empty.return_value = True
    mock_custom_stack.elements = []
    
    # Criando a instância de NumberAscOrder
    number_asc = NumberAscOrder()
    sorted_numbers = number_asc.sort(mock_custom_stack)

    # A pilha está vazia, então o retorno deve ser uma lista vazia
    assert sorted_numbers == []
