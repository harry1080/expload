#!/usr/bin/env python
# coding: utf-8
# Rewrite by hosch3n in 2020-04-10
# Origin by Macr0phag3 in 2019-05-07

import sys

# 删掉 this, antigravity 库

# Python2标准库模块
modules2 = [
    'BaseHTTPServer', 'imaplib', 'shelve', 'Bastion', 'anydbm', 'imghdr', 'shlex', 'CDROM', 'argparse', 'imp', 'shutil', 'CGIHTTPServer', 'array', 'importlib', 'signal', 'Canvas', 'ast', 'imputil', 'site', 'ConfigParser', 'asynchat', 'inspect', 'sitecustomize', 'Cookie', 'asyncore', 'io', 'smtpd', 'DLFCN', 'atexit', 'itertools', 'smtplib', 'Dialog', 'audiodev', 'json', 'sndhdr', 'DocXMLRPCServer', 'audioop', 'keyword', 'socket', 'FileDialog', 'base64', 'lib2to3', 'spwd', 'FixTk', 'bdb', 'linecache', 'sqlite3', 'HTMLParser', 'binascii', 'linuxaudiodev', 'sre', 'IN', 'binhex', 'locale', 'sre_compile', 'MimeWriter', 'bisect', 'logging', 'sre_constants', 'Queue', 'bsddb', 'lsb_release', 'sre_parse', 'ScrolledText', 'bz2', 'macpath', 'ssl', 'SimpleDialog', 'cPickle', 'macurl2path', 'stat', 'SimpleHTTPServer', 'cProfile', 'mailbox', 'statvfs', 'SimpleXMLRPCServer', 'cStringIO', 'mailcap', 'string', 'SocketServer', 'calendar', 'markupbase', 'stringold', 'StringIO', 'cgi', 'marshal', 'stringprep', 'TYPES', 'cgitb', 'math', 'strop', 'Tix', 'chunk', 'md5', 'struct', 'Tkconstants', 'cmath', 'mhlib', 'subprocess', 'Tkdnd', 'cmd', 'mimetools', 'sunau', 'Tkinter', 'code', 'mimetypes', 'sunaudio', 'UserDict', 'codecs', 'mimify', 'symbol', 'UserList', 'codeop', 'mmap', 'symtable', 'UserString', 'collections', 'modulefinder', 'sys', '_LWPCookieJar', 'colorsys', 'multifile', 'sysconfig', '_MozillaCookieJar', 'commands', 'multiprocessing', 'syslog', '__builtin__', 'compileall', 'mutex', 'tabnanny', '__future__', 'compiler', 'netrc', 'talloc', '_abcoll', 'contextlib', 'new', 'tarfile', '_ast', 'cookielib', 'nis', 'telnetlib', '_bisect', 'copy', 'nntplib', 'tempfile', '_bsddb', 'copy_reg', 'ntpath', 'termios', '_codecs', 'crypt', 'nturl2path', 'test', '_codecs_cn', 'csv', 'numbers', 'textwrap', '_codecs_hk', 'ctypes', 'opcode', '_codecs_iso2022', 'curses', 'operator', 'thread', '_codecs_jp', 'datetime', 'optparse', 'threading', '_codecs_kr', 'dbhash', 'os', 'time', '_codecs_tw', 'dbm', 'os2emxpath', 'timeit', '_collections', 'decimal', 'ossaudiodev', 'tkColorChooser', '_csv', 'difflib', 'parser', 'tkCommonDialog', '_ctypes', 'dircache', 'pdb', 'tkFileDialog', '_ctypes_test', 'dis', 'pickle', 'tkFont', '_curses', 'distutils', 'pickletools', 'tkMessageBox', '_curses_panel', 'doctest', 'pipes', 'tkSimpleDialog', '_elementtree', 'dumbdbm', 'pkgutil', 'toaiff', '_functools', 'dummy_thread', 'platform', 'token', '_hashlib', 'dummy_threading', 'plistlib', 'tokenize', '_heapq', 'email', 'popen2', 'trace', '_hotshot', 'encodings', 'poplib', 'traceback', '_io', 'ensurepip', 'posix', 'ttk', '_json', 'errno', 'posixfile', 'tty', '_locale', 'exceptions', 'posixpath', 'turtle', '_lsprof', 'fcntl', 'pprint', 'types', '_md5', 'filecmp', 'profile', 'unicodedata', '_multibytecodec', 'fileinput', 'pstats', 'unittest', '_multiprocessing', 'fnmatch', 'pty', 'urllib', '_osx_support', 'formatter', 'pwd', 'urllib2', '_pyio', 'fpformat', 'py_compile', 'urlparse', '_random', 'fractions', 'pyclbr', 'user', '_sha', 'ftplib', 'pydoc', 'uu', '_sha256', 'functools', 'pydoc_data', 'uuid', '_sha512', 'future_builtins', 'pyexpat', 'warnings', '_socket', 'gc', 'quopri', 'wave', '_sqlite3', 'genericpath', 'random', 'weakref', '_sre', 'getopt', 're', 'webbrowser', '_ssl', 'getpass', 'readline', 'whichdb', '_strptime', 'gettext', 'repr', 'wsgiref', '_struct', 'glob', 'resource', 'xdrlib', '_symtable', 'grp', 'rexec', 'xml', '_sysconfigdata', 'gzip', 'rfc822', 'xmllib', '_sysconfigdata_nd', 'hashlib', 'rlcompleter', 'xmlrpclib', '_testcapi', 'heapq', 'robotparser', 'xxsubtype', '_threading_local', 'hmac', 'runpy', 'zipfile', '_warnings', 'hotshot', 'sched', 'zipimport', '_weakref', 'htmlentitydefs', 'select', 'zlib', '_weakrefset', 'htmllib', 'sets', 'abc', 'httplib', 'sgmllib', 'aifc', 'ihooks', 'sha'
]

