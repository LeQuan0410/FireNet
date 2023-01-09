# FireNet-Beta
<h3>main.py</h3>
<b>main.py is a layer7 and layer4 attack, it uses proxies so you dont need a VPS but this slows the speed and power alot.<b>
<p></p>
<h3>raw.py</h3>
<b>raw.py is main.py without proxies, it hits pretty hard and on a doodoo vps i got like 120mb/s so on a good one u can expect GB/s power.<b>
<p></p>
<h3>sock.py</h3>
<b>sock.py is a layer4 socket attack, also known as CPU eater and it ramps up servers and hits hard. On a doodoo vps i got 90mb/s+</b>
<p></p>

<h2>extra</h2>
<b>post.py is raw.py but uses post attack instead of get</b>
<p></p>

#More
<b>raw.py and main.py both do something special, besides the fact they send get requests the server also sends back alot (On doodoo vps i got 150mb/s being sent out) meaning it eats all the in and out power of the target.</b>

#Use case and requirements
<b>To use post.py, main.py or raw.py on layer 4 the IP must accept HTTP requests, and example would be an nginx proxy. On layer7 it does not hit many requests but hits the backend which isnt visible on dstat.</b>

urllib3 is required to run [pip install urllib3]


NOTE: This is for educational purposes only! this software was made for education and to inform the public, i do not condone the use of this product for illegal or immoral purposes.
