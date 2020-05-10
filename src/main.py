import argparse
import sys
import configparser

def help(show=False):
	parser = argparse.ArgumentParser(description="")
	configs = parser.add_argument_group('System settings', 'The system parameters to run the system in the different modes')
	configs.add_argument('-s', '--settings', dest='settings', \
                        type=str, default="settings.ini", \
                        help='The system settings file (default: settings.ini)')	
	configs.add_argument('-a', '--achilles', dest='achilles', type=str, default='',\
                        help='Achiles results CSV file. If the user prefer to extract the information from the achilles_results.csv file. \
                        (Some parameters must be defined in the seetings file)')	

	executionMode = parser.add_argument_group('Execution Mode', 'Chooe what is the execution mode!')
	executionMode.add_argument('-db', '--database', default=False, action='store_true', \
							help='In this mode, the system will extract the information directly from the database (default: False)')
	executionMode.add_argument('-f', '--file', default=False, action='store_true', \
							help='In this mode, the system will extract the information from an achilles_results.csv (default: False)')

	if show:
		parser.print_help()
	return parser.parse_args()

def readSettings(settingsFile):
	configuration = configparser.ConfigParser()
	configuration.read(settingsFile)
	if not configuration:
		raise Exception("The settings file was not found!")
	return configuration._sections

def validateSettings(settings, args):
	if args.database:
		if "datatype" not in settings["database"] or \
		   "server" not in settings["database"] or \
		   "database" not in settings["database"] or \
		   "schema" not in settings["database"] or \
		   "port" not in settings["database"] or \
		   "user" not in settings["database"] or \
		   "password" not in settings["database"]:
			return False
	elif args.file:
		if "sep" not in settings["achilles_results"]:
			return False
	else:
		return False
	if "analysis_id" not in settings["general"]:
		return False
	return True

def main():
	args = help()
	settings = readSettings(args.settings)
	if validateSettings(settings, args):
		if args.database:
			pass
		elif args.file:
			pass
	else:
		print("The settings.ini is not correct. Please confirm all the necessary parameters in the documentation!")
		help(show=True)
		exit()

main()