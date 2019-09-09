import static_data
import datetime
import random

def generate_reports(num):

	for current_num in range(num):
		
		# Generate the right filenam eof the correct length
		file_name = str(current_num + 1).zfill(3) + '_report.txt'
		
		# Create the file in write mode
		f = open(file_name, 'w')

		# Generate all of the text content of our dummy report files
		date = str(datetime.date(2019,1,1) + datetime.timedelta(random.randint(1, 365)))
		
		random.shuffle(static_data.names)
		employee = static_data.names[0]

		random.shuffle(static_data.ongoing_tasks)
		ongoing_task_1, ongoing_task_2 = static_data.ongoing_tasks[0:2]
		ongoing_tasks = f'\t{ongoing_task_1}\n\t{ongoing_task_2}\n'

		random.shuffle(static_data.completed_tasks)
		completed_task_1, completed_task_2 = static_data.completed_tasks[0:2]
		completed_tasks = f'\t{completed_task_1}\n\t{completed_task_2}\n'

		random.shuffle(static_data.problems)
		problem_1, problem_2 = static_data.problems[0:2]
		problems = f'\t{problem_1}\n\t{problem_2}\n'

		approved_by = static_data.names[1]
		
		# Fully construct content of dummy report file
		report_content = 'MARIO OFFICE REPORT\n\n' + \
						 'Date: ' 				+ date + '\n\n' + \
						 'Employee: ' 			+ employee + '\n\n' + \
						 'Ongoing Tasks:\n' 	+ ongoing_tasks + '\n' + \
						 'Completed Tasks:\n' 	+ completed_tasks + '\n' + \
						 'Problems:\n' 			+ problems + '\n' + \
						 'Approved By:\n' 		+ approved_by
						 
		# Write content to the line
		f.write(report_content)


generate_reports(10)