// 
// Decompiled by Procyon v0.5.36
// 

package cn.abc.core.sqldict;

public class Row
{
    String name;
    String type;
    String def;
    String isNull;
    String isAuto;
    String remark;
    String isPK;
    String size;
    
    public String getIsPK() {
        return this.isPK;
    }
    
    public void setIsPK(final String isPK) {
        this.isPK = isPK;
    }
    
    public String getName() {
        return this.name;
    }
    
    public void setName(final String name) {
        this.name = name;
    }
    
    public String getType() {
        return this.type;
    }
    
    public void setType(final String type) {
        this.type = type;
    }
    
    public String getDef() {
        return this.def;
    }
    
    public void setDef(final String def) {
        this.def = def;
    }
    
    public String getIsNull() {
        return this.isNull;
    }
    
    public void setIsNull(final String isNull) {
        this.isNull = isNull;
    }
    
    public String getIsAuto() {
        return this.isAuto;
    }
    
    public void setIsAuto(final String isAuto) {
        this.isAuto = isAuto;
    }
    
    public String getRemark() {
        return this.remark;
    }
    
    public void setRemark(final String remark) {
        this.remark = remark;
    }
    
    public String getSize() {
        return this.size;
    }
    
    public void setSize(final String size) {
        this.size = size;
    }
    
    public Row() {
    }
    
    public Row(final String name, final String type, final String def, final String isNull, final String isAuto, final String remark, final String isPK, final String size) {
        this.name = name;
        this.type = type;
        this.def = def;
        this.isNull = isNull;
        this.isAuto = isAuto;
        this.remark = remark;
        this.isPK = isPK;
        this.size = size;
    }
}
