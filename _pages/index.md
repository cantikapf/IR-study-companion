---
layout: default
title: IR Study Companion as Your Study Guide to Learn International Relations
permalink: /
---


<div class="hero-wrapper">
  <div class="hero-container">
    <h1 class="hero-title">Master International Relations</h1>
    <p class="hero-subtitle">
      A comprehensive, interactive study guide designed for enthusiasts and students. Explore global politics, theories, and diplomacy through engaging content.
    </p>
    <a href="{{site.baseurl}}/introduction.html" class="hero-btn">Start Learning Now 🚀</a>
  </div>
  <div class="hero-image-container" style="position: relative; overflow: visible;">
    <link rel="stylesheet" href="{{site.baseurl}}/assets/edankwan-globe/style.css">
    <div style="display: flex; flex-direction: column; align-items: center; width: 100%;">
      <div class="world" style="margin-right: 0;">
        <div class="world-bg"></div>
        <div class="world-globe">
            <div class="world-globe-pole"></div>
            <div class="world-globe-doms-container"></div>
            <div class="world-globe-halo"></div>
        </div>
      </div>
      <p style="font-size: 0.85rem; color: #6b7280; text-align: center; margin-top: -30px; z-index: 10; position: relative;">
        Interactive CSS 3D Globe by <a href="https://codepen.io/edankwan/pen/emqgpr" target="_blank" style="color: #3b82f6; text-decoration: none; font-weight: bold;">Edan Kwan</a>
      </p>
    </div>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/modernizr/2.8.3/modernizr.min.js"></script>
    <script src="https://public.codepenassets.com/js/prefixfree-1.0.7.min.js"></script>
    <script src="https://s3-us-west-2.amazonaws.com/s.cdpn.io/6043/css_globe_PerspectiveTransform.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/1.16.1/TweenMax.min.js"></script>
    <script src="{{site.baseurl}}/assets/edankwan-globe/script.js"></script>
  </div>
</div>

{% include homepage_progress.html %}

<h3 class="featured-title">Featured Modules</h3>
<div class="features-grid">
  {% assign featured = site.chapters | where: "layout", "part" | limit: 3 %}
  {% for doc in featured %}
  <a href="{{ site.baseurl }}{{ doc.url }}" class="feature-card">
    <h4 class="feature-title">{{ doc.title }}</h4>
    <p class="feature-desc">{{ doc.abstract | truncate: 120 }}</p>
  </a>
  {% endfor %}
</div>

<h3 class="featured-title" style="margin-top: 40px;">Why learn with us?</h3>

<div class="features-grid">
  <div class="feature-card">
    <div class="feature-icon">📖</div>
    <div class="feature-title">Comprehensive Modules</div>
    <p class="feature-desc">Over 100 structured chapters covering foundational theories to contemporary global issues.</p>
  </div>
  <div class="feature-card">
    <div class="feature-icon">🎮</div>
    <div class="feature-title">Interactive Simulations</div>
    <p class="feature-desc">Step into the shoes of world leaders with custom mini-games and decision-making scenarios.</p>
  </div>
  <div class="feature-card">
    <div class="feature-icon">🧠</div>
    <div class="feature-title">Active Recall</div>
    <p class="feature-desc">Test your knowledge with built-in flashcards and quizzes at the end of every chapter.</p>
  </div>
</div>

<div class="about-container">
  <h2 class="about-title">About this platform</h2>
  <p class="about-text">Designed with a focus on international relations, Asia, and Indonesia, this website aims to provide a structured learning path for those interested in this field. Whether you're a student or a curious mind, our courses are intended for study purposes, offering a wealth of knowledge without the need for external references.</p>
</div>

<div style="text-align: center; margin-top: 40px; padding-top: 20px; border-top: 1px solid #e5e7eb;">
  <h3 style="color: #6b7280; font-size: 1rem; margin-bottom: 10px;">Website Visitors</h3>
  <a href="https://github.com/antonkomarev/github-profile-views-counter">
    <img src="https://komarev.com/ghpvc/?username=cantikapf-IR-study-companion&label=Total%20Visitors&color=3B82F6&style=flat" alt="Visitor Count"/>
  </a>
</div>
