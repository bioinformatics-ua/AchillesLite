from sqlalchemy import create_engine

class DBManager():
	def query(DBsettings, analysisIDs):
		engine = create_engine(	DBsettings["datatype"]+"://"+
								DBsettings["user"]+":"+
								DBsettings["password"]+"@"+
								DBsettings["server"]+":"+
								DBsettings["port"]+"/"+
								DBsettings["database"])
		schema = DBsettings["schema"]
		IDs = [int(x) for x in analysisIDs]
		query = "SELECT * \
	  			FROM "+schema+".achilles_results \
	  			WHERE analysis_id in "+str(tuple(IDs))+";"
		queryRes = engine.execute(query)
		data = []
		for elem in queryRes:
			data.append(str(elem)[1:-1]+"\n")
		return None, data