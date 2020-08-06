# Creates and configures a nginx webserver
node '34.73.196.89' {
  package { 'nginx':
    ensure => installed,
  }
}
file { '/var/www/html/index.nginx-debian.html':
  path    => '/var/www/html/index.nginx-debian.html',
  content => 'Holberton School',
  mode    => '0744',
}
