# creates a custom HTTP header response
exec { '/usr/bin/env apt-get -y update':
}
-> package { 'nginx':
  ensure => installed,
}
file {'/var/www/html/index.nginx-debian.html':
  ensure  => present,
  content => 'Holberton School',
}
file_line { 'add_header':
  ensure => present,
  path   => '/etc/nginx/sites-available/default',
  line   => "\tadd_header X-Served-By ${hostname};\n",
  after  => 'server_name _;',
  notify => Service['nginx'],
}
service { 'nginx':
  ensure => running,
}
