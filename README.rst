Bulma主题模板
=============

为Django开发提供常用的页面模板

Quick Start
-----------

修改\ ``settings.py``

::

   INSTALLED_APPS = [
       'bulma',
       ...
   ]

   FORM_RENDERER = 'django.forms.renderers.TemplatesSetting'

Includes
--------

基础模板
~~~~~~~~

-  base.html
-  navbar.html
-  footer.html
-  profile.html
-  empty.html
-  pagination.html
-  search_bar.html
-  messages.html

django-allauth
~~~~~~~~~~~~~~

替换allauth的简易模板

模板form表单
~~~~~~~~~~~~

替换django默认的django/forms目录

django-filters
~~~~~~~~~~~~~~

-  filters.html
