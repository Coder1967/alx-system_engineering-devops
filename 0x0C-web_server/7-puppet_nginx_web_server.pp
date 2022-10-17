#installs nginx on server
package {'nginx':
name     => 'nginx',
provider => 'apt',
ensure   => 'latest',
}

file {'/var/www/html/index.nginx-debian.html':
content => "Hello World!",
ensure  => 'present',
}

exec {'redirect':
provider => 'shell',
command  => 'sudo sed -i "s/server_name _;/server_name _;\n\trewrite ^\/redirect_me https:\/\/github.com\/Tolulope05 permanent;/" /etc/nginx/sites-available/default ; sudo service nginx start',
}
