exec { 'pkill':
  command => 'pkill killmenow',
  path	  => '/usr/bin/:/bin/',
}