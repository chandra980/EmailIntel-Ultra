from emailintel.providers import providers


def test_provider_registry_has_real_entries():
    items = providers()
    assert len(items) == 6
    assert all(not provider.requires_auth for provider in items)
    assert len({provider.name for provider in items}) == len(items)
    assert all(provider.source_name for provider in items)
    assert all(provider.source_homepage for provider in items)
    assert all(provider.access_method == "anonymous-public" for provider in items)
