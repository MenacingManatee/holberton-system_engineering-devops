# Kills a process called killmenow
exec { 'pkill killmenow':
  command => 'pkill killmenow',
  path	  => '/usr/bin/:/bin/',
}