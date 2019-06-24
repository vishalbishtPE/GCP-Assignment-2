#!/bin/bash
sudo apt-get update  -y
sudo apt install apache2  -y
sudo service apache2 start

sudo rm /var/www/html/index.html
sudo touch /var/www/html/index.html

echo "<html>" >> /var/www/html/index.html
echo "<head>" >> /var/www/html/index.html
echo "<title>" >> /var/www/html/index.html
echo "My Page" >> /var/www/html/index.html
echo "</title>" >> /var/www/html/index.html
echo "</head>" >> /var/www/html/index.html
echo "<body>" >> /var/www/html/index.html
echo "<h1>" >> /var/www/html/index.html
echo "Vishal Bisht" >> /var/www/html/index.html
echo "</h1>" >> /var/www/html/index.html
echo "</body>" >> /var/www/html/index.html
echo "</html>" >> /var/www/html/index.html

