Dir.glob('d:/PERSONAL PROJECT/IR-study-companion/**/*.{html,md,js}').each do |f|
  next if f.include?('_site')
  begin
    content = File.read(f, encoding: 'utf-8')
    if content.include?('✅')
      puts "Found in #{f}"
    end
  rescue
  end
end
