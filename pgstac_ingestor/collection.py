import os

from pgstac_ingestor.loader import Loader
from pgstac_ingestor.schemas import StacCollection
from pgstac_ingestor.utils import get_db_credentials
from pypgstac.db import PgstacDB
from pypgstac.load import Methods


def ingest(collection: StacCollection):
    """
    Takes a collection model,
    does necessary preprocessing,
    and loads into the PgSTAC collection table
    """
    try:
        creds = get_db_credentials(os.environ["DB_SECRET_ARN"])
        with PgstacDB(dsn=creds.dsn_string, debug=True) as db:
            loader = Loader(db=db)
            loader.load_collections(
                # pypgstac wants either a string or an Iterable of dicts.
                file=[collection.to_dict()],
                insert_mode=Methods.upsert,
            )
    except Exception as e:
        print(f"Encountered failure loading collection into pgSTAC: {e}")


def delete(collection_id: str):
    """
    Deletes the collection from the database
    """
    creds = get_db_credentials(os.environ["DB_SECRET_ARN"])
    with PgstacDB(dsn=creds.dsn_string, debug=True) as db:
        loader = Loader(db=db)
        loader.delete_collection(collection_id)
