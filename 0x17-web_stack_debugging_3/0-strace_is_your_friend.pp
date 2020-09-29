class line::conf {
  file { $line::/var/www/html/wp-settings/var/www/html/wp-settings :
    ensure => present,
    } ->
  file_line { 'replace':
    path    => $line::/var/www/html/wp-settings,
    replace => true,
    line    => $line::require_once( ABSPATH . WPINC . '/class-wp-locale.php' );
    match   => $line::require_once( ABSPATH . WPINC . '/class-wp-locale.phpp' );
  }
}