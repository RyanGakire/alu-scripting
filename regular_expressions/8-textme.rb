#!/usr/bin/env ruby

lines = ARGV.empty? ? STDIN : ARGV

lines.each do |line|
  match = line.match(/\[from:([^\]]+)\].*\[to:([^\]]+)\].*\[flags:([^\]]+)\]/)
  next unless match

  puts "#{match[1]},#{match[2]},#{match[3]}"
end
