// 
// Decompiled by Procyon v0.5.36
// 

package cn.abc.servlet;

import java.util.Map;
import javax.servlet.ServletResponse;
import javax.servlet.ServletRequest;
import java.util.HashMap;
import java.io.IOException;
import javax.servlet.ServletException;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServlet;

public class ListFileServlet extends HttpServlet
{
    private static final long serialVersionUID = 1L;
    
    protected void doGet(final HttpServletRequest request, final HttpServletResponse response) throws ServletException, IOException {
        this.doPost(request, response);
    }
    
    protected void doPost(final HttpServletRequest request, final HttpServletResponse response) throws ServletException, IOException {
        final String uploadFilePath = this.getServletContext().getRealPath("/WEB-INF/upload");
        final Map<String, String> fileNameMap = new HashMap<String, String>();
        final String saveFilename = (String)request.getAttribute("saveFilename");
        final String filename = (String)request.getAttribute("filename");
        System.out.println("saveFilename" + saveFilename);
        System.out.println("filename" + filename);
        final String realName = saveFilename.substring(saveFilename.indexOf("_") + 1);
        fileNameMap.put(saveFilename, filename);
        request.setAttribute("fileNameMap", (Object)fileNameMap);
        request.getRequestDispatcher("/listfile.jsp").forward((ServletRequest)request, (ServletResponse)response);
    }
}
