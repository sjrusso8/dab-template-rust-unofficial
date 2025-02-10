import os
import asyncio
from urllib.parse import urlparse

import nest_asyncio

from ._internal import rust_task

nest_asyncio.apply()


def _set_environment():
    from dbruntime import get_databricks_shell

    shell = get_databricks_shell()
    metadata = shell.parent_header.get("metadata", {})
    cmd_metadata = metadata.get("commandMetadata", {})
    extra_context = cmd_metadata.get("extraContext", {})

    session_id = metadata.get("spark_connect_compute_session_id")
    cluster_id = cmd_metadata.get("tags", {}).get("clusterId")
    affinity = extra_context.get("sparkAffinityKey")
    channel = extra_context.get("dbrPlatformChannel")
    token = extra_context.get("api_token")
    api_url = extra_context.get("api_url")

    if session_id:
        os.environ["DATABRICKS_SERVERLESS_SESSION_ID"] = session_id

    if cluster_id:
        os.environ["DATABRICKS_SERVERLESS_CLUSTER_ID"] = cluster_id

    if api_url:
        os.environ["DATABRICKS_REMOTE_HOST"] = urlparse(api_url).hostname

    if token:
        os.environ["DATABRICKS_API_TOKEN"] = token

    if affinity:
        os.environ["DATABRICKS_SERVERLESS_AFFINITY"] = affinity

    if channel:
        os.environ["DATABRICKS_SERVERLESS_CHANNEL"] = channel

    os.environ["DATABRICKS_SERVERLESS_ADD_PORT"] = str(
        int(
            shell.spark_config.get(
                "databricks.manager.mtlsControlPlaneClientPort", "7073"
            )
        )
    )


async def rust_pipeline():
    _set_environment()
    await rust_task()


def main():
    asyncio.run(rust_pipeline())
