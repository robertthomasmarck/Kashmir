from click.testing import CliRunner
from kashmir import kash


def test_sync():
  runner = CliRunner()
  runner.invoke(kash, ['hist', '-tf', 'Day'])
