/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package dataTransformStep;
import java.sql.Connection;
import java.sql.SQLException;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.Statement;

/**
 *
 * @author Six
 */
public class ConexionMysqlDao {
    
   private Connection conexion;

    public void setConexion(Connection conexion) {
        this.conexion = conexion;
    }
    
       public Connection getConexion() {
        return this.conexion;
    }
    
      static public void main(String args[]) {
          new ConexionMysqlDao().getConexion();
       }
    
    
    public  Connection RealizarConexion(){
        try {
            if(conexion == null){
                Runtime.getRuntime().addShutdownHook(new getClose());
                Class.forName("com.mysql.jdbc.Driver");
                conexion = DriverManager.getConnection("jdbc:mysql://localhost:3306/contaminantes2","root","root");
                //jdbc:mysql://localhost:3306/contaminantes2?zeroDateTimeBehavior=convertToNull [root on Default schema]
                System.out.println("Conexion a Mysql.Contaminante2 correcta...");
            }
            return conexion;
        } catch (ClassNotFoundException | SQLException e) {
            throw new RuntimeException("Conexion Erronea", e);
        }
    }
    
    public int findByIdElemento(String elemento)throws SQLException{
       //  System.out.println("Iniciando funcin findByIdElemento");

               int idElemento=-1;
               try {
                   Statement sBuscar =conexion.createStatement();
                   ResultSet resultado = sBuscar.executeQuery("select id_elemento from elementos where elemento='"+elemento+"'");
                  while(resultado.next()){
                       idElemento=Integer.parseInt(resultado.getObject(1)+"");
                   }
               } catch (Exception e) {
                   e.printStackTrace();
               }
               return idElemento;
    }
    public  int findByIdEstacion(String claveEstacion) throws SQLException{
        // System.out.println("Iniciando funcin findByIdEstacion");

               int idEstacion=-1;
               try {
                   Statement sBuscar = conexion.createStatement();
                   ResultSet resultado = sBuscar.executeQuery("select id_estacion from estaciones where clave_estacion='"+claveEstacion+"'");
                   while(resultado.next()){
                       idEstacion=Integer.parseInt(resultado.getObject(1)+"");
                   }
               } catch (Exception e) {
               }
               return idEstacion;
       }
    
    
     class getClose extends Thread{
        @Override
        public void run(){
            try {
                conexion.close();
            } catch (SQLException ex) {
                throw new RuntimeException(ex);
            }
        }
     }
     
      public void transferDataFromTxtToMeasureTable(String dataFilePath) throws SQLException{  
        dataFilePath=dataFilePath.replaceAll("\\\\", "\\\\\\\\");
        System.out.println("Se cargara el: "+ dataFilePath+" a mysql");
        String sqlOrder="VACIO";
           try {
               Statement sInsertar = conexion.createStatement();
               sqlOrder = "LOAD DATA LOCAL INFILE  '"+dataFilePath+"' into table\n" 
                          +" mediciones fields terminated by ','\n" 
                          +" lines terminated by '\\n';";
               System.out.println("Ejecutando script: "+ sqlOrder);
               sInsertar.executeQuery(sqlOrder);
               System.out.println("proceso terminado");
           } catch (Exception e) {
               e.printStackTrace();
               System.out.println(sqlOrder);
           }
       }
   }
