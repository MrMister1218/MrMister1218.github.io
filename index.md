---
layout: home
title: "{{ site.data.profile.name }} — {{ site.data.profile.title }}"
---

{% assign p = site.data.profile %}

<!-- HERO -->
<div class="hero">
  {% if p.avatar_image %}
  <img class="hero-avatar hero-avatar--img" src="{{ p.avatar_image }}" alt="{{ p.name }}">
  {% else %}
  <div class="hero-avatar">{{ p.avatar_initials }}</div>
  {% endif %}
  <div class="hero-status">{{ p.status }}</div>
  <h1>{{ p.name }}</h1>
  <p class="hero-sub">{{ p.subtitle }}</p>
  <div class="hero-tags">
    {% for tag in p.hero_tags %}
    <span class="hero-tag">{{ tag }}</span>
    {% endfor %}
  </div>
</div>

<!-- ABOUT -->
<div class="section">
  <h2 class="section-title" data-num="01">About Me</h2>
  <div class="glass about-text">
    {% for item in p.about.background %}
    {{ item }}
    {% endfor %}
    <br><br>
    {% for item in p.about.extra %}
    {{ item }}
    {% endfor %}
  </div>
</div>

<!-- SKILLS -->
<div class="section">
  <h2 class="section-title" data-num="02">Skills</h2>
  <div class="skills-grid">
    {% for skill in p.skills %}
    <div class="glass skill-card">
      <h3><i class="fas {{ skill.icon }}"></i> {{ skill.category }}</h3>
      <ul>
        {% for item in skill.items %}
        <li><span class="skill-dot"></span>{{ item }}</li>
        {% endfor %}
      </ul>
    </div>
    {% endfor %}
  </div>
</div>

<!-- PROJECTS -->
<div class="section">
  <h2 class="section-title" data-num="03">Projects</h2>
  {% for project in p.projects %}
  <div class="glass project-card">
    <h3><i class="fas {{ project.icon }}" style="color: var(--primary);"></i> {{ project.title }}</h3>
    <span class="project-year">{{ project.period }}{% if project.tag != "" %} — {{ project.tag }}{% endif %}</span>
    <p>{{ project.description }}</p>
    <ul>
      {% for detail in project.details %}
      <li><strong>{{ detail.key }}:</strong> {{ detail.val }}</li>
      {% endfor %}
    </ul>
    {% if project.github %}
    <a class="project-link" href="{{ project.github }}" target="_blank">
      <i class="fab fa-github"></i> View on GitHub
    </a>
    {% endif %}
  </div>
  {% endfor %}
</div>

<!-- RESUME -->
<div class="section">
  <h2 class="section-title" data-num="04">Resume</h2>
  <div class="resume-block">
    <p>{{ p.resume.message }}</p>
    <a class="resume-btn" href="{{ p.resume.pdf }}" target="_blank">
      <i class="fas fa-file-pdf"></i> Download Resume (PDF)
    </a>
  </div>
</div>

<!-- CONTACT -->
<div class="section">
  <h2 class="section-title" data-num="05">Contact</h2>
  <div class="contact-grid">

    <a class="glass contact-card" href="mailto:{{ p.contact.email }}">
      <div class="contact-icon email"><i class="fas fa-envelope"></i></div>
      <div class="contact-info">
        <div class="label">Email</div>
        <div class="value">{{ p.contact.email }}</div>
      </div>
    </a>

    <a class="glass contact-card" href="{{ p.contact.github }}" target="_blank">
      <div class="contact-icon github"><i class="fab fa-github"></i></div>
      <div class="contact-info">
        <div class="label">GitHub</div>
        <div class="value">{{ p.contact.github_handle }}</div>
      </div>
    </a>

    <a class="glass contact-card" href="{{ p.contact.linkedin }}" target="_blank">
      <div class="contact-icon linkedin"><i class="fab fa-linkedin-in"></i></div>
      <div class="contact-info">
        <div class="label">LinkedIn</div>
        <div class="value">{{ p.contact.linkedin_handle }}</div>
      </div>
    </a>

  </div>
</div>

<footer class="page-footer">
  Designed &amp; built by <strong>{{ p.name }}</strong> · {{ site.time | date: '%Y' }} · Powered by GitHub Pages
</footer>
