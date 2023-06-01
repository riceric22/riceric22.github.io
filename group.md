---
layout: page
title: Group  
---

### PhD students

<div class ="avatar-gallery">
{% for student in site.data.group.phd %}
    <div class="avatar-container">
    	<div class="avatar-img-border">
	      <img src="{{ student.photo }}" alt="{{ student.name }}"  class="avatar-img" />
  		</div>	
	    <div class="avatar-name">
		    <a href="{{ student.url }}">{{ student.name }}</a>
		      {% if student.coadvisor -%}
		      <br>(co-advised with <a href="{{ student.coadvisor_url }}">{{ student.coadvisor }}</a>)
		      {%- endif %}
		</div>
    </div>
 {% endfor %}
</div>

<hr style="clear:both;">

### Collaborators

In addition, I have had the fortune of being able to work on various papers with the following students/postdocs here at UPenn: 

+ [Aaditya Naik](https://www.seas.upenn.edu/~asnaik/) 
+ [Adam Stein](https://www.seas.upenn.edu/~steinad/)
+ [Anton Xue](https://antonxue.github.io/)
+ [Natalie Maus](https://antonxue.github.io/)
+ [Patrick Chao](https://patrickrchao.github.io/)
+ [Tai Nguyen](https://taidnguyen.github.io/)
+ [Veronica Lyu](https://veronica320.github.io/)
+ [Yinjun Wu](https://www.seas.upenn.edu/~wuyinjun/)

