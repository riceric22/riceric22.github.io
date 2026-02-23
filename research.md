---
layout: page
title: Research
css: ["/assets/css/research-cards.css"]
---

How can we make sure that deep learning models are actually doing what we want them to do? I study the foundations of robust and reliable machine learning: how to understand, debug, and guarantee the behavior of machine learning models. My research interests span machine learning, optimization, and robustness, in order to develop principled methods with an eye towards scalability and practicality in real-world settings such as cosmology, surgery, cardiology, and sepsis. My work is organized around three themes: **Adversarial Safety**, **Interpretability with Guarantees**, and **Formal Assurances for Foundation Models**.

{% comment %}
  Flatten all papers into a single array for filtering.
{% endcomment %}
{% assign all_papers = "" | split: "" %}
{% for collection in site.data.papers %}
  {% for paper in collection.papers %}
    {% assign all_papers = all_papers | push: paper %}
  {% endfor %}
{% endfor %}

<!-- ═══ ADVERSARIAL SAFETY ═══ -->
<div class="research-card">
<h3><span class="card-icon"><i class="fas fa-shield-alt"></i></span> Adversarial Safety</h3>
<p class="card-desc">How do we defend models against adversarial threats, from perturbation attacks to jailbreaks to misuse? Topics include <strong>mechanistic theory of safety</strong>, <strong>alignment & control</strong>, <strong>jailbreaking & LLM defenses</strong>, and <strong>adversarial robustness</strong>.</p>
<div class="papers-preview" id="safety-papers">

<div class="subtheme-heading">Mechanistic Theory of Safety</div>
<p class="subtheme-desc">We develop theoretical frameworks that mechanistically explain how models follow and break rules, connecting attention mechanisms and logical inference to safety behaviors.</p>
<ul class="paper-list">
{% for p in all_papers %}{% if p.themes contains "adversarial-safety" and p.subtheme == "mechanistic-theory-of-safety" %}
<li>
  <div class="paper-title">{% if p.link %}<a href="{{ p.link }}">{{ p.title }}</a>{% else %}{{ p.title }}{% endif %}{% if p.short %}<span class="venue-badge">{{ p.short }}</span>{% endif %}</div>
  <div class="paper-authors">{{ p.authors | replace: "*", "" }}</div>
  {% if p.blog or p.github or p.website %}<div class="paper-links">{% if p.website %}<a href="{{ p.website }}">Site</a>{% endif %}{% if p.blog %}<a href="{{ p.blog }}">Blog</a>{% endif %}{% if p.github %}<a href="{{ p.github }}">Code</a>{% endif %}</div>{% endif %}
</li>
{% endif %}{% endfor %}
</ul>

<div class="subtheme-heading">Alignment & Control</div>
<p class="subtheme-desc">How do we control model behavior to prevent misuse and remove unwanted knowledge? We develop methods for machine unlearning, misuse mitigation, and cross-cultural alignment.</p>
<ul class="paper-list">
{% for p in all_papers %}{% if p.themes contains "adversarial-safety" and p.subtheme == "alignment-control" or p.themes contains "adversarial-safety" and p.subtheme == "concepts-structure" %}
<li>
  <div class="paper-title">{% if p.link %}<a href="{{ p.link }}">{{ p.title }}</a>{% else %}{{ p.title }}{% endif %}{% if p.short %}<span class="venue-badge">{{ p.short }}</span>{% endif %}</div>
  <div class="paper-authors">{{ p.authors | replace: "*", "" }}</div>
  {% if p.blog or p.github or p.website %}<div class="paper-links">{% if p.website %}<a href="{{ p.website }}">Site</a>{% endif %}{% if p.blog %}<a href="{{ p.blog }}">Blog</a>{% endif %}{% if p.github %}<a href="{{ p.github }}">Code</a>{% endif %}</div>{% endif %}
</li>
{% endif %}{% endfor %}
</ul>

<div class="subtheme-heading">Jailbreaking & LLM Defenses</div>
<p class="subtheme-desc">We study how adversarial prompts bypass LLM safety guardrails and develop principled defenses, spanning automated attack algorithms, smoothing-based defenses, and standardized benchmarks.</p>
<ul class="paper-list">
{% for p in all_papers %}{% if p.themes contains "adversarial-safety" and p.subtheme == "jailbreaking" %}
<li>
  <div class="paper-title">{% if p.link %}<a href="{{ p.link }}">{{ p.title }}</a>{% else %}{{ p.title }}{% endif %}{% if p.short %}<span class="venue-badge">{{ p.short }}</span>{% endif %}</div>
  <div class="paper-authors">{{ p.authors | replace: "*", "" }}</div>
  {% if p.blog or p.github or p.website %}<div class="paper-links">{% if p.website %}<a href="{{ p.website }}">Site</a>{% endif %}{% if p.blog %}<a href="{{ p.blog }}">Blog</a>{% endif %}{% if p.github %}<a href="{{ p.github }}">Code</a>{% endif %}</div>{% endif %}
</li>
{% endif %}{% endfor %}
</ul>

<div class="subtheme-heading">Adversarial Robustness</div>
<p class="subtheme-desc">We develop both empirical and provably certified defenses against adversarial perturbations, spanning threat models from Lp norms to patches to learned perturbation sets.</p>
<ul class="paper-list">
{% for p in all_papers %}{% if p.themes contains "adversarial-safety" and p.subtheme == "adversarial-robustness" %}
<li>
  <div class="paper-title">{% if p.link %}<a href="{{ p.link }}">{{ p.title }}</a>{% else %}{{ p.title }}{% endif %}{% if p.short %}<span class="venue-badge">{{ p.short }}</span>{% endif %}</div>
  <div class="paper-authors">{{ p.authors | replace: "*", "" }}</div>
  {% if p.blog or p.github or p.website %}<div class="paper-links">{% if p.website %}<a href="{{ p.website }}">Site</a>{% endif %}{% if p.blog %}<a href="{{ p.blog }}">Blog</a>{% endif %}{% if p.github %}<a href="{{ p.github }}">Code</a>{% endif %}</div>{% endif %}
</li>
{% endif %}{% endfor %}
</ul>

</div>
<a class="expand-link" href="#" data-target="safety-papers" data-label="Adversarial Safety">Show all Adversarial Safety papers <i class="fas fa-chevron-down"></i></a>
</div>

<!-- ═══ INTERPRETABILITY WITH GUARANTEES ═══ -->
<div class="research-card">
<h3><span class="card-icon"><i class="fas fa-search"></i></span> Interpretability with Guarantees</h3>
<p class="card-desc">What do model explanations actually mean? We build principled methods for understanding, debugging, and explaining ML models. Topics include <strong>concepts & structure</strong>, <strong>scientific & healthcare applications</strong>, <strong>certified explanations</strong>, and <strong>debugging</strong>.</p>
<div class="papers-preview" id="interpretability-papers">

<div class="subtheme-heading">Concepts & Structure</div>
<p class="subtheme-desc">What concepts do models learn, and how do they compose? We develop methods for extracting expert-aligned features, compositional concept representations, and topic-based explanations across domains and languages.</p>
<ul class="paper-list">
{% for p in all_papers %}{% if p.themes contains "interpretability" and p.subtheme == "concepts-structure" or p.themes contains "interpretability" and p.subtheme == "neurosymbolic" or p.themes contains "interpretability" and p.subtheme == "alignment-control" %}
<li>
  <div class="paper-title">{% if p.link %}<a href="{{ p.link }}">{{ p.title }}</a>{% else %}{{ p.title }}{% endif %}{% if p.short %}<span class="venue-badge">{{ p.short }}</span>{% endif %}</div>
  <div class="paper-authors">{{ p.authors | replace: "*", "" }}</div>
  {% if p.blog or p.github or p.website %}<div class="paper-links">{% if p.website %}<a href="{{ p.website }}">Site</a>{% endif %}{% if p.blog %}<a href="{{ p.blog }}">Blog</a>{% endif %}{% if p.github %}<a href="{{ p.github }}">Code</a>{% endif %}</div>{% endif %}
</li>
{% endif %}{% endfor %}
</ul>

<div class="subtheme-heading">Scientific & Healthcare Applications</div>
<p class="subtheme-desc">We apply interpretable ML methods to high-stakes scientific and medical settings, including treatment effect estimation, anomaly repair with formal guarantees, and clinical prediction.</p>
<ul class="paper-list">
{% for p in all_papers %}{% if p.themes contains "interpretability" and p.subtheme == "scientific-healthcare" %}
<li>
  <div class="paper-title">{% if p.link %}<a href="{{ p.link }}">{{ p.title }}</a>{% else %}{{ p.title }}{% endif %}{% if p.short %}<span class="venue-badge">{{ p.short }}</span>{% endif %}</div>
  <div class="paper-authors">{{ p.authors | replace: "*", "" }}</div>
  {% if p.blog or p.github or p.website %}<div class="paper-links">{% if p.website %}<a href="{{ p.website }}">Site</a>{% endif %}{% if p.blog %}<a href="{{ p.blog }}">Blog</a>{% endif %}{% if p.github %}<a href="{{ p.github }}">Code</a>{% endif %}</div>{% endif %}
</li>
{% endif %}{% endfor %}
</ul>

<div class="subtheme-heading">Certified Explanations</div>
<p class="subtheme-desc">Can we trust model explanations? We develop explanation methods with provable guarantees, including certified stability for feature attributions and faithful group-based models.</p>
<ul class="paper-list">
{% for p in all_papers %}{% if p.themes contains "interpretability" and p.subtheme == "certified-explanations" %}
<li>
  <div class="paper-title">{% if p.link %}<a href="{{ p.link }}">{{ p.title }}</a>{% else %}{{ p.title }}{% endif %}{% if p.short %}<span class="venue-badge">{{ p.short }}</span>{% endif %}</div>
  <div class="paper-authors">{{ p.authors | replace: "*", "" }}</div>
  {% if p.blog or p.github or p.website %}<div class="paper-links">{% if p.website %}<a href="{{ p.website }}">Site</a>{% endif %}{% if p.blog %}<a href="{{ p.blog }}">Blog</a>{% endif %}{% if p.github %}<a href="{{ p.github }}">Code</a>{% endif %}</div>{% endif %}
</li>
{% endif %}{% endfor %}
</ul>

<div class="subtheme-heading">Debugging</div>
<p class="subtheme-desc">We build tools for diagnosing model failures, from sparse linear layers for debuggable networks to methods for detecting spurious correlations, data biases, and transfer learning pathologies.</p>
<ul class="paper-list">
{% for p in all_papers %}{% if p.themes contains "interpretability" and p.subtheme == "debugging" %}
<li>
  <div class="paper-title">{% if p.link %}<a href="{{ p.link }}">{{ p.title }}</a>{% else %}{{ p.title }}{% endif %}{% if p.short %}<span class="venue-badge">{{ p.short }}</span>{% endif %}</div>
  <div class="paper-authors">{{ p.authors | replace: "*", "" }}</div>
  {% if p.blog or p.github or p.website %}<div class="paper-links">{% if p.website %}<a href="{{ p.website }}">Site</a>{% endif %}{% if p.blog %}<a href="{{ p.blog }}">Blog</a>{% endif %}{% if p.github %}<a href="{{ p.github }}">Code</a>{% endif %}</div>{% endif %}
</li>
{% endif %}{% endfor %}
</ul>

</div>
<a class="expand-link" href="#" data-target="interpretability-papers" data-label="Interpretability">Show all Interpretability papers <i class="fas fa-chevron-down"></i></a>
</div>

<!-- ═══ FORMAL ASSURANCES FOR FOUNDATION MODELS ═══ -->
<div class="research-card">
<h3><span class="card-icon"><i class="fas fa-brain"></i></span> Formal Assurances for Foundation Models</h3>
<p class="card-desc">How can we bring formal structure and provable guarantees to foundation models through programs, logic, and verification? Topics include <strong>verifying & faithful reasoning</strong> and <strong>neurosymbolic learning</strong>.</p>
<div class="papers-preview" id="formal-papers">

