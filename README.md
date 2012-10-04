DionaeaFR
=========

Front Web to Dionaea log analysis.

[*] Technologies:
  
  - Python 2.7.3
  - Django 1.4
  - Bootstrap Framework 2.1.1
  - Jvectormaps 1.0
  - Kendo-UI v2011.3.1129
  - SQLite3

[*] Requeriments:
  
  - pygeoip
  - django-pagination

[*] Install

  Copy /opt/dionaea/var/dionaea/logsql.sqlite to DionaeaFR/Database directory
  
  Change STATICFILES_DIRS in DionaeaFR/Dionaea/settings.py to absolute paths of DionaeaFR/static
  Change TEMPLATE_DIRS in DionaeaFR/Dionaea/settings.py to absolute paths of DionaeaFR/Templates
  
  python manage.py collecstatic
  python manage.py runserver
  
  Access to http://localhost:8000 in browser.

[*] Upcoming

  - Add filters in connections table.
  - Add filters in downloads table.
  - Add more Graphs and Maps.

¿Suggestions?

Designed by @rubenespadas