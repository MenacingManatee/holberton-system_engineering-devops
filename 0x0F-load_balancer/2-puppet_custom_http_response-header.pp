# creates a custom HTTP header response
exec { '/usr/bin/env apt-get -y update':
}
-> package { 'nginx':
  ensure => installed,
}
file_line { 'add_header':
  ensure => present,
  path   => '/etc/nginx/sites-available/default',
  line   => "\tadd_header X-Served-By ${hostname};\n",
  after  => 'server_name _;',
}
service { 'nginx':
  ensure => running,
}
