# django-bulmacss：快速搭建 Django 应用程序的必备工具

`django-bulmacss` 是一个基于 `Bulma CSS` 的常用 HTML 模板库，为 Django 开发者提供了快速搭建 Django 应用程序的解决方案。

`django-bulmacss` 提供了以下功能：

* 基于 Bulma CSS 的常用 HTML 模板，包括表单、导航栏、页脚、消息、模态框等。
* 开箱即用的 Django 扩展模板，如 Django-allauth、Django-filters、Django.contrib.flatpages 等。
* 允许您通过 Bulma CSS 的官方方式来自定义 CSS，比如通过 node-sass 来自定义 CSS 主题颜色等。

## Screenshots

![Login Page](./login.jpeg)

![User Profile](./profile.jpeg)

## Quick Start

Install Package

``` {.bash}
pip install django-bulmacss
```

修改`settings.py`

``` {.bash}
INSTALLED_APPS = [
    'bulma',
    ...
]

FORM_RENDERER = 'django.forms.renderers.TemplatesSetting'
```

## Extra

### Feather Icons

Simply beautiful open source icons

<https://feathericons.com/>

### Jdenticon

Open source library for generating identicons.

<https://jdenticon.com/>
