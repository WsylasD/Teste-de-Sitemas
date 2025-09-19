import 'package:flutter/material.dart';

void main() {
  runApp(MercadinhoApp());
}

class Produto {
  int id;
  String nome;
  double preco;

  Produto({required this.id, required this.nome, required this.preco});

  @override
  String toString() {
    return "$id - $nome (R\$ ${preco.toStringAsFixed(2)})";
  }
}

class MercadinhoApp extends StatefulWidget {
  @override
  _MercadinhoAppState createState() => _MercadinhoAppState();
}

class _MercadinhoAppState extends State<MercadinhoApp> {
  final List<Produto> _produtos = [];
  final TextEditingController _idController = TextEditingController();
  final TextEditingController _nomeController = TextEditingController();
  final TextEditingController _precoController = TextEditingController();

  int? _selectedIndex;

  void _adicionarProduto() {
    try {
      final id = int.parse(_idController.text);
      final nome = _nomeController.text;
      final preco = double.parse(_precoController.text);

      setState(() {
        _produtos.add(Produto(id: id, nome: nome, preco: preco));
      });

      _limparCampos();
    } catch (e) {
      _mostrarErro("Erro ao adicionar produto!");
    }
  }

  void _atualizarProduto() {
    if (_selectedIndex != null) {
      try {
        final id = int.parse(_idController.text);
        final nome = _nomeController.text;
        final preco = double.parse(_precoController.text);

        setState(() {
          _produtos[_selectedIndex!] =
              Produto(id: id, nome: nome, preco: preco);
        });

        _limparCampos();
      } catch (e) {
        _mostrarErro("Erro ao atualizar produto!");
      }
    }
  }

  void _removerProduto() {
    if (_selectedIndex != null) {
      setState(() {
        _produtos.removeAt(_selectedIndex!);
      });
      _limparCampos();
    }
  }

  void _limparCampos() {
    _idController.clear();
    _nomeController.clear();
    _precoController.clear();
    _selectedIndex = null;
  }

  void _mostrarErro(String mensagem) {
    ScaffoldMessenger.of(context).showSnackBar(
      SnackBar(content: Text(mensagem)),
    );
  }

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Mercadinho CRUD',
      home: Scaffold(
        appBar: AppBar(
          title: Text("Mercadinho CRUD"),
          centerTitle: true,
        ),
        body: Padding(
          padding: EdgeInsets.all(16.0),
          child: Column(
            children: [
              TextField(
                controller: _idController,
                decoration: InputDecoration(labelText: "ID"),
                keyboardType: TextInputType.number,
              ),
              TextField(
                controller: _nomeController,
                decoration: InputDecoration(labelText: "Nome"),
              ),
              TextField(
                controller: _precoController,
                decoration: InputDecoration(labelText: "Preço"),
                keyboardType: TextInputType.number,
              ),
              Row(
                mainAxisAlignment: MainAxisAlignment.spaceEvenly,
                children: [
                  ElevatedButton(onPressed: _adicionarProduto, child: Text("Adicionar")),
                  ElevatedButton(onPressed: _atualizarProduto, child: Text("Atualizar")),
                  ElevatedButton(onPressed: _removerProduto, child: Text("Remover")),
                ],
              ),
              Expanded(
                child: ListView.builder(
                  itemCount: _produtos.length,
                  itemBuilder: (context, index) {
                    final produto = _produtos[index];
                    return ListTile(
                      title: Text(produto.toString()),
                      selected: _selectedIndex == index,
                      onTap: () {
                        setState(() {
                          _selectedIndex = index;
                          _idController.text = produto.id.toString();
                          _nomeController.text = produto.nome;
                          _precoController.text = produto.preco.toString();
                        });
                      },
                    );
                  },
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
