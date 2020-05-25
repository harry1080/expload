// 
// Decompiled by Procyon v0.5.36
// 

package cn.abc.core.sqldict;

import java.util.ArrayList;
import java.util.List;

public class Table
{
    String tableName;
    String tableDescribe;
    List<Row> list;
    
    public Table() {
        this.list = new ArrayList<Row>();
    }
    
    public String getTableDescribe() {
        return this.tableDescribe;
    }
    
    public void setTableDescribe(final String tableDescribe) {
        this.tableDescribe = tableDescribe;
    }
    
    public String getTableName() {
        return this.tableName;
    }
    
    public void setTableName(final String tableName) {
        this.tableName = tableName;
    }
    
    public List<Row> getList() {
        return this.list;
    }
    
    public void setList(final List<Row> list) {
        this.list = list;
    }
}
