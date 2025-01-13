package com.fundamentos.view;

import com.fundamentos.view.admin.InterfazAdmi;
import com.fundamentos.view.medico.InterfazMedico;
import com.fundamentos.view.afiliadoBeneficiario.InterfazAfiliadoBeneficiario;
import java.awt.Color;
import java.awt.Font;
import java.awt.event.ActionEvent;
import java.awt.event.KeyAdapter;
import java.awt.event.KeyEvent;
import javax.swing.JButton;
import javax.swing.JComboBox;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.JTextField;
import javax.swing.SwingConstants;
import com.fundamentos.persistence.DAO;
import java.sql.SQLException;

public class IniciarSesion extends JFrame {

    private JPanel panel;
    private DAO controlador;

    public IniciarSesion() {
        initCompo();
        mostrar();
        controlador = DAO.getInstance();

    }

    public void initCompo() {
        setSize(600, 320);
        setTitle("Iniciar Sesión");
        setResizable(false);
        panel = new JPanel();
        panel.setLayout(null);
        this.getContentPane().add(panel);
        setDefaultCloseOperation(EXIT_ON_CLOSE);
    }

    public void mostrar() {
        JLabel titulo = new JLabel("Iniciar Sesión", SwingConstants.CENTER);
        titulo.setBounds(0, 10, 600, 30);
        titulo.setFont(new Font("Serif", Font.BOLD, 22));
        titulo.setForeground(new Color(21, 67, 96));
        panel.add(titulo);

        JLabel tipoD = new JLabel("Tipo");
        tipoD.setBounds(100, 90, 300, 30);
        tipoD.setFont(new Font("Serif", Font.BOLD, 14));
        panel.add(tipoD);

        JLabel textTipoUsuario = new JLabel("¿Quién está ingresando?");
        textTipoUsuario.setBounds(100, 120, 700, 30);
        textTipoUsuario.setFont(new Font("Serif", Font.BOLD, 14));
        panel.add(textTipoUsuario);

        JComboBox<String> tipoUsuario = new JComboBox<>();
        tipoUsuario.addItem("Médico");
        tipoUsuario.addItem("Afiliado/Beneficiario");
        tipoUsuario.setBounds(305, 125, 200, 20);
        panel.add(tipoUsuario);

        JComboBox<String> mTipo = new JComboBox<>();
        mTipo.addItem("Cédula de ciudadanía");
        mTipo.addItem("Cédula de extranjero");
        mTipo.addItem("Pasaporte");
        mTipo.addItem("Registro civil");
        mTipo.setBounds(305, 95, 200, 20);
        mTipo.setBackground(Color.white);
        panel.add(mTipo);

        JLabel id = new JLabel("Número identificación *");
        id.setBounds(100, 150, 300, 30);
        id.setFont(new Font("Serif", Font.BOLD, 14));
        panel.add(id);

        JTextField cID = new JTextField();
        cID.setBounds(305, 155, 200, 20);
        cID.addKeyListener(new KeyAdapter() {
            public void keyTyped(KeyEvent e) {
                if (cID.getText().length() >= 12) {
                    e.consume();
                }
                if (!(e.getKeyChar() >= '0' && e.getKeyChar() <= '9') || e.getKeyChar() == ' ') {
                    e.consume();
                }
            }
        });
        panel.add(cID);

        JButton iSesion = new JButton("Iniciar Sesión");
        iSesion.setSize(150, 30);
        iSesion.setLocation(220, 200);
        panel.add(iSesion);

        JButton botonBack = new JButton("Exit");
        botonBack.setBounds(15, 250, 100, 30);
        botonBack.addActionListener((ActionEvent ae) -> {
            System.exit(0);
        });
        panel.add(botonBack);

        JButton adminView = new JButton("Admin view");
        adminView.setSize(150, 30);
        adminView.setLocation(432, 250);
        adminView.addActionListener((ActionEvent ae) -> {
            InterfazAdmi adminViewInstance = new InterfazAdmi();
            adminViewInstance.setVisible(true);
            adminViewInstance.setLocationRelativeTo(null);
        });
        panel.add(adminView);

        iSesion.addActionListener((ActionEvent ae) -> {
            String userId = cID.getText();
            String tipoUsuarioStr = String.valueOf(tipoUsuario.getSelectedItem());
            String tipoDocumento = String.valueOf(mTipo.getSelectedItem()); 
            if (tipoUsuarioStr.equals("Médico")) {
                try {
                    if (controlador.getUser("medico", tipoDocumento, Long.parseLong(userId))) {
                        IniciarSesion.this.setVisible(false);
                        InterfazMedico medico = new InterfazMedico(Long.valueOf(userId), tipoDocumento);
                        medico.setVisible(true);
                        medico.setLocationRelativeTo(null);
                    } else {
                        JOptionPane.showMessageDialog(null, "Credenciales incorrectas", "Estado login", JOptionPane.WARNING_MESSAGE);
                    }
                } catch (SQLException aex) {
                    aex.printStackTrace();
                    JOptionPane.showMessageDialog(null, "Verifique que sus datos estén correctos", "Estado login", JOptionPane.ERROR_MESSAGE);
                } catch (NumberFormatException aex) {
                    aex.printStackTrace();
                    JOptionPane.showMessageDialog(null, "Rellene correctamente todos los campos obligatorios", "Estado login", JOptionPane.ERROR_MESSAGE);
                }
            } else if (tipoUsuarioStr.equals("Afiliado/Beneficiario")) {
                try {
                    if (controlador.getUser("afiliado_beneficiario", tipoDocumento, Long.parseLong(userId))) {
                        IniciarSesion.this.setVisible(false);
                        InterfazAfiliadoBeneficiario AB = new InterfazAfiliadoBeneficiario(tipoDocumento, Long.valueOf(userId));
                        AB.setVisible(true);
                        AB.setLocationRelativeTo(null);
                    } else {
                        JOptionPane.showMessageDialog(null, "Credenciales incorrectas", "Estado login", JOptionPane.WARNING_MESSAGE);
                    }
                } catch (SQLException aex) {
                    aex.printStackTrace();
                    JOptionPane.showMessageDialog(null, "Ha habido un problema, verifique que los datos son correctos o que su usuario esté activo", "Estado login", JOptionPane.ERROR_MESSAGE);
                } catch (NumberFormatException aex) {
                    aex.printStackTrace();
                    JOptionPane.showMessageDialog(null, "Rellene correctamente todos los campos obligatorios", "Estado login", JOptionPane.ERROR_MESSAGE);
                }
            }
        });
    }
}
