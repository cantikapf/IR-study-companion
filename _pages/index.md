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
  <div class="hero-image-container" style="position: relative; display: flex; align-items: center; justify-content: center;">
    <div style="background: rgba(255,255,255,0.65); border: 1px solid #e5e7eb; border-radius: 24px; padding: 32px; max-width: 420px; text-align: center; box-shadow: 0 10px 30px rgba(59,130,246,0.08);">
      <h3 style="margin: 0 0 12px; color: #1e3a5f; font-size: 1.25rem;">Belajar IR secara terstruktur</h3>
      <p style="margin: 0; color: #4b5563; line-height: 1.6;">Dari teori klasik hingga isu kontemporer dunia &mdash; 100+ bab, simulasi interaktif, dan latihan recall untuk memperkuat pemahamanmu.</p>
    </div>
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
