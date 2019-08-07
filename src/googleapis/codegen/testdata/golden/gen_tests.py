#!/usr/bin/python2.7
"""Hacky script to generate the test cases from the files we already have."""

import sys

for line in sys.stdin:
  line = line.rstrip()
  if not line.endswith('.golden'):
    continue
  language, variant, gold = line.split('/')
  base, _ = gold.split('.')

  print '\ngolden_output_test('  # )
  print '  name = "%s_%s_%s_test",' % (language, variant, gold)
  print '  discovery = "%s.json",' % base
  print '  golden_file = "%s",' % line
  print '  language = "%s",' % language
  print '  variant = "%s",' % variant
  print ')'
