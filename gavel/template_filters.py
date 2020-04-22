import re

from flask import Markup
from gavel import app
from humanize import naturaltime

@app.template_filter('utcdatetime_local')
def _jinja2_filter_datetime_local(datetime):
    if datetime is None:
        return 'None'
    return naturaltime(datetime)

@app.template_filter('utcdatetime_epoch')
def _jinja2_filter_datetime_epoch(datetime):
    if datetime is None:
        return 0
    return datetime.strftime('%s')

@app.template_filter('youtube_embed')
def _jinja2_filter_youtube_embed(url: str):
    """
    Converts a wide assortment of YouTube URLs into an embedded IFrame.  Safely
    aborts by returning a hyperlink if regex fails, and "No URL specified" if
    not even a URL is passed in.
    """
    if url is None:
        return "No URL specified"

    id_group = 1
    embed_format_str = (
        "https://youtube.com/embed/{id_str}?"
        "rel=0&modestbranding=1&playsinline=1"
    )
    iframe_html_str = (
        '<iframe type="text/html" src="{embed_url}" frameborder="0" '
        'allow="accelerometer; encrypted-media; gyroscope; picture-in-picture" '
        'allowfullscreen></iframe>'
    )
    pattern = re.compile(r'(?:\/|%3D|v=|vi=)([0-9A-z-_]{11})(?:[%#?&]|$)')
    hyperlink_fallback = (
        f'<p><a href="{url}" target="_blank" rel="nofollow">{url}</a></p>'
    )

    try:
        match = pattern.search(url)
        id_str = match.group(id_group)
        embed_url = embed_format_str.format(id_str=id_str)
        return Markup(iframe_html_str.format(embed_url=embed_url))
    except (AttributeError, IndexError):
        return Markup(hyperlink_fallback)
