#killing a process
exec { 'pkill':
command  => pkill -f 'killmenow',
provider => 'shell',
}
