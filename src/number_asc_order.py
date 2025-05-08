class NumberAscOrder:
    def sort(self, custom_stack):
        # Verifica se a pilha não está vazia
        if custom_stack.is_empty():
            return []
        
        # Ordena os números da pilha
        sorted_list = sorted(custom_stack.elements)  # elements é a lista interna da pilha
        return sorted_list
