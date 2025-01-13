package com.fundamentos.view.medico;

import java.awt.Color;
import java.awt.Font;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.sql.SQLException;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JTextField;
import javax.swing.SwingConstants;

import com.fundamentos.persistence.AgendaDAO;

public class CrearAgendaParte1 extends JFrame {

    public JPanel panel;
    private AgendaDAO agenda;
    private long idMedicoC;
    private String tipoDocumentoC;
    private long idAgendaC;

    public CrearAgendaParte1(long idMedico, String tipoDocumento, long idAgenda) {
        idMedicoC = idMedico;
        tipoDocumentoC = tipoDocumento;
        idAgendaC = idAgenda;
        agenda = AgendaDAO.getInstance();  
        initCompo();
        mostrar();
    }

    public void initCompo() {
        setSize(600, 250);
        setTitle("Crear una agenda");
        panel = new JPanel();
        panel.setLayout(null);
        this.getContentPane().add(panel);
        setDefaultCloseOperation(DISPOSE_ON_CLOSE);
    }

    public void mostrar() {
        JLabel titulo = new JLabel("Crear una agenda", SwingConstants.CENTER);
        titulo.setBounds(0, 10, 600, 30);
        titulo.setFont(new Font("Serif", Font.BOLD, 22));
        titulo.setForeground(new Color(21, 67, 96));
        panel.add(titulo);

        JLabel MAgen = new JLabel("Digite el mes");
        MAgen.setBounds(100, 90, 100, 30);
        MAgen.setFont(new Font("Serif", Font.BOLD, 14));
        panel.add(MAgen);

        JTextField CMAgen = new JTextField();
        CMAgen.setBounds(305, 95, 200, 20);
        panel.add(CMAgen);

        JLabel AAgen = new JLabel("Digite el año");
        AAgen.setBounds(100, 120, 300, 30);
        AAgen.setFont(new Font("Serif", Font.BOLD, 14));
        panel.add(AAgen);

        JTextField CAAgen = new JTextField();
        CAAgen.setBounds(305, 125, 200, 20);
        panel.add(CAAgen);

        JButton continuar = new JButton("Continuar");  
        continuar.setBounds(250, 165, 100, 30);
        panel.add(continuar);

        continuar.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                try {
                    agenda.registrarAgenda(idMedicoC, tipoDocumentoC, idAgendaC, Integer.parseInt(CMAgen.getText()), Integer.parseInt(CAAgen.getText()));
                    CrearAgendaParte2 cont = new CrearAgendaParte2(idMedicoC, tipoDocumentoC, idAgendaC, Integer.parseInt(CMAgen.getText()), Integer.parseInt(CAAgen.getText()));
                    cont.setVisible(true);
                    cont.setLocationRelativeTo(null);
                } catch (SQLException z) {
                    z.printStackTrace();
                }
            }
        });
    }
}
