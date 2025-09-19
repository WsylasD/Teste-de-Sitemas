# ------------------------------------------------------------
# Título: Testes Unitários do Sistema Mercadinho
# Autor: Silas Gabriel
# Data: 18/09/2025
#
# Cenários de Teste:
# 1. Adicionar produto → deve retornar True se o produto for novo.
# 2. Cadastro de produto duplicado → deve retornar False e manter apenas o produto original.
# 3. Buscar produto → deve retornar o objeto quando existir.
# 4. Buscar produto inexistente → deve retornar None.
# 5. Atualizar nome do produto → deve alterar somente o nome.
# 6. Atualizar preço do produto → deve alterar somente o preço.
# 7. Atualizar produto inexistente → deve retornar False.
# 8. Remover produto existente → deve retornar True.
# 9. Remover produto inexistente → deve retornar False.
# 10. Listagem de produtos → deve retornar todos os produtos cadastrados.
# 11. Limpeza da lista → deve deixar a lista vazia.
# 12. Controle de estoque → deve atualizar apenas a quantidade.
#
# Execução:
# - Cada teste cria um novo objeto Mercadinho (setUp).
# - Um Produto é adicionado, atualizado, buscado ou removido conforme o cenário.
#
# Verificação:
# - assertTrue confirma sucesso da operação.
# - assertFalse confirma falha esperada (como duplicado ou inexistente).
# - assertIsNotNone confirma que o produto existe.
# - assertIsNone confirma que o produto não existe.
# - assertEqual confirma atualização correta ou contagem da lista.
# - assertIn / assertNotIn confirma inclusão ou exclusão correta da lista.
# ------------------------------------------------------------

import unittest
from mercadinho import Mercadinho, Produto

