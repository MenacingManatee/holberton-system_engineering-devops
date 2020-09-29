# Uses exec to run sed to fix phpp typo
file { '/var/www/html/wp-settings.php' :
  ensure => present,
}
exec { 'find and replace phpp' :
  command    => 'cat /var/www/html/wp-settings.php | sed \'s/phpp/php/g\' | sudo tee /var/www/html/wp-settings.php',
  provider   => 'shell',
}