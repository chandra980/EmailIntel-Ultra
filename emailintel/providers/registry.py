from .dns_provider import DNSProvider
from .gravatar_provider import GravatarProvider
from .openpgp_provider import OpenPGPProvider
from .rdap_provider import RDAPProvider


def providers():
    return [
        DNSProvider(),
        RDAPProvider(),
        GravatarProvider(),
        OpenPGPProvider(),
    ]