class TestMercadinho(unittest.TestCase):
    def setUp(self):
        # Cria um "mercado" limpo antes de cada teste
        self.mercado = Mercadinho()

    def test_cenarioA01_adicionar_produto(self):
        # Cenário 1: Cadastro de produto válido - Silas, 18/09/2025

        #Execução:
        produto = Produto(1, "Produto 1", 10.0, 10)

        # Verficação:
        # Verifica se retornou True ao cadastrar
        self.assertTrue(self.mercado.adicionar_produto(produto))

        # Verifica se o produto realmente entrou na lista
        self.assertIn(produto, self.mercado.listar_produtos())

    def test_cenarioA02_cadastro_produto_duplicado(self):
        # Cenário 2: Cadastro de produto duplicado - Silas, 18/09/2025
        produto1 = Produto(1, "Produto 1", 10.0, 10)
        produto2 = Produto(1, "Produto 2", 20.0, 20)

        # Execução:
        # Primeiro cadastro deve funcionar
        self.assertTrue(self.mercado.adicionar_produto(produto1))

        # Tentativa de cadastro duplicado deve retornar False
        self.assertFalse(self.mercado.adicionar_produto(produto2))

        # Verificação:
        # A lista deve conter apenas o produto original
        produtos = self.mercado.listar_produtos()
        self.assertEqual(len(produtos), 1)
        self.assertIn(produto1, produtos)
        self.assertNotIn(produto2, produtos)

    def test_cenarioA03_buscar_produto(self):
        # Cenário 3: busca de produto existente - Silas, 18/09/2025
        produto = Produto(1, "produto 1", 10.0, 10)
        self.mercado.adicionar_produto(produto)

        # Execução: 
        # buscar produto pelo ID
        resultado = self.mercado.buscar_produto(1)

        # Verificação:
        self.assertIsNotNone(resultado)  # produto deve existir
        self.assertEqual(resultado.nome, "produto 1")
        self.assertEqual(resultado.preco, 10.0)
        self.assertEqual(resultado.quantidade, 10)

    def test_cenarioA04_busca_produto_inexistente(self):
        # Cenário 4: busca de produto inexistente - Silas, 18/09/2025

        # Nenhum produto cadastrado ainda
        resultado = self.mercado.buscar_produto(1)  # ID que não existe

        # Verificação:
        self.assertIsNone(resultado)  # deve retornar None


    def test_cenarioA05_atualizar_nome_produto(self):
        # Cenário 5: Atualização de nome do produto - Silas, 18/09/2025
        produto = Produto(1, "produto 1", 10.0, 10)
        self.mercado.adicionar_produto(produto)

        # Execução:
        # Atualizar apenas o nome
        execucao = self.mercado.atualizar_produto(1, {"nome": "produto 2"})

        # Verificação:

        # Verifica se o produto foi atualizado corretamente
        self.assertTrue(execucao)

        # Verifica se os outros atributos não foram alterados
        resultado = self.mercado.buscar_produto(1)
        self.assertEqual(resultado.nome, "produto 2") # nome atualizado
        self.assertEqual(resultado.preco, 10.0) # preco nao alterado
        self.assertEqual(resultado.quantidade, 10) # quantidade nao alterada

    def test_cenarioA06_atualizar_preco_produto(self):
        # Cenário 6: Atualização de preço do produto - Silas, 18/09/2025
        produto = Produto(1, "produto 1", 10.0, 10)
        self.mercado.adicionar_produto(produto)

        # Execução:
        # Atualizar apenas o preco
        execucao = self.mercado.atualizar_produto(1, {"preco": 20.0})

        # Verificação:

        # Verifica se o produto foi atualizado corretamente
        self.assertTrue(execucao)

        # Verifica se os outros atributos não foram alterados
        resultado = self.mercado.buscar_produto(1)
        self.assertEqual(resultado.nome, "produto 1") # nome não alterado
        self.assertEqual(resultado.preco, 20.0) # preco atualizado
        self.assertEqual(resultado.quantidade, 10) # quantidade não alterada

    def test_cenarioA07_atualizar_produto_inexistente(self):
        # Cenário 7: Atualização de produto inexistente - Silas, 18/09/2025

        # Execução:
        # Atualizar produto inexistente
        execucao = self.mercado.atualizar_produto(1, {"preco": 20.0})

        # Verificação:
        # Verifica se o retorno é falso na tentativa de atualizar
        self.assertFalse(execucao)

    def test_cenarioA08_remover_produto(self):
        # Cenário 8: Remoção de produto existente - Silas, 18/09/2025
        produto = Produto(1, "produto 1", 10.0, 10)
        self.mercado.adicionar_produto(produto)

        # Execução:
        # Remover produto existente
        self.assertTrue(self.mercado.remover_produto(1))

        # Verificação:
        # Verifica se o produto foi removido corretamente
        produto = self.mercado.buscar_produto(1)
        self.assertIsNone(produto)

    def test_cenarioA09_remover_produto_inexistente(self):
        # Cenário 9: Remoção de produto inexistente - Silas, 18/09/2025
        produto = Produto(1, "produto 1", 10.0, 10)
        self.mercado.adicionar_produto(produto)

        # Execução:
        # Tentativa de Remover produto inexistente deve retornar False
        self.assertFalse(self.mercado.remover_produto(2))

        # Verificação:
        # Verifica se a lista de produtos não foi alterada
        produtos = self.mercado.listar_produtos()
        self.assertEqual(len(produtos), 1)
        self.assertIn(produto, produtos) # produto original não alterado

    def test_cenarioA10_listagem_produtos(self):
        # Cenário 10: Listagem de produtos - Silas, 18/09/2025
        produto1 = Produto(1, "produto 1", 10.0, 10)
        produto2 = Produto(2, "produto 2", 20.0, 20)
        self.mercado.adicionar_produto(produto1)
        self.mercado.adicionar_produto(produto2)

        # Execução:
        # Listagem de produtos
        produtos = self.mercado.listar_produtos()

        # Verificação:
        # Verifica se a listagem retornou os produtos cadastrados
        self.assertEqual(len(produtos), 2)
        self.assertIn(produto1, produtos)
        self.assertIn(produto2, produtos)

    def test_cenarioA11_limpeza_lista(self):
        # Cenário 11: Limpeza da lista - Silas, 18/09/2025
        produto1 = Produto(1, "produto 1", 10.0, 10)
        produto2 = Produto(2, "produto 2", 20.0, 20)
        produto3 = Produto(3, "produto 3", 30.0, 30)
        self.mercado.adicionar_produto(produto1)
        self.mercado.adicionar_produto(produto2)
        self.mercado.adicionar_produto(produto3)

        # Execução:
        # Limpeza da lista
        self.mercado.limpar()

        # Verificação:
        # Verifica se a lista foi limpa corretamente
        self.assertEqual(len(self.mercado.produtos), 0)

    def test_cenarioA12_controle_estoque(self):
        # Cenário 12: Controle de estoque - Silas, 18/09/2025
        produto = Produto(1, "produto 1", 10.0, 10)
        self.mercado.adicionar_produto(produto)

        # Execução:
        # Atualizar apenas a quantidade
        execucao = self.mercado.atualizar_produto(1, {"quantidade": 20})

        # Verificação:

        # Verifica se o produto foi atualizado corretamente
        self.assertTrue(execucao)

        # Verifica se os outros atributos não foram alterados
        resultado = self.mercado.buscar_produto(1)
        self.assertEqual(resultado.nome, "produto 1") # nome não alterado
        self.assertEqual(resultado.preco, 10.0) # preco não alterado
        self.assertEqual(resultado.quantidade, 20) # quantidade atualizada

if __name__ == "__main__":
    unittest.main(verbosity=2)