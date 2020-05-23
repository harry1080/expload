// 
// Decompiled by Procyon v0.5.36
// 

package cn.abc.servlet;

import javax.servlet.ServletOutputStream;
import java.io.FileInputStream;
import java.net.URLEncoder;
import java.io.File;
import javax.servlet.ServletResponse;
import javax.servlet.ServletRequest;
import java.io.IOException;
import javax.servlet.ServletException;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServlet;

public class DownloadServlet extends HttpServlet
{
    private static final long serialVersionUID = 1L;
    
    protected void doGet(final HttpServletRequest request, final HttpServletResponse response) throws ServletException, IOException {
        this.doPost(request, response);
    }
    
    protected void doPost(final HttpServletRequest request, final HttpServletResponse response) throws ServletException, IOException {
        String fileName = request.getParameter("filename");
        fileName = new String(fileName.getBytes("ISO8859-1"), "UTF-8");
        System.out.println("filename=" + fileName);
        if (fileName != null && fileName.toLowerCase().contains("flag")) {
            request.setAttribute("message", (Object)"\u7981\u6b62\u8bfb\u53d6");
            request.getRequestDispatcher("/message.jsp").forward((ServletRequest)request, (ServletResponse)response);
            return;
        }
        final String fileSaveRootPath = this.getServletContext().getRealPath("/WEB-INF/upload");
        final String path = this.findFileSavePathByFileName(fileName, fileSaveRootPath);
        final File file = new File(path + "/" + fileName);
        if (!file.exists()) {
            request.setAttribute("message", (Object)"\u60a8\u8981\u4e0b\u8f7d\u7684\u8d44\u6e90\u5df2\u88ab\u5220\u9664!");
            request.getRequestDispatcher("/message.jsp").forward((ServletRequest)request, (ServletResponse)response);
            return;
        }
        final String realname = fileName.substring(fileName.indexOf("_") + 1);
        response.setHeader("content-disposition", "attachment;filename=" + URLEncoder.encode(realname, "UTF-8"));
        final FileInputStream in = new FileInputStream(path + "/" + fileName);
        final ServletOutputStream out = response.getOutputStream();
        final byte[] buffer = new byte[1024];
        int len = 0;
        while ((len = in.read(buffer)) > 0) {
            out.write(buffer, 0, len);
        }
        in.close();
        out.close();
    }
    
    public String findFileSavePathByFileName(final String filename, final String saveRootPath) {
        final int hashCode = filename.hashCode();
        final int dir1 = hashCode & 0xF;
        final int dir2 = (hashCode & 0xF0) >> 4;
        final String dir3 = saveRootPath + "/" + dir1 + "/" + dir2;
        final File file = new File(dir3);
        if (!file.exists()) {
            file.mkdirs();
        }
        return dir3;
    }
}
