from click.testing import CliRunner
from kashmir import *


def test_sync():
  runner = CliRunner()
  runner.invoke(hist, ['-tf', 'Day', '-s', '9-1-2022', '-e', '9-20-2022'])
