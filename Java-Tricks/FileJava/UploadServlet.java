// 
// Decompiled by Procyon v0.5.36
// 

package cn.abc.servlet;

import java.util.UUID;
import org.apache.poi.ss.usermodel.Sheet;
import org.apache.poi.ss.usermodel.Workbook;
import java.io.InputStream;
import java.util.Iterator;
import java.util.List;
import javax.servlet.ServletResponse;
import javax.servlet.ServletRequest;
import org.apache.commons.fileupload.FileUploadException;
import java.io.FileOutputStream;
import org.apache.poi.openxml4j.exceptions.InvalidFormatException;
import org.apache.poi.ss.usermodel.WorkbookFactory;
import org.apache.commons.fileupload.FileItem;
import org.apache.commons.fileupload.ProgressListener;
import org.apache.commons.fileupload.FileItemFactory;
import org.apache.commons.fileupload.servlet.ServletFileUpload;
import org.apache.commons.fileupload.disk.DiskFileItemFactory;
import java.io.File;
import java.io.IOException;
import javax.servlet.ServletException;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServlet;

public class UploadServlet extends HttpServlet
{
    private static final long serialVersionUID = 1L;
    
    protected void doGet(final HttpServletRequest request, final HttpServletResponse response) throws ServletException, IOException {
        this.doPost(request, response);
    }
    
    protected void doPost(final HttpServletRequest request, final HttpServletResponse response) throws ServletException, IOException {
        final String savePath = this.getServletContext().getRealPath("/WEB-INF/upload");
        final String tempPath = this.getServletContext().getRealPath("/WEB-INF/temp");
        final File tempFile = new File(tempPath);
        if (!tempFile.exists()) {
            tempFile.mkdir();
        }
        String message = "";
        try {
            final DiskFileItemFactory factory = new DiskFileItemFactory();
            factory.setSizeThreshold(102400);
            factory.setRepository(tempFile);
            final ServletFileUpload upload = new ServletFileUpload((FileItemFactory)factory);
            upload.setProgressListener((ProgressListener)new UploadServlet.UploadServlet$1(this));
            upload.setHeaderEncoding("UTF-8");
            upload.setFileSizeMax(1048576L);
            upload.setSizeMax(10485760L);
            if (!ServletFileUpload.isMultipartContent(request)) {
                return;
            }
            final List<FileItem> list = (List<FileItem>)upload.parseRequest(request);
            for (final FileItem fileItem : list) {
                if (fileItem.isFormField()) {
                    final String name = fileItem.getFieldName();
                    fileItem.getString("UTF-8");
                }
                else {
                    final String filename = fileItem.getName();
                    if (filename == null) {
                        continue;
                    }
                    if (filename.trim().equals("")) {
                        continue;
                    }
                    final String fileExtName = filename.substring(filename.lastIndexOf(".") + 1);
                    final InputStream in = fileItem.getInputStream();
                    if (filename.startsWith("excel-") && "xlsx".equals(fileExtName)) {
                        try {
                            final Workbook wb1 = WorkbookFactory.create(in);
                            final Sheet sheet = wb1.getSheetAt(0);
                            System.out.println(sheet.getFirstRowNum());
                        }
                        catch (InvalidFormatException e) {
                            System.err.println("poi-ooxml-3.10 has something wrong");
                            e.printStackTrace();
                        }
                    }
                    final String saveFilename = this.makeFileName(filename);
                    request.setAttribute("saveFilename", (Object)saveFilename);
                    request.setAttribute("filename", (Object)filename);
                    final String realSavePath = this.makePath(saveFilename, savePath);
                    final FileOutputStream out = new FileOutputStream(realSavePath + "/" + saveFilename);
                    final byte[] buffer = new byte[1024];
                    int len = 0;
                    while ((len = in.read(buffer)) > 0) {
                        out.write(buffer, 0, len);
                    }
                    in.close();
                    out.close();
                    message = "\u6587\u4ef6\u4e0a\u4f20\u6210\u529f!";
                }
            }
        }
        catch (FileUploadException e2) {
            e2.printStackTrace();
        }
        request.setAttribute("message", (Object)message);
        request.getRequestDispatcher("/ListFileServlet").forward((ServletRequest)request, (ServletResponse)response);
    }
    
    private String makeFileName(final String filename) {
        return UUID.randomUUID().toString() + "_" + filename;
    }
    
    private String makePath(final String filename, final String savePath) {
        final int hashCode = filename.hashCode();
        final int dir1 = hashCode & 0xF;
        final int dir2 = (hashCode & 0xF0) >> 4;
        final String dir3 = savePath + "/" + dir1 + "/" + dir2;
        final File file = new File(dir3);
        if (!file.exists()) {
            file.mkdirs();
        }
        return dir3;
    }
}
