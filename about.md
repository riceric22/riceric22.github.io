---
layout: page
title: About Me
---

# Bio
Eric Wong is an Assistant Professor in the Department of Computer and Information Science at the University of Pennsylvania. He researches the foundations of robust systems, building on elements of machine learning and optimization to debug, understand, and develop reliable systems. 

<!-- He is a 2020 Siebel Scholar and received an honorable mention for his thesis on the robustness of deep networks to adversarial examples at Carnegie Mellon University advised by Zico Kolter. Prior to joining UPenn, he was a postdoc at CSAIL MIT advised by Aleksander Madry.  -->

<a href="https://riceric22.github.io/assets/img/photo_small.jpg">Link to photo</a>

<style type="text/css">
   /*! div style */
  .image-gallery {
    width: 100%;
    display: grid;
    grid-template-columns: repeat(auto-fill,minmax(200px, 1fr));
    justify-content: center;
    padding: 4px;
  }

  .box {
      flex-basis: 25%;
      width: 100%;
      padding: 10px;
      margin: 2px;
  }

  .img-gallery {
	width: 100%;
  height: 200px;
	object-fit: cover;
  transform: scale(1);
  transition: all 0.3s ease-in-out;
  }
  .img-gallery:hover {
    transform: scale(1.05);
  }
</style>


## Miscellaneous

I used to do competitive ballroom dancing as well as hip hop. 

I love experimenting with cooking, and occasionally post pictures of my creations on [Instagram](https://www.instagram.com/riceric22/). 

{% assign filenames = "french_toast.jpg,lobster_rolls.jpg,katsudon.jpg,mac_and_cheese.jpg,karaage.jpg,roast_pork.jpg,wok_stir_fry.jpg,shortrib.jpg,steak.jpg" | split: "," %}
<div class ="image-gallery">
{% for name in filenames %}
    <div class="box">
    <a href="{{ site.url }}{{ site.baseurl }}/assets/img/food/full/{{ name }}">
      <img src="{{ site.url }}{{ site.baseurl }}/assets/img/food/thumbs/{{ name }}" alt="{{ name }}"  class="img-gallery" />
     </a>
    </div>
 {% endfor %}
</div>
