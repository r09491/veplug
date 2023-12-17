from setuptools import setup

with open("README.md", 'r') as f:
    long_description = f.read()
    
setup(name='victron_plug',
      version='0.2',
      description='Victron serial VE.Direct decoder',
      url='https://github.com/r09491/vesocket',
      author='r09491',
      author_email='r09491@gmail.com',
      license='MIT',
      long_description=long_description,
      scripts=[
          './victron_plug_scripts/victron_plug_latest_single.py',
          './victron_plug_scripts/victron_plug_latest_loop.py',
          './victron_plug_scripts/victron_plug_plot.py',
          './victron_plug_scripts/victron_plug_plot.sh',
          './victron_plug_scripts/victron_plug_plot_yesterday.sh',
          './victron_plug_scripts/victron_plug_watts.py',
          './victron_plug_scripts/victron_plug_watt_hours.py',
          './victron_plug_scripts/victron_plug_latest_serial_cron.sh',
          './victron_plug_scripts/victron_plug_latest_socket_cron.sh',
          './victron_plug_scripts/victron_plug_watts_cron.sh',
          './victron_plug_scripts/victron_plug_watt_hours_cron.sh',
          './victron_plug_scripts/victron_plug_aliases.sh',
      ],
      packages=['victron_plug',
                'victron_converters'],
      install_requires=['pyserial',
                        'pandas',
                        'termgraph',
      ],
      zip_safe=False)
