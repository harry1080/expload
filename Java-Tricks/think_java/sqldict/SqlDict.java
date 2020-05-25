// 
// Decompiled by Procyon v0.5.36
// 

package cn.abc.core.sqldict;

import java.sql.ResultSet;
import java.sql.DatabaseMetaData;
import java.sql.Statement;
import java.util.ArrayList;
import java.util.List;
import java.sql.SQLException;
import java.sql.DriverManager;
import java.sql.Connection;

public class SqlDict
{
    public static Connection getConnection(String dbName, String user, String pass) {
        Connection conn = null;
        try {
            Class.forName("com.mysql.jdbc.Driver");
            if (dbName != null && !dbName.equals("")) {
                dbName = "jdbc:mysql://mysqldbserver:3306/" + dbName;
            }
            else {
                dbName = "jdbc:mysql://mysqldbserver:3306/myapp";
            }
            if (user == null || dbName.equals("")) {
                user = "root";
            }
            if (pass == null || dbName.equals("")) {
                pass = "abc@12345";
            }
            conn = DriverManager.getConnection(dbName, user, pass);
        }
        catch (ClassNotFoundException var5) {
            var5.printStackTrace();
        }
        catch (SQLException var6) {
            var6.printStackTrace();
        }
        return conn;
    }
    
    public static List<Table> getTableData(final String dbName, final String user, final String pass) {
        final List<Table> Tables = new ArrayList<Table>();
        final Connection conn = getConnection(dbName, user, pass);
        String TableName = "";
        try {
            final Statement stmt = conn.createStatement();
            final DatabaseMetaData metaData = conn.getMetaData();
            final ResultSet tableNames = metaData.getTables(null, null, null, new String[] { "TABLE" });
            while (tableNames.next()) {
                TableName = tableNames.getString(3);
                final Table table = new Table();
                final String sql = "Select TABLE_COMMENT from INFORMATION_SCHEMA.TABLES Where table_schema = '" + dbName + "' and table_name='" + TableName + "';";
                final ResultSet rs = stmt.executeQuery(sql);
                while (rs.next()) {
                    table.setTableDescribe(rs.getString("TABLE_COMMENT"));
                }
                table.setTableName(TableName);
                final ResultSet data = metaData.getColumns(conn.getCatalog(), null, TableName, "");
                final ResultSet rs2 = metaData.getPrimaryKeys(conn.getCatalog(), null, TableName);
                String PK = "";
                while (rs2.next()) {
                    PK = rs2.getString(4);
                }
                while (data.next()) {
                    final Row row = new Row(data.getString("COLUMN_NAME"), data.getString("TYPE_NAME"), data.getString("COLUMN_DEF"), data.getString("NULLABLE").equals("1") ? "YES" : "NO", data.getString("IS_AUTOINCREMENT"), data.getString("REMARKS"), data.getString("COLUMN_NAME").equals(PK) ? "true" : null, data.getString("COLUMN_SIZE"));
                    table.list.add(row);
                }
                Tables.add(table);
            }
        }
        catch (SQLException var16) {
            var16.printStackTrace();
        }
        return Tables;
    }
}
