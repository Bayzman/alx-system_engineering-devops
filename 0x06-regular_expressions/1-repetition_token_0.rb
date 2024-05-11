#!/usr/bin/env ruby
# Regular expression to match htbn with t
# ranging from 2 to 5 strings in a text

puts ARGV[0].scan(/hbt{2,5}n/)
