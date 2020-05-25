<!DOCTYPE html>
<html>
<head>
  <title>phpweb</title>
  <style type="text/css">
		body {
			background:url("bg.jpg") no-repeat;
			background-size: 100%;
      }
    p {
      color: white;
    }
	</style>
</head>
<body>
  <script language=javascript>
    setTimeout("document.form1.submit()",5000)
  </script>
  <p>
  <?php
    $disable_fun = array("exec","shell_exec","system","passthru","proc_open","show_source","phpinfo","popen","dl","eval","proc_terminate","touch",
      "escapeshellcmd","escapeshellarg","assert","substr_replace","call_user_func_array","call_user_func","array_filter", "array_walk",
      "array_map","registregister_shutdown_function","register_tick_function","filter_var", "filter_var_array", "uasort", "uksort", "array_reduce",
      "array_walk", "array_walk_recursive","pcntl_exec","fopen","fwrite","file_put_contents"
    );
    function gettime($func, $p) {
      $result = call_user_func($func, $p);
      $a= gettype($result);
      if ($a == "string") {
        return $result;
      } else {
        return "";
      }
    }
    class Test {
      var $p = "Y-m-d h:i:s a";
      var $func = "date";
      function __destruct() {
        if ($this->func != "") {
          echo gettime($this->func, $this->p);
        }
      }
    }
    $func = $_REQUEST["func"];
    $p = $_REQUEST["p"];
    if ($func != null) {
      $func = strtolower($func);
      if (!in_array($func,$disable_fun)) {
        echo gettime($func, $p);
      }else {
        die("Hacker...");
      }
    }
  ?>
  </p>
  <form id=form1 name=form1 action="index.php" method="post">
    <input type="hidden" id="func" name="func" value='date'>
    <input type="hidden" id="p" name="p" value='Y-m-d h:i:s a'>
  </form>
</body>
</html>