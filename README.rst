uwsgimon
========

``uwsgimon`` uses uWSGI Stats Server to produce arbitrary output that
can be used to monitor your uwsgi application, e.g. ``InfluxDB``
``Graphite``.

To use uWSGI Stat Server simply use the ``stats`` option followed by
a valid socket address, for example::s

    uwsgi --module myapp --socket :3030 --stats /tmp/stats.socket

Note: If you want the stats served over HTTP you will need to also add
the ``stats-http`` option.

To start monitoring your application with ``uwsgimon`` call it with
the socket address::

    uwsgimon --node xcfapp-app-01 --frequency 10 /tmp/stats.socket

Installation
------------

::

    pip install git+https://github.com/ushuz/uwsgimon.git

Usage
-----

    $ uwsgimon --help
    usage: uwsgimon [-h] [--node NODE] [--frequency FREQ] [--format FORMAT] stats

    positional arguments:
      stats                 uWSGI stats address

    optional arguments:
      -h, --help            show this help message and exit
      --node NODE, -n NODE  uWSGI node name, current hostname by default
      --frequency FREQ, -q FREQ
                            uWSGI stats refresh frequency, in seconds
      --format FORMAT, -f FORMAT
                            output format, available variables:
                                ver  - uWSGI version
                                node - uWSGI node name
                                req  - total requests
                                rps  - requests per second
                                avg  - average response time
                                lq   - listen queue
                                tx   - traffic

                            e.g. "uwsgi,node={node} req={req}i,rps={rps}i,avg={avg},lq={lq}i,tx={tx}i"

Further Reading
---------------

For more info on uWSGI Stats Server see http://projects.unbit.it/uwsgi/wiki/StatsServer
