import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.util.ArrayList;

public class MercadinhoApp extends JFrame {
    private ArrayList<Produto> produtos = new ArrayList<>();
    private DefaultListModel<String> listModel = new DefaultListModel<>();
    private JList<String> listaProdutos = new JList<>(listModel);

    private JTextField campoId = new JTextField(5);
    private JTextField campoNome = new JTextField(10);
    private JTextField campoPreco = new JTextField(7);

    public MercadinhoApp() {
        super("Mercadinho CRUD");

        setLayout(new BorderLayout());

        // Painel de entrada
        JPanel painelEntrada = new JPanel();
        painelEntrada.add(new JLabel("ID:"));
        painelEntrada.add(campoId);
        painelEntrada.add(new JLabel("Nome:"));
        painelEntrada.add(campoNome);
        painelEntrada.add(new JLabel("Preço:"));
        painelEntrada.add(campoPreco);

        JButton btnAdd = new JButton("Adicionar");
        JButton btnUpdate = new JButton("Atualizar");
        JButton btnDelete = new JButton("Remover");

        painelEntrada.add(btnAdd);
        painelEntrada.add(btnUpdate);
        painelEntrada.add(btnDelete);

        add(painelEntrada, BorderLayout.NORTH);
        add(new JScrollPane(listaProdutos), BorderLayout.CENTER);

        // Eventos
        btnAdd.addActionListener(e -> adicionarProduto());
        btnUpdate.addActionListener(e -> atualizarProduto());
        btnDelete.addActionListener(e -> removerProduto());

        listaProdutos.addMouseListener(new MouseAdapter() {
            public void mouseClicked(MouseEvent e) {
                int index = listaProdutos.getSelectedIndex();
                if (index >= 0) {
                    Produto p = produtos.get(index);
                    campoId.setText(String.valueOf(p.getId()));
                    campoNome.setText(p.getNome());
                    campoPreco.setText(String.valueOf(p.getPreco()));
                }
            }
        });

        setSize(600, 400);
        setDefaultCloseOperation(EXIT_ON_CLOSE);
        setVisible(true);
    }

    private void adicionarProduto() {
        try {
            int id = Integer.parseInt(campoId.getText());
            String nome = campoNome.getText();
            double preco = Double.parseDouble(campoPreco.getText());

            Produto p = new Produto(id, nome, preco);
            produtos.add(p);
            listModel.addElement(p.toString());

            limparCampos();
        } catch (Exception ex) {
            JOptionPane.showMessageDialog(this, "Erro ao adicionar produto!");
        }
    }

    private void atualizarProduto() {
        int index = listaProdutos.getSelectedIndex();
        if (index >= 0) {
            try {
                int id = Integer.parseInt(campoId.getText());
                String nome = campoNome.getText();
                double preco = Double.parseDouble(campoPreco.getText());

                Produto p = new Produto(id, nome, preco);
                produtos.set(index, p);
                listModel.set(index, p.toString());

                limparCampos();
            } catch (Exception ex) {
                JOptionPane.showMessageDialog(this, "Erro ao atualizar produto!");
            }
        }
    }

    private void removerProduto() {
        int index = listaProdutos.getSelectedIndex();
        if (index >= 0) {
            produtos.remove(index);
            listModel.remove(index);
            limparCampos();
        }
    }

    private void limparCampos() {
        campoId.setText("");
        campoNome.setText("");
        campoPreco.setText("");
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(MercadinhoApp::new);
    }
}
