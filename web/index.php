<html>
<head>
	<script src='https://code.jquery.com/jquery-3.1.1.js'></script>
</head>
<body>
	<center>
		<div id='div1' style='text-align: left; outline: 2px solid black;'>
		</div>
		<br>
		<br>
		<a id='button' download>Download text file in current state</a>
	</center>
	<script type='text/javascript'>
	dates = new Date()
	month = dates.getMonth() + 1 
	download = 'logs/' + dates.getFullYear() + ':' +  month +  ':' + dates.getDate() + '.txt'
	setInterval(function(){ $.ajax({url: "output.php", success: function(result){
        				$("#div1").html(result);
    			}}); }, 50);

	$("a").attr("href", download)
	</script>
</body>
</html>
