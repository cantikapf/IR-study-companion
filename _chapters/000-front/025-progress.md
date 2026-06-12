---
title: My Progress
slug: progress
---

<style>
.progress-dashboard {
    font-family: 'Inter', sans-serif;
    margin-top: 20px;
}

.progress-header {
    background: linear-gradient(135deg, #1e3a8a, #3b82f6);
    color: white;
    padding: 30px;
    border-radius: 12px;
    box-shadow: 0 10px 20px rgba(59, 130, 246, 0.2);
    margin-bottom: 40px;
}

.progress-header h2 {
    margin-top: 0;
    color: white !important;
    border-bottom: none;
    font-weight: 700;
}

.progress-bar-container {
    width: 100%;
    height: 12px;
    background-color: rgba(255, 255, 255, 0.2);
    border-radius: 10px;
    margin: 20px 0;
    overflow: hidden;
}

.progress-bar-fill {
    height: 100%;
    background-color: #10b981;
    border-radius: 10px;
    transition: width 1s ease-in-out;
    box-shadow: 0 0 10px rgba(16, 185, 129, 0.8);
}

.progress-stats {
    font-size: 1.1rem;
    font-weight: 500;
}

.progress-lists {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 30px;
}

@media (max-width: 768px) {
    .progress-lists {
        grid-template-columns: 1fr;
    }
}

.list-section {
    background: white;
    padding: 20px;
    border-radius: 12px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
    border: 1px solid #e5e7eb;
}

body.dark-theme .list-section {
    background: #1f2937;
    border-color: #374151;
}

.list-section h3 {
    margin-top: 0;
    font-size: 1.3rem;
    border-bottom: 2px solid #f3f4f6;
    padding-bottom: 10px;
    margin-bottom: 15px;
}

body.dark-theme .list-section h3 {
    border-color: #374151;
}

.chapter-list {
    list-style: none;
    padding: 0;
    margin: 0;
    max-height: 400px;
    overflow-y: auto;
}

.chapter-list li {
    margin-bottom: 10px;
}

.chapter-list a {
    display: block;
    padding: 10px 15px;
    background: #f9fafb;
    border-radius: 8px;
    color: #374151;
    text-decoration: none;
    transition: all 0.2s;
    font-weight: 500;
}

body.dark-theme .chapter-list a {
    background: #374151;
    color: #d1d5db;
}

.chapter-list a:hover {
    background: #eff6ff;
    color: #2563eb;
    transform: translateX(5px);
}

body.dark-theme .chapter-list a:hover {
    background: #1e3a8a;
    color: #93c5fd;
}
</style>

<div class="progress-dashboard">
  <div class="progress-header">
    <h2>Your Study Progress</h2>
    <div class="progress-bar-container">
      <div class="progress-bar-fill" id="progress-bar-fill" style="width: 0%;"></div>
    </div>
    <div class="progress-stats" id="progress-stats">Loading your progress...</div>
  </div>

  <div class="progress-lists">
    <div class="list-section">
      <h3 style="color: #ef4444;"><i class="fa fa-book"></i> Up Next (Unread)</h3>
      <ul id="unread-list" class="chapter-list"></ul>
    </div>
    <div class="list-section">
      <h3 style="color: #10b981;"><i class="fa fa-check-circle"></i> Completed</h3>
      <ul id="completed-list" class="chapter-list"></ul>
    </div>
  </div>
</div>

<script>
  // Mengambil seluruh chapter yang bukan frontmatter atau backmatter
  const allChaptersRaw = [
    {% for chapter in site.chapters %}
      {% if chapter.id contains '000-front' or chapter.id contains '999-back' %}
        {% continue %}
      {% endif %}
      {
        "title": {{ chapter.title | jsonify }},
        "url": {{ chapter.url | relative_url | jsonify }},
        "slug": {{ chapter.slug | jsonify }}
      },
    {% endfor %}
    null // untuk handle koma terakhir di loop
  ];

  document.addEventListener("DOMContentLoaded", () => {
      const validChapters = allChaptersRaw.filter(c => c !== null && c.slug);
      
      const completed = [];
      const unread = [];

      validChapters.forEach(chapter => {
          if (localStorage.getItem('chapter_read_' + chapter.slug) === 'true') {
              completed.push(chapter);
          } else {
              unread.push(chapter);
          }
      });

      const total = validChapters.length;
      const readCount = completed.length;
      const percentage = total === 0 ? 0 : Math.round((readCount / total) * 100);

      // Animate progress bar
      setTimeout(() => {
          document.getElementById('progress-bar-fill').style.width = percentage + '%';
      }, 300);
      
      document.getElementById('progress-stats').innerText = `${readCount} of ${total} chapters completed (${percentage}%)`;

      const unreadList = document.getElementById('unread-list');
      const completedList = document.getElementById('completed-list');

      unreadList.innerHTML = unread.length ? '' : '<li style="padding: 10px; color: #10b981;">You have completed everything! 🎉</li>';
      completedList.innerHTML = completed.length ? '' : '<li style="padding: 10px; color: #6b7280;">You have not completed any chapters yet. Start reading!</li>';

      unread.forEach(chapter => {
          const li = document.createElement('li');
          li.innerHTML = `<a href="${chapter.url}">${chapter.title}</a>`;
          unreadList.appendChild(li);
      });

      completed.forEach(chapter => {
          const li = document.createElement('li');
          li.innerHTML = `<a href="${chapter.url}"><i class="fa fa-check" style="color: #10b981; margin-right: 8px;"></i>${chapter.title}</a>`;
          completedList.appendChild(li);
      });
  });
</script>
