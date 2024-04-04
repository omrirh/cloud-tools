from simple_logger.logger import get_logger

LOGGER = get_logger(name=__name__)


def get_aro_supported_versions(aro_client, region):
    supported_versions = [aro_version.version for aro_version in aro_client.open_shift_versions.list(location=region)]
    LOGGER.info(f"ARO supported versions: {supported_versions}")
    return supported_versions


def get_azure_supported_regions(subscription_client, subscription_id):
    supported_regions = [
        region.name for region in subscription_client.subscriptions.list_locations(subscription_id=subscription_id)
    ]
    LOGGER.info(f"ARO supported regions: {supported_regions}")
    return supported_regions