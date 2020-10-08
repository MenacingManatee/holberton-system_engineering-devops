# uses exec to run sed to set worker processes to max
file { '/etc/nginx/nginx.conf' :
  ensure => present,
}
exec { 'update worker_processes' :
  command  => 'cat /etc/nginx/nginx.conf | sed \'s/worker_processes 4/worker_processes 1024/g\' | sudo tee /etc/nginx/nginx.conf ; service nginx restart',
  provider => 'shell',
}
