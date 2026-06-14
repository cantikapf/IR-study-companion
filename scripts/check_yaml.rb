require 'yaml'

Dir.glob('d:/PERSONAL PROJECT/IR-study-companion/_chapters/**/*.md').each do |file|
  text = File.read(file)
  parts = text.split('---', 3)
  next if parts.length < 3
  frontmatter = parts[1]
  begin
    YAML.safe_load(frontmatter)
  rescue => e
    puts "Error in #{file}: #{e.message}"
  end
end
puts 'Done checking YAML.'
