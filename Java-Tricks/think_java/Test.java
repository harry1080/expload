// 
// Decompiled by Procyon v0.5.36
// 

package cn.abc.core.controller;

import io.swagger.annotations.ApiOperation;
import cn.abc.common.security.annotation.Access;
import org.springframework.web.bind.annotation.PostMapping;
import java.io.IOException;
import cn.abc.core.sqldict.Table;
import java.util.List;
import cn.abc.common.bean.ResponseCode;
import cn.abc.core.sqldict.SqlDict;
import cn.abc.common.bean.ResponseResult;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.CrossOrigin;

@CrossOrigin
@RestController
@RequestMapping({ "/common/test" })
public class Test
{
    @PostMapping({ "/sqlDict" })
    @Access
    @ApiOperation("\u4e3a\u4e86\u5f00\u53d1\u65b9\u4fbf\u5bf9\u5e94\u6570\u636e\u5e93\u5b57\u5178\u67e5\u8be2")
    public ResponseResult sqlDict(final String dbName) throws IOException {
        final List<Table> tables = (List<Table>)SqlDict.getTableData(dbName, "root", "abc@12345");
        return ResponseResult.e(ResponseCode.OK, (Object)tables);
    }
}
