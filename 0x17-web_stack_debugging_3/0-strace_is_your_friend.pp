# Used strace to find out why Apache is returning a 500 error and automating the fix with puppet

exec {'replace':
  provider => shell,
  command  => 'sed -i "s/phpp/php/g" /var/www/html/wp-settings.php'
}
