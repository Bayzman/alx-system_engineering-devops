#!/usr/bin/env ruby
# Regular expression to match only upper case letters

puts ARGV[0].scan(/[A-Z]*/).join
