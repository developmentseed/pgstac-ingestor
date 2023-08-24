from typing import TYPE_CHECKING, List, Optional

from boto3.dynamodb import conditions
from pydantic import parse_obj_as

from pgstac_ingestor import schemas

if TYPE_CHECKING:
    from mypy_boto3_dynamodb.service_resource import Table


class Database:
    def __init__(self, table: "Table"):
        self.table = table

    def write(self, ingestion: schemas.Ingestion):
        self.table.put_item(Item=ingestion.dynamodb_dict())

    def fetch_one(self, username: str, ingestion_id: str):
        response = self.table.get_item(
            Key={"created_by": username, "id": ingestion_id},
        )
        try:
            return schemas.Ingestion.parse_obj(response["Item"])
        except KeyError as e:
            raise NotInDb("Record not found") from e

    def fetch_many(
        self,
        status: str,
        next: Optional[str] = None,
        limit: Optional[int] = None,
    ) -> schemas.ListIngestionResponse:
        response = self.table.query(
            IndexName="status",
            KeyConditionExpression=conditions.Key("status").eq(status),
            **{"Limit": limit} if limit else {},
            **{"ExclusiveStartKey": next} if next else {},
        )
        return schemas.ListIngestionResponse(
            items=parse_obj_as(List[schemas.Ingestion], response["Items"]),
            next=response.get("LastEvaluatedKey"),
        )


class NotInDb(Exception):
    ...
