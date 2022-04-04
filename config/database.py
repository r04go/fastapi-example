from sqlalchemy import create_engine, MetaData

engine = create_engine('mysql+pymysql://kamajuhaq5a11lei:g8a4m4xzq8cd4uu5@dcrhg4kh56j13bnu.cbetxkdyhwsb.us-east-1.rds.amazonaws.com:3306/iotbi0bkia5eryb7')

meta = MetaData()

cdb = engine.connect()