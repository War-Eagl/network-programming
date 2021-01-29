#This code creates and writes HTML file 

f = open('red_index.html','wb')

webpage = '''
<html>
<head> HTTP server creation DCN </head>
<body style="background-color=red">
<center><h1> This page is fetched by the TCP_server program </h1>!</center>

<marquee behaviour = "slide"> Hello all... </marquee>

</body>
</html>
'''
f.write(webpage)
f.close()