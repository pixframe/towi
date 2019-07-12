{% extends "admin/base.html" %}

{% block title %}{{ title }} | {{ site_title|default:_('Towi Administration') }}{% endblock %}

{% block branding %}
<h1 id="site-name"><a href="{% url 'admin:index' %}">{{ site_header|default:_('Towi administration') }}</a></h1>
{% endblock %}

{% block nav-global %}{% endblock %}