# Python3标准库模块
modules3 = [
    'AptUrl', 'hmac', 'requests_unixsocket', 'CommandNotFound', 'apport', 'hpmudext', 'resource', 'Crypto', 'apport_python_hook', 'html', 'rlcompleter', 'DistUpgrade', 'apt', 'http', 'runpy', 'HweSupportStatus', 'apt_inst', 'httplib2', 'scanext', 'LanguageSelector', 'apt_pkg', 'idna', 'sched', 'NvidiaDetector', 'aptdaemon', 'imaplib', 'secrets', 'PIL', 'aptsources', 'imghdr', 'secretstorage', 'Quirks', 'argparse', 'imp', 'select', 'UbuntuDrivers', 'array', 'importlib', 'selectors', 'UbuntuSystemService', 'asn1crypto', 'inspect', 'shelve', 'UpdateManager', 'ast', 'io', 'shlex', '__future__', 'asynchat', 'ipaddress', 'shutil', '_ast', 'asyncio', 'itertools', 'signal', '_asyncio', 'asyncore', 'janitor', 'simplejson', '_bisect', 'atexit', 'json', 'site', '_blake2', 'audioop', 'keyring', 'sitecustomize', '_bootlocale', 'base64', 'keyword', 'six', '_bz2', 'bdb', 'language_support_pkgs', 'smtpd', '_cffi_backend', 'binascii', 'launchpadlib', 'smtplib', '_codecs', 'binhex', 'linecache', 'sndhdr', '_codecs_cn', 'bisect', 'locale', 'socket', '_codecs_hk', 'brlapi', 'logging', 'socketserver', '_codecs_iso2022', 'builtins', 'louis', 'softwareproperties', '_codecs_jp', 'bz2', 'lsb_release', 'speechd', '_codecs_kr', 'cProfile', 'lzma', 'speechd_config', '_codecs_tw', 'cairo', 'macaroonbakery', 'spwd', '_collections', 'calendar', 'macpath', 'sqlite3', '_collections_abc', 'certifi', 'macurl2path', 'sre_compile', '_compat_pickle', 'cgi', 'mailbox', 'sre_constants', '_compression', 'cgitb', 'mailcap', 'sre_parse', '_crypt', 'chardet', 'mako', 'ssl', '_csv', 'chunk', 'markupsafe', 'stat', '_ctypes', 'cmath', 'marshal', 'statistics', '_ctypes_test', 'cmd', 'math', 'string', '_curses', 'code', 'mimetypes', 'stringprep', '_curses_panel', 'codecs', 'mmap', 'struct', '_datetime', 'codeop', 'modual_test', 'subprocess', '_dbm', 'collections', 'modulefinder', 'sunau', '_dbus_bindings', 'colorsys', 'multiprocessing', 'symbol', '_dbus_glib_bindings', 'compileall', 'nacl', 'symtable', '_decimal', 'concurrent', 'netrc', 'sys', '_dummy_thread', 'configparser', 'nis', 'sysconfig', '_elementtree', 'contextlib', 'nntplib', 'syslog', '_functools', 'copy', 'ntpath', 'systemd', '_gdbm', 'copyreg', 'nturl2path', 'tabnanny', '_hashlib', 'crypt', 'numbers', 'tarfile', '_heapq', 'cryptography', 'oauth', 'telnetlib', '_imp', 'csv', 'olefile', 'tempfile', '_io', 'ctypes', 'opcode', 'termios', '_json', 'cups', 'operator', 'test', '_locale', 'cupsext', 'optparse', 'textwrap', '_lsprof', 'cupshelpers', 'orca', '_lzma', 'curses', 'os', 'threading', '_markupbase', 'datetime', 'ossaudiodev', 'time', '_md5', 'dbm', 'parser', 'timeit', '_multibytecodec', 'dbus', 'pathlib', 'token', '_multiprocessing', 'deb822', 'pcardext', 'tokenize', '_opcode', 'debconf', 'pdb', 'trace', '_operator', 'debian', 'pexpect', 'traceback', '_osx_support', 'debian_bundle', 'pickle', 'tracemalloc', '_pickle', 'decimal', 'pickletools', 'tty', '_posixsubprocess', 'defer', 'pipes', 'turtle', '_pydecimal', 'difflib', 'pkg_resources', 'types', '_pyio', 'dis', 'pkgutil', 'typing', '_random', 'distro_info', 'platform', 'ufw', '_sha1', 'distro_info_test', 'plistlib', 'unicodedata', '_sha256', 'distutils', 'poplib', 'unittest', '_sha3', 'doctest', 'posix', 'urllib', '_sha512', 'dummy_threading', 'posixpath', 'urllib3', '_signal', 'email', 'pprint', 'usbcreator', '_sitebuiltins', 'encodings', 'problem_report', 'uu', '_socket', 'enum', 'profile', 'uuid', '_sqlite3', 'errno', 'pstats', 'venv', '_sre', 'faulthandler', 'pty', 'wadllib', '_ssl', 'fcntl', 'ptyprocess', 'warnings', '_stat', 'filecmp', 'pwd', 'wave', '_string', 'fileinput', 'py_compile', 'weakref', '_strptime', 'fnmatch', 'pyatspi', 'webbrowser', '_struct', 'formatter', 'pyclbr', 'wsgiref', '_symtable', 'fractions', 'pydoc', 'xdg', '_sysconfigdata_m_linux_x86_64-linux-gnu', 'ftplib', 'pydoc_data', 'xdrlib', '_testbuffer', 'functools', 'pyexpat', 'xkit', '_testcapi', 'gc', 'pygtkcompat', 'xml', '_testimportmultiple', 'genericpath', 'pymacaroons', 'xmlrpc', '_testmultiphase', 'getopt', 'pyrfc3339', 'xxlimited', '_thread', 'getpass', 'pytz', 'xxsubtype', '_threading_local', 'gettext', 'queue', 'yaml', '_tracemalloc', 'gi', 'quopri', 'zipapp', '_warnings', 'glob', 'random', 'zipfile', '_weakref', 'grp', 're', 'zipimport', '_weakrefset', 'gtweak', 'readline', 'zlib', '_yaml', 'gzip', 'reportlab', 'zope', 'abc', 'hashlib', 'reprlib', 'aifc', 'heapq'
]

