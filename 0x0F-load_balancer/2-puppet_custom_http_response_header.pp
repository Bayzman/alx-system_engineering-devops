# Setup New Ubuntu server with nginx
# and add a custom HTTP header

exec { 'http header':
  command  => 'sudo apt-get update';
  sudo apt-get install -y nginx;
  sudo sed -i "/server_name _/a add_header X-Served-By ${HOSTNAME};" /etc/nginx/sites-available/default
  sudo service nginx restart,
  provider => shell,
}
