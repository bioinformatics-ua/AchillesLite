# AchillesLite
AchillesLite is a python tool to extract relevant information from Achilles output that will be used in the EHDEN Network Dashboards. This tool can read the Achilles results directly from the CSV file or the database.

### Setup
The tool can be executed using docker. Therefore, execute the following command to start the application:

```bash
sh run.sh 
```

or 

```bash
docker-compose up -d && docker exec -it achilleslite_src_1 bash && docker-compose down
```

This will build the image and start the container with all the dependencies installed. Then, it will open a console where it is possible to execute the tool. To exit, just type exit and the docker will be stoped.

### Execution mode

The tool was designed to have two modes of execution: 
-  Extracting the data directly from the database. It requires all the parameters defined in the "database" section of the settings file. Command:
   ```bash
   python main.py -db
   ```
- Extracting the data from an achilles_results.csv file. This requires the parameters defined in "achilles_results" section of the settings file. It also requires the input file which is defined in the python command. Command:
   ```bash
   python main.py -f -a <file>
   ```
  
To see the help, just type:
   ```bash
   $ python main.py -h
usage: main.py [-h] [-s SETTINGS] [-a ACHILLES] [-db] [-f]

optional arguments:
  -h, --help            show this help message and exit

System settings:
  The system parameters to run the system in the different modes

  -s SETTINGS, --settings SETTINGS
                        The system settings file (default: settings.ini)
  -a ACHILLES, --achilles ACHILLES
                        Achilles results CSV file. If the user prefers to
                        extract the information from the achilles_results.csv
                        file. (Some parameters must be defined in the settings
                        file)

Execution Mode:
  Choose what is the execution mode!

  -db, --database       In this mode, the system will extract the information
                        directly from the database (default: False)
  -f, --file            In this mode, the system will extract the information
                        from an achilles_results.csv (default: False)

   ```


### Settings
The settings file has the following structure:
```ini
[database]
datatype=
server=
database=
schema=
port=
user=
password=

[achilles_results]
sep=

[general]
analysis_id=../analysisIDS.csv
export_location=../achilles_results.csv
```

