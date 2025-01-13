package com.fundamentos.persistence;

import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.Random;

public class AgendaDAO extends DAO {

    private static AgendaDAO instance;  
    private AgendaDAO() {
        super();
    }

    public static AgendaDAO getInstance() {
        if (instance == null) {
            instance = new AgendaDAO();
        }
        return instance;
    }

    public void registrarAgenda(long numeroDocumento, String tipoDocumento, long idAgenda, int mes, int dia) throws SQLException {

        String query = "INSERT INTO agenda VALUES (?,?,?,?,?);";
        try (PreparedStatement ps = conexion.prepareStatement(query)) {
            ps.setString(1, tipoDocumento);
            ps.setLong(2, numeroDocumento);
            ps.setLong(3, idAgenda);
            ps.setInt(4, mes);
            ps.setInt(5, dia);
            ps.execute();
            System.out.println("Agenda registrada correctamente.");
        }
    }

    public long crearAgendaID() throws SQLException {
        Random r = new Random();
        long valorID;
        String query = "SELECT k_agenda FROM agenda WHERE k_agenda = ?;";
        try (PreparedStatement ps = conexion.prepareStatement(query)) {
            do {
                valorID = r.nextInt(9999);
                ps.setLong(1, valorID);
                try (ResultSet rs = ps.executeQuery()) {
                    if (!rs.next()) {
                        break;
                    }
                }
            } while (true);
        }
        return valorID;
    }
}
