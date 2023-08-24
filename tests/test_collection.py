import os
from unittest.mock import Mock, patch

import pytest
import pgstac_ingestor.collection as collection
from pgstac_ingestor.utils import DbCreds

from pypgstac.load import Methods


@pytest.fixture()
def loader():
    with patch("pgstac_ingestor.collection.Loader", autospec=True) as m:
        yield m


@pytest.fixture()
def pgstacdb():
    with patch("pgstac_ingestor.collection.PgstacDB", autospec=True) as m:
        m.return_value.__enter__.return_value = Mock()
        yield m


def test_load_collections(stac_collection, loader, pgstacdb):
    with patch(
        "pgstac_ingestor.collection.get_db_credentials",
        return_value=DbCreds(
            username="", password="", host="", port=1, dbname="", engine=""
        ),
    ):
        os.environ["DB_SECRET_ARN"] = ""
        collection.ingest(stac_collection)

    loader.return_value.load_collections.assert_called_once_with(
        file=[stac_collection.to_dict()],
        insert_mode=Methods.upsert,
    )
