from selenium import webdriver

driver = webdriver.PhantomJS(executable_path='phantomjs')

input_file = open('input','rb')
output_file = open('output', 'wb')

for line in input_file:
	driver.get(line)
	output_file.write(driver.current_url + '\n')

input_file.close()
output_file.close()
driver.quit()






