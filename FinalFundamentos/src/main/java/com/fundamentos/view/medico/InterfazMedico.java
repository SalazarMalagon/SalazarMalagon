package com.fundamentos.view.medico;

import java.awt.Color;
import java.awt.Font;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import javax.swing.JButton;
import javax.swing.JFrame;
import static javax.swing.JFrame.EXIT_ON_CLOSE;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.SwingConstants;
import com.fundamentos.persistence.AgendaDAO;
import java.sql.SQLException;

public class InterfazMedico extends JFrame {

    public JPanel panel;
    private String tipoDocumentoRef;
    private long iDMedicoRef;
    private AgendaDAO agenda;

    public InterfazMedico(long iDMedico, String tipoDocumento) {
        iDMedicoRef = iDMedico;
        tipoDocumentoRef = tipoDocumento;
        agenda = AgendaDAO.getInstance(); 
        initCompo();
        mostrar();
    }

    public void initCompo() {
        setSize(600, 200);
        setTitle("Opciones del médico");
        panel = new JPanel();
        panel.setLayout(null);
        this.getContentPane().add(panel);
        setDefaultCloseOperation(EXIT_ON_CLOSE);
    }

    public void mostrar() {
        JLabel titulo = new JLabel("¿Qué acción desea realizar?", SwingConstants.CENTER);
        titulo.setBounds(0, 10, 600, 30);
        titulo.setFont(new Font("Serif", Font.BOLD, 22));
        titulo.setForeground(new Color(21, 67, 96));
        panel.add(titulo);

        JButton creaAgen = new JButton("Crear una agenda");  
        creaAgen.setBounds(200, 70, 200, 30);
        panel.add(creaAgen);

        creaAgen.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                try {
                    CrearAgendaParte1 agen1 = new CrearAgendaParte1(iDMedicoRef, tipoDocumentoRef, agenda.crearAgendaID());
                    agen1.setVisible(true);
                    agen1.setLocationRelativeTo(null);
                } catch (SQLException z) {
                    z.printStackTrace();
                    System.out.println(z.getMessage()); 
                }
            }
        });
    }
}
