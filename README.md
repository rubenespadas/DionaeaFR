DionaeaFR
=========

Front Web to Dionaea low-interaction honeypot.

Home DionaeaFR: http://rootingpuntoes.github.com/DionaeaFR/

Home Dionaea:   http://dionaea.carnivore.it/

[*] Technologies:

  - Python 2.7.3
  - Django 1.4
  - Jquery 1.7.2
  - Bootstrap Framework 2.1.1
  - jVectorMap 1.0
  - Kendo-UI v2011.3.1129
  - SQLite3

[*] Requeriments:

	pip install Django
	pip install pygeoip
	pip install django-pagination
	pip install django-tables2
	pip install django-compressor
	pip install django-htmlmin
	
	django-tables2-simplefilter:
		https://github.com/benjiec/django-tables2-simplefilter
	
	npm install -g less

[*] Install

  Copy /opt/dionaea/var/dionaea/logsql.sqlite to DionaeaFR root directory
  
  Download GeoIP and GeoLiteCity:
  
    wget http://geolite.maxmind.com/download/geoip/database/GeoLiteCity.dat.gz
    wget http://geolite.maxmind.com/download/geoip/database/GeoLiteCountry/GeoIP.dat.gz

  Decompress GeoIP and GeoLiteCity:
  
    gunzip GeoLiteCity.dat.gz
    gunzip GeoIP.dat.gz

  Move GeoIP and GeoLiteCity to DionaeaFR/static:
  
    mv GeoIP.dat DionaeaFR/static
	mv GeoLiteCity.dat DionaeaFR/static

  Change STATICFILES_DIRS in DionaeaFR/settings.py to absolute paths of DionaeaFR/static

  Change TEMPLATE_DIRS in DionaeaFR/settings.py to absolute paths of DionaeaFR/Templates
  
  Run server:
  
	python manage.py collectstatic
	python manage.py runserver

  Access to http://localhost:8000 in browser.

[*] Changelog

  - Add transport, type and protocol filters in connections table.
  - Add Attacks graph last 7 days.
  
  29/11/2012
	- Add less support
	- Add HTML minify
	- Add menu icons
	- Other visuals changes

[*] Suggestions?

Designed by @rubenespadas