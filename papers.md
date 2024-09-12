---
layout: page
title: Papers
---

{% for collection in site.data.papers %}
### {{ collection.year }}
  {% for paper in collection.papers %}
  + [{{ paper.title }}]({{ paper.link }})  
    {{ paper.authors | replace: "*", "\*" }}  
    {% if paper.conference -%}
      {{ paper.conference }}  
    {% endif -%}
    {% if paper.blog -%}
      [Blog Post]({{ paper.blog }}){%- if paper.github %} \+ {% endif -%}
    {%- endif -%}
    {%- if paper.blog -%}
      [Source Code on GitHub]({{ paper.github }})
    {%- endif %}
  {% endfor %}
{% endfor %}


## Other
My PhD thesis can be found <a href='https://www.ml.cmu.edu/research/phd-dissertation-pdfs/thesis-wong-eric.pdf'>here</a>. 
