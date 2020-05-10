class FileManager():
	def readAnalysisID(analysisIDfile):
		"""
		Reads the analysis ids necessary for the SQL queries in the Network Dashboards
		:param analysisIDfile: file location with the anaylsis ids
		:return: List with the IDs
		"""
		ids = []
		try:
			with open(analysisIDfile) as fp:
				content = fp.readlines()
			ids = [x.strip() for x in content] 
		finally:
			fp.close()
		return ids

	def readAchillesResults(filePath, sep, analysisIDs):
		"""
		Reads the achilles_results csv and filters based on the analysis ids
		:param filePath: The achilles_results location
		:param sep: The column spliter used in the file
		:param analysisIDs: The list of IDs
		:return: Tuple with Header and List with rows that contain the selected analysis IDs
		"""
		data = []
		header = None
		try:
			with open(filePath) as fp:
				content = fp.readlines()
			for line in content:
				row = line.strip().split(sep)
				if "analysis_id" in line:
					header = line
				if row[0] in analysisIDs:
					data.append(line)
		finally:
			fp.close()
		return header, data

	def write(header, data, fileLoc):
		"""
		Writes the CSV containing the filtered achilles results based on the analysis ids
		:param header: Contains the same header used in the original file (Can be None)
		:param data: List with all the lines to write in the file
		:param fileLoc: Location to write the file
		"""
		try:
			fp = open(fileLoc, "w")
			if header:
				fp.write(header)
			for line in data:
				fp.write(line)
		finally:
			fp.close()
