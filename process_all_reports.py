import os
import shutil


subdirectory_folder = 'flagged_files'

def process_all_reports():

	os.mkdir(subdirectory_folder)

	for file_name in os.listdir(os.getcwd()):
		if file_name.endswith('_report.txt'):
			os.rename(file_name, file_name.lstrip('0'))
			
			# Search the report file
			criteria = 'I don\'t want to automate with Python'
			criteria_met = search_for_criteria(file_name, criteria)

			# If report file meets criteria
			if criteria_met:
				print(file_name)
				# Process that file	
				process_report(file_name)


def search_for_criteria(file_name, criteria):
	
	f = open(file_name)
	text_of_file = f.read()
	
	if criteria in text_of_file:
		return True
	return False


def process_report(file_name):
	
	f = open(file_name)
	lines = f.readlines()
	
	for line in lines:
		if line.startswith('Employee: '):
			employee_to_report = ' '.join(line.split(' ')[1:]).strip()

		if line.startswith('Approved By: '):
			employee_reporting = ' '.join(line.split(' ')[2:]).strip()

	flagged_report_filename = f'FLAGGED REPORT - {employee_to_report}.txt'
	flagged_report = open(flagged_report_filename, 'w')

	flagged_report.write(f'EMPLOYEES FLAGGED FOR REVIEW. CONSIDER TERMINATION.\n' + \
						employee_to_report.upper() + \
						' DOES NOT WANT TO AUTOMATE WITH PYTHON.\n' + \
						employee_reporting.upper() + \
						' APPROVED THIS.\n' + \
						'COPY OF REPORT HERE:\n\n')

	f = open(file_name)
	flagged_report.write(f.read())
	flagged_report.close()

	os.rename(flagged_report_filename, os.path.join(subdirectory_folder, flagged_report_filename))


def delete_files():
	if os.path.isdir(subdirectory_folder):
		shutil.rmtree(subdirectory_folder)


if __name__ == '__main__':
	delete_files()
	process_all_reports()