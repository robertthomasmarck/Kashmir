from click.testing import CliRunner
from kashmir import *


def test_sync():
  runner = CliRunner()
  runner.invoke(kash, ['hist', '-tf', 'Day', '-s', '9-1-2020', '-e', '9-20-2020'])
