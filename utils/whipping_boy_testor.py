from click.testing import CliRunner
from kashmir import cli


def test_sync():
  runner = CliRunner()
  runner.invoke(cli, ['look-at-assets'])
