# config file

include stdlib

file_line { 'Turn off Password Auth':
  path               => '/etc/ssh/ssh_config',
  line               => 'PasswordAuthentication no',
  match              => '^[#]+[\s]*(?i)PasswordAuthentication[\s]+(yes|no)$',
  replace            => true,
  append_on_no_match => true
}

file_line { 'Declare Identity file':
  path               => '/etc/ssh/ssh_config',
  line               => 'IdentityFile ~/.ssh/school',
  match              => '^[#]+[\s]*(?i)IdentityFile[\s]+~/.ssh/id_rsa$',
  replace            => true,
  append_on_no_match => true
}
