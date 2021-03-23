"""
Tests for the create_credentials_api_configuration command
"""

from unittest import TestCase

import mock
import pytest
from django.core.management import call_command

from openedx.core.djangoapps.credentials.models import CredentialsApiConfig

from ..create_credentials_api_configuration import Command

COMMAND_MODULE = 'openedx.core.djangoapps.credentials.management.commands.create_credentials_api_configuration'

@pytest.mark.django_db
class CertAllowlistGenerationTests(TestCase):
    """
    Tests for the create_credentials_api_configuration management command
    """

    def setUp(self):
        super().setUp()
        CredentialsApiConfig.objects.create(
            enabled=False
        )

    @mock.patch(COMMAND_MODULE)
    def test_successful_generation(self, mock):
        call_command(Command())
        assert CredentialsApiConfig.objects.get(enabled=True)
