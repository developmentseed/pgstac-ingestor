from unittest.mock import Mock, patch

import pytest
from fastapi.encoders import jsonable_encoder

from pgstac_ingestor.utils import DbCreds
from pypgstac.load import Methods


@pytest.fixture()
def loader():
    with patch("pgstac_ingestor.utils.Loader", autospec=True) as m:
        yield m


@pytest.fixture()
def pgstacdb():
    with patch("pgstac_ingestor.utils.PgstacDB", autospec=True) as m:
        m.return_value.__enter__.return_value = Mock()
        yield m


@pytest.fixture()
def dbcreds():
    dbcreds = DbCreds(username="", password="", host="", port=1, dbname="", engine="")
    return dbcreds


def test_load_items(loader, pgstacdb, example_ingestion, dbcreds):
    from pgstac_ingestor import utils

    utils.load_items(dbcreds, [example_ingestion])
    loader.return_value.load_items.assert_called_once_with(
        file=jsonable_encoder([example_ingestion.item]),
        insert_mode=Methods.upsert,
    )