<div class="subtheme-heading">Verifying & Faithful Reasoning</div>
<p class="subtheme-desc">Can we verify that a model's reasoning is sound? We develop methods for certifying reasoning chain correctness, ensuring chain-of-thought faithfulness, and checking whether models follow statistical rules inferred from data.</p>
<ul class="paper-list">
{% for p in all_papers %}{% if p.themes contains "formal-assurances" and p.subtheme == "verifying-reasoning" or p.themes contains "formal-assurances" and p.subtheme == "mechanistic-theory-of-safety" %}
<li>
  <div class="paper-title">{% if p.link %}<a href="{{ p.link }}">{{ p.title }}</a>{% else %}{{ p.title }}{% endif %}{% if p.short %}<span class="venue-badge">{{ p.short }}</span>{% endif %}</div>
  <div class="paper-authors">{{ p.authors | replace: "*", "" }}</div>
  {% if p.blog or p.github or p.website %}<div class="paper-links">{% if p.website %}<a href="{{ p.website }}">Site</a>{% endif %}{% if p.blog %}<a href="{{ p.blog }}">Blog</a>{% endif %}{% if p.github %}<a href="{{ p.github }}">Code</a>{% endif %}</div>{% endif %}
</li>
{% endif %}{% endfor %}
</ul>

<div class="subtheme-heading">Neurosymbolic Learning</div>
<p class="subtheme-desc">We combine neural networks with symbolic programs to enable scalable, data-efficient learning with formal structure, from programmable frameworks to compositional tensor methods.</p>
<ul class="paper-list">
{% for p in all_papers %}{% if p.themes contains "formal-assurances" and p.subtheme == "neurosymbolic" %}
<li>
  <div class="paper-title">{% if p.link %}<a href="{{ p.link }}">{{ p.title }}</a>{% else %}{{ p.title }}{% endif %}{% if p.short %}<span class="venue-badge">{{ p.short }}</span>{% endif %}</div>
  <div class="paper-authors">{{ p.authors | replace: "*", "" }}</div>
  {% if p.blog or p.github or p.website %}<div class="paper-links">{% if p.website %}<a href="{{ p.website }}">Site</a>{% endif %}{% if p.blog %}<a href="{{ p.blog }}">Blog</a>{% endif %}{% if p.github %}<a href="{{ p.github }}">Code</a>{% endif %}</div>{% endif %}
</li>
{% endif %}{% endfor %}
</ul>

</div>
<a class="expand-link" href="#" data-target="formal-papers" data-label="Formal Assurances">Show all Formal Assurances papers <i class="fas fa-chevron-down"></i></a>
</div>

<div class="research-footer">
Before this, I have dabbled in a <a href="https://arxiv.org/abs/1705.00772">semismooth Newton method</a> (ICML 2017), an <a href="http://zicokolter.com/publications/wong2015svdkernel.pdf">SVD kernel approach</a> (AAAI 2015), as well as a <a href="https://github.com/locuslab/dreaml">reactive programming language</a> that became obsolete when PyTorch was released. My PhD thesis can be found <a href="https://www.ml.cmu.edu/research/phd-dissertation-pdfs/thesis-wong-eric.pdf">here</a>.
</div>

<script>
document.querySelectorAll('.expand-link').forEach(function(link) {
  link.addEventListener('click', function(e) {
    e.preventDefault();
    var target = document.getElementById(this.getAttribute('data-target'));
    var isExpanded = target.classList.toggle('expanded');
    var label = this.getAttribute('data-label');
    if (isExpanded) {
      this.innerHTML = 'Show fewer ' + label + ' papers <i class="fas fa-chevron-up"></i>';
    } else {
      this.innerHTML = 'Show all ' + label + ' papers <i class="fas fa-chevron-down"></i>';
    }
  });
});
</script>
