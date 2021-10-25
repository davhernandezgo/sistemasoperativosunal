import os
for variable, valor in os.environ.iteritems():
    print ("%s: %s" % (variable, valor))