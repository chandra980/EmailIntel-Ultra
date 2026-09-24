from emailintel.providers import providers


def test_provider_registry_has_real_entries():
    items = providers()
    assert len(items) == 4
    assert all(not provider.requires_auth for provider in items)
    assert len({provider.name for provider in items}) == len(items)
