from unittest import TestCase

import pytest


@pytest.mark.usefixtures("host")
class TestAlpine(TestCase):
    def setUp(self):
        super(TestAlpine, self).setUp()

    def test_version(self):
        f = self.host.file("/etc/os-release")

        self.assertTrue(f.contains("VERSION_ID=3"))

    def test_required_packages(self):
        packages = ["ca-certificates"]
        for package in packages:
            self.assertTrue(self.host.package(package).is_installed)

    def test_prometheus_binary(self):
        prometheus = '/bin/prometheus-ecs-discovery'
        self.assertTrue(self.host.exists(prometheus))
