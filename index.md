---
layout: home
title: Dylan Zhou — Data Engineer
---

<!-- HERO -->
<div class="hero">
  <div class="hero-avatar">DZ</div>
  <h1>Dylan Zhou</h1>
  <p class="hero-sub">
    Aspiring Data Engineer with expertise in Big Data pipelines and Real-time AI,
    seeking to leverage data-driven solutions for impactful business outcomes.
  </p>
  <div class="hero-tags">
    <span class="hero-tag">Data Engineering</span>
    <span class="hero-tag">Big Data</span>
    <span class="hero-tag">Python</span>
    <span class="hero-tag">SQL</span>
    <span class="hero-tag">PySpark</span>
    <span class="hero-tag">YOLOv8</span>
    <span class="hero-tag">Computer Vision</span>
  </div>
</div>

<!-- ABOUT -->
<div class="section">
  <h2 class="section-title"><span class="num">01</span> About Me</h2>
  <div class="about-text">
    I am a <strong>Master of Science in Data Science</strong> student at Lingnan University, expected to graduate in <strong>August 2026</strong>. With a solid background in full-stack software development (Java / Vue), I specialize in bridging the gap between robust backend architecture and advanced data analytics. My focus lies in building scalable data infrastructures and deploying high-performance machine learning models in production environments. I am a proactive problem solver with a passion for optimizing distributed systems and real-time computer vision applications.
  </div>
</div>

<!-- SKILLS -->
<div class="section">
  <h2 class="section-title"><span class="num">02</span> Skills</h2>
  <div class="skills-grid">

    <div class="skill-card">
      <h3><i class="fas fa-code"></i> Programming</h3>
      <ul>
        <li>Python</li>
        <li>SQL</li>
        <li>Java (Spring Boot)</li>
        <li>JavaScript / Vue</li>
      </ul>
    </div>

    <div class="skill-card">
      <h3><i class="fas fa-chart-line"></i> Data & ML</h3>
      <ul>
        <li>PySpark</li>
        <li>PyTorch</li>
        <li>Transformers (BERT / FinBERT)</li>
        <li>Pandas, Scikit-learn</li>
      </ul>
    </div>

    <div class="skill-card">
      <h3><i class="fas fa-brain"></i> Specializations</h3>
      <ul>
        <li>Natural Language Processing</li>
        <li>Computer Vision</li>
        <li>Distributed Computing</li>
        <li>Statistics & A/B Testing</li>
      </ul>
    </div>

    <div class="skill-card">
      <h3><i class="fas fa-toolbox"></i> Tools</h3>
      <ul>
        <li>Tableau, Matplotlib</li>
        <li>Docker, Git</li>
        <li>IntelliJ IDEA, PyCharm</li>
        <li>YOLOv8, BiLSTM + Attention</li>
      </ul>
    </div>

  </div>
</div>

<!-- PROJECTS -->
<div class="section">
  <h2 class="section-title"><span class="num">03</span> Projects</h2>

  <div class="project-card">
    <h3><i class="fas fa-chart-bar" style="color: var(--primary); font-size: 0.9em;"></i> Financial News Sentiment Analysis</h3>
    <span class="project-year">2026 — Group Project</span>
    <p>Automated financial news sentiment analysis to assist investment decision-making by classifying headlines as Positive, Neutral, or Negative — addressing severe class imbalance (Negative at only 12.5%).</p>
    <ul>
      <li><strong>Data:</strong> Financial Phrasebank — 4,846 professionally annotated English sentences</li>
      <li><strong>Approach:</strong> BiLSTM + Attention (class-weighted CrossEntropyLoss + Label Smoothing) vs. fine-tuned FinBERT baseline</li>
      <li><strong>Key insight:</strong> Imbalance handled via <code>w_c = sqrt(N / (C × N_c))</code>; Label Smoothing regularizes small-domain data</li>
      <li><strong>Result:</strong> BiLSTM + Label Smoothing achieved <strong>89.0% accuracy</strong>, outperforming FinBERT (87.8%)</li>
      <li><strong>Contribution:</strong> Led experimental design, implemented the BiLSTM + Attention architecture, built all visualizations and the final academic report</li>
    </ul>
    <a class="project-link" href="https://github.com/MrMister1218/CDS525-SentimentAnalysis" target="_blank">
      <i class="fab fa-github"></i> View on GitHub
    </a>
  </div>

  <div class="project-card">
    <h3><i class="fas fa-car" style="color: var(--primary); font-size: 0.9em;"></i> Real-time License Plate Recognition</h3>
    <span class="project-year">2026</span>
    <p>High-speed vehicle identification system for smart parking management — automating entry/exit tracking with real-time computer vision.</p>
    <ul>
      <li><strong>Approach:</strong> Real-time object detection pipeline using YOLOv8, optimized for low-latency inference</li>
      <li><strong>Hardware:</strong> RTX 4080 environment configuration for accelerated training and inference</li>
      <li><strong>Result:</strong> <strong>95%+ detection accuracy</strong> across diverse lighting conditions</li>
      <li><strong>Contribution:</strong> End-to-end model training, environment setup, and backend integration</li>
    </ul>
    <a class="project-link" href="https://github.com/yiplm/automatic-license-plate-recognition" target="_blank">
      <i class="fab fa-github"></i> View on GitHub
    </a>
  </div>
</div>

<!-- RESUME -->
<div class="section">
  <h2 class="section-title"><span class="num">04</span> Resume</h2>
  <div class="resume-block">
    <p>Interested in my full background? Download my resume for a complete overview.</p>
    <a class="resume-btn" href="./Resume_Dylan.pdf" target="_blank">
      <i class="fas fa-file-pdf"></i> Download Resume (PDF)
    </a>
  </div>
</div>

<!-- CONTACT -->
<div class="section">
  <h2 class="section-title"><span class="num">05</span> Contact</h2>
  <div class="contact-grid">

    <a class="contact-card" href="mailto:chouyuhsiang1218@gmail.com">
      <div class="contact-icon email"><i class="fas fa-envelope"></i></div>
      <div class="contact-info">
        <div class="label">Email</div>
        <div class="value">chouyuhsiang1218@gmail.com</div>
      </div>
    </a>

    <a class="contact-card" href="https://github.com/MrMister1218" target="_blank">
      <div class="contact-icon github"><i class="fab fa-github"></i></div>
      <div class="contact-info">
        <div class="label">GitHub</div>
        <div class="value">@MrMister1218</div>
      </div>
    </a>

    <a class="contact-card" href="#">
      <div class="contact-icon linkedin"><i class="fab fa-linkedin-in"></i></div>
      <div class="contact-info">
        <div class="label">LinkedIn</div>
        <div class="value">Dylan Zhou</div>
      </div>
    </a>

  </div>
</div>

<footer class="page-footer">
  Designed &amp; built by <strong>Dylan Zhou</strong> · {{ site.time | date: '%Y' }} · Powered by GitHub Pages
</footer>
