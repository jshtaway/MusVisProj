from sqlalchemy import Column, String, Float, Integer, create_engine
from sqlalchemy.ext.declarative import declarative_base
from pandas import read_csv
import pandas as pd 

engine = create_engine('sqlite:///events.sqlite', echo=True)

def createTable():
    Base = declarative_base()
    class artist_events(Base):
        __tablename__ = "artist_events"
        id = Column(Integer, primary_key=True)
        artist_name = Column(String)
        city = Column(String)
        date = Column(String)
        lat = Column(Float)
        lng = Column(Float)
        consert_name = Column(String)
        popularity = Column(Float)

    
    Base.metadata.create_all(engine)

def append_table(artist, csvFile):
    event_df = read_csv(csvFile)
    event_df['Lat'].infer_objects()
    event_df['Lng'].infer_objects()
    event_df['Popularity'].infer_objects()
    event_df['Artist'] = artist
    event_df.columns = ['city', 'date', 'lat', 'lng', 'consert_name', 'popularity', 'artist_name']
    event_df.to_sql('artist_events', con=engine, if_exists='append', index=False)