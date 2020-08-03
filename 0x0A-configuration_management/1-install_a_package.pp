# Installs puppet-lint with version 2.1.1 using gem
package { 'puppet-lint':
  ensure   => '2.1.1',
  provider => gem,
}