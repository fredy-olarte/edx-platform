"""
Tests for the create_credentials_api_configuration command
"""

import pytest
from unittest import TestCase
from django.core.management import CommandError, call_command
from waffle.testutils import override_switch
from openedx.core.djangoapps.credentials.models import CredentialsApiConfig


@pytest.mark.django_db
class CertAllowlistGenerationTests(TestCase):
    """
    Tests for the create_credentials_api_configuration management command
    """

    def test_successful_generation(self):
        call_command("create_credentials_api_configuration")
        assert len(CredentialsApiConfig.objects.all()) > 0
