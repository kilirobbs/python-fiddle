from distutils.core import setup
setup(
      data_files=[('/sbin', ['rootfill']),
                  ('/etc/init.d', ['init-script'])]
     )