import decimal
import json
from dataclasses import dataclass

import boto3

database_client = boto3.client("dynamodb", endpoint_url="http://dynamo-local:8000")
database_resource = boto3.resource("dynamodb", endpoint_url="http://dynamo-local:8000")


@dataclass
class Game:
    id: int
    title: str = None
    authors: set = None
    new_field: set = None
    new_field2: set = None
    other_field: str = None


def lambda_handler(event, context):
    print("-------------------------------------------------------------")
    print(database_client.list_tables())
    print("-------------------------------------------------------------")
    game_database = database_resource.Table("Game")
    print(game_database)
    print("-------------------------------------------------------------")
    # method 1: client update
    database_client.update_item(
        TableName="Game",
        Key={"id": {"N": "1"}},
        UpdateExpression="ADD new_field :val",
        ExpressionAttributeValues={":val": {"SS": ("TEST", "Another value")}}
    )
    # method 2: resource update
    game_database.update_item(
        Key={"id": 1},
        UpdateExpression="ADD new_field2 :val",
        ExpressionAttributeValues={":val": set(("value 1", "value 2"))}
    )
    print("-------------------------------------------------------------")
    print(event["queryStringParameters"])
    print("-------------------------------------------------------------")
    response = game_database.scan()
    response_items = response["Items"]
    print(response_items)

    response_objects = [Game(**item) for item in response_items]
    print(f"\033[92m {response_objects[0]} \033[0m")

    return {
        "statusCode": 200,
        "body": json.dumps(response_items, cls=EnhancedJSONEncoder)
    }


class EnhancedJSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            return int(o)

        if isinstance(o, set):
            return [*o]

        return super().default(o)
