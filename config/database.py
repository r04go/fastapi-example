from sqlalchemy import create_engine, MetaData

engine = create_engine('mysql+pymysql://')

meta = MetaData()

cdb = engine.connect()