# 危险模块
methods = ['sys', 'os', 'system', 'popen', 'subprocess', 'platform', 'commands', 'timeit', 'importlib', 'pickle', 'pty', '__builtins__', '__import__', 'import_module', 'eval', 'exec', 'spawn', 'file', 'linecache', 'types']

# object的派生类
subclasses = {}

# 危险标准库模块
risk_modules = {}

# 遍历派生类并获取模块
for i in range(0, len(object.__subclasses__())):
    try:
        subclasses[i] = object.__subclasses__()[i].__init__.__globals__.keys()
    except Exception as e:
        #print(e)
        pass

print('------------------------------ 思路二 ------------------------------')

# 导入了危险模块的派生类
for i, submodules in subclasses.items():
    for submodule in submodules:
        for method in methods:
            if method == submodule:
                #print(f"object.__subclasses__()[{i}].__init__.__globals__['{method}']")
                print("object.__subclasses__()[{i}].__init__.__globals__['{method}']".format(i=i, method=method))

print('------------------------------ 缓冲区 ------------------------------')

# 判断Python版本
if sys.version_info[0] == 3:
    modules = modules3
else:
    modules = modules2

# 导入了危险模块的标准库
for module in modules:
    risk_modules[module] = []
    try:
        m = __import__(module)  # 导入模块
        attrs = dir(m)          # 获取属性与方法
        for method in methods:
            if method in attrs: # 若存在危险模块
                risk_modules[module].append(method)
    except Exception as e:
        #print(e)
        pass

print('------------------------------ 思路三 ------------------------------')

# 导入了危险标准库的派生类
for i, submodules in subclasses.items():
    for submodule in submodules:
        for risk_module in risk_modules.keys():
            if risk_module == submodule:
                for method in risk_modules[risk_module]:
                    #print(f"object.__subclasses__()[{i}].__init__.__globals__['{risk_module}'].__dict__['{method}']")
                    print("object.__subclasses__()[{i}].__init__.__globals__['{risk_module}'].__dict__['{method}']".format(i=i, risk_module=risk_module, method=method))