package sistema.empleadosDAL;
import java.sql.*;
        
public class conexion {
    
    String strConexionDB = "jdbc:sqlite:D:/Descargas/Mision Tic/Ciclo 2/Bases de Datos/sistema.db";
    
    Connection conn = null;
    
    //metodos constructor
    public conexion(){
        try{
            Class.forName("org.sqlite.JDBC");
            conn = DriverManager.getConnection(strConexionDB);
            System.out.println("Conexion Establecida");
        }
        catch(Exception e){
            System.out.println("Error en la conexion " +e);            
        }
        
    }
    public int ejecutarSentenciaSQL(String strSentenciaSQL){
        try{
            PreparedStatement pstm = conn.prepareStatement (strSentenciaSQL);
            pstm.execute();
            return 1;
        }
        catch(Exception e){
            System.out.println(e);
            return 0;
        }
    }   
    
    public ResultSet consultarRegistros(String strSentenciaSQL){
        try{
            PreparedStatement pstm = conn.prepareStatement (strSentenciaSQL);
            ResultSet respuesta = pstm.executeQuery();
            return respuesta;
        }
        catch(Exception e){
            System.out.println(e);
            return null;
        }
    }    
}
