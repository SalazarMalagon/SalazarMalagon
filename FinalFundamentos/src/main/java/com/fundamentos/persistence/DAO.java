package com.fundamentos.persistence;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;

public class DAO {

    private static DAO instance;
    protected Connection conexion;

    protected DAO() {
        try {
            establecerConexion();
        } catch (SQLException ex) {
            ex.printStackTrace();
        }
    }

    public static DAO getInstance() {  
        if (instance == null) {
            instance = new DAO();
        }
        return instance;
    }

    /**
     * @throws SQLException
     */
    private void establecerConexion() throws SQLException {
        
        String url = "jdbc:postgresql://localhost:5432/eps";
        String user = "lgsus";
        String password = "pass";
        conexion = DriverManager.getConnection(url, user, password);
        System.out.println("Conexión a la base de datos exitosa: " + conexion.getMetaData().getURL());
    }

    public void cerrarConexion() {
        try {
            if (conexion != null && !conexion.isClosed()) {
                conexion.close();
                System.out.println("Conexión cerrada correctamente.");
            }
        } catch (SQLException ex) {
            ex.printStackTrace();
        }
    }

    public boolean getUser(String tabla, String tipo, long id) throws SQLException {
        String consulta = "SELECT * FROM " + tabla + " WHERE k_tipodocumento = ? AND k_numerodocumento = ?;";
        try (PreparedStatement st = conexion.prepareStatement(consulta)) {
            st.setString(1, tipo);
            st.setLong(2, id);
            try (ResultSet user = st.executeQuery()) {
                while (user.next()) {
                    if ("afiliado_beneficiario".equals(tabla)) {
                        if (user.getLong(2) == id && tipo.equals(user.getString(1)) && "Activo".equals(user.getString(4))) {
                            return true;
                        }
                    } else {
                        if (user.getLong(2) == id && tipo.equals(user.getString(1))) {
                            return true;
                        }
                    }
                }
            }
        }
        return false;
    }
}
