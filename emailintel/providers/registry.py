from .cert_transparency_provider import CertificateTransparencyProvider
from .dns_provider import DNSProvider
from .github_commit_provider import GitHubCommitProvider
from .gravatar_provider import GravatarProvider
from .openpgp_provider import OpenPGPProvider
from .rdap_provider import RDAPProvider


def providers():
    return [
        DNSProvider(),
        RDAPProvider(),
        GitHubCommitProvider(),
        CertificateTransparencyProvider(),
        GravatarProvider(),
        OpenPGPProvider(),
    ]
