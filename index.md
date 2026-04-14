---
layout: home
title: Dylan Zhou — Data Engineer
---

<!-- HERO -->
<div class="hero">
  <div class="hero-avatar">DZ</div>
  <div class="hero-status">Open to Work</div>
  <h1>Dylan Zhou</h1>
  <p class="hero-sub">
    Aspiring Data Engineer specializing in Big Data pipelines, Real-time AI,
    and scalable ML systems — bridging robust backend architecture with
    advanced data analytics.
  </p>
  <div class="hero-tags">
    <span class="hero-tag">Data Engineering</span>
    <span class="hero-tag">PySpark</span>
    <span class="hero-tag">Python</span>
    <span class="hero-tag">SQL</span>
    <span class="hero-tag">Computer Vision</span>
    <span class="hero-tag">NLP</span>
    <span class="hero-tag">YOLOv8</span>
    <span class="hero-tag">XGBoost</span>
  </div>
</div>

<!-- ABOUT -->
<div class="section">
  <h2 class="section-title" data-num="01">About Me</h2>
  <div class="glass about-text">
    I am a <strong>Master of Science in Data Science</strong> student at Lingnan University, expected to graduate in <strong>August 2026</strong>. With a solid background in full-stack software development (Java / Vue), I specialize in bridging the gap between robust backend architecture and advanced data analytics. My focus lies in building scalable data infrastructures and deploying high-performance machine learning models in production environments. I am a proactive problem solver with a passion for optimizing distributed systems and real-time computer vision applications.
    <br><br>
    I am proficient in <strong>prompt engineering</strong>, skilled in <strong>vibe coding</strong>, and highly experienced with <strong>Claude Code</strong> and a wide range of its skills — enabling rapid prototyping and end-to-end development across the full stack.
  </div>
</div>

<!-- SKILLS -->
<div class="section">
  <h2 class="section-title" data-num="02">Skills</h2>
  <div class="skills-grid">

    <div class="glass skill-card">
      <h3><i class="fas fa-code"></i> Programming</h3>
      <ul>
        <li><span class="skill-dot"></span>Python</li>
        <li><span class="skill-dot"></span>SQL</li>
        <li><span class="skill-dot"></span>Java (Spring Boot)</li>
        <li><span class="skill-dot"></span>JavaScript / Vue</li>
      </ul>
    </div>

    <div class="glass skill-card">
      <h3><i class="fas fa-chart-line"></i> Data &amp; ML</h3>
      <ul>
        <li><span class="skill-dot"></span>PySpark</li>
        <li><span class="skill-dot"></span>PyTorch</li>
        <li><span class="skill-dot"></span>Transformers (BERT / FinBERT)</li>
        <li><span class="skill-dot"></span>Pandas, Scikit-learn</li>
      </ul>
    </div>

    <div class="glass skill-card">
      <h3><i class="fas fa-brain"></i> Specializations</h3>
      <ul>
        <li><span class="skill-dot"></span>Natural Language Processing</li>
        <li><span class="skill-dot"></span>Computer Vision</li>
        <li><span class="skill-dot"></span>Distributed Computing</li>
        <li><span class="skill-dot"></span>Statistics &amp; A/B Testing</li>
      </ul>
    </div>

    <div class="glass skill-card">
      <h3><i class="fas fa-toolbox"></i> Tools</h3>
      <ul>
        <li><span class="skill-dot"></span>Tableau, Matplotlib</li>
        <li><span class="skill-dot"></span>Docker, Git</li>
        <li><span class="skill-dot"></span>IntelliJ IDEA, PyCharm</li>
        <li><span class="skill-dot"></span>YOLOv8, BiLSTM + Attention</li>
      </ul>
    </div>

  </div>
</div>

<!-- PROJECTS -->
<div class="section">
  <h2 class="section-title" data-num="03">Projects</h2>

  <div class="glass project-card">
    <h3><i class="fas fa-chart-bar" style="color: var(--primary);"></i> Financial News Sentiment Analysis</h3>
    <span class="project-year">Feb 2026 – Apr 2026</span>
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

  <div class="glass project-card">
    <h3><i class="fas fa-house" style="color: var(--primary);"></i> House Price Prediction with Machine Learning Ensemble</h3>
    <span class="project-year">Feb 2026 – Apr 2026</span>
    <p>Predicted residential house sale prices to assist real estate valuation and investment decision-making, addressing the need for accurate, data-driven pricing in the housing market.</p>
    <ul>
      <li><strong>Data:</strong> Kaggle Ames Housing dataset — 1,460 training samples, 81 raw features including physical attributes (area, year built, quality ratings) and categorical variables (zoning, neighborhood, sale condition)</li>
      <li><strong>Approach:</strong> Built a supervised ML pipeline covering data preprocessing (StandardScaler, OneHotEncoder, SimpleImputer), feature engineering (PropertyAge, TotalSF, TotalBath), PCA dimensionality reduction, and hyperparameter tuning via 3-fold GridSearchCV across Linear Regression, Random Forest, XGBoost (GPU-accelerated via CUDA), and MLP neural network; evaluated individual models, average ensemble, and stacking ensemble (XGBoost as meta-learner)</li>
      <li><strong>Outcome:</strong> XGBoost achieved the best individual RMSE of <strong>0.138</strong> on test data; stacking ensemble further improved prediction accuracy; Kaggle submission RMSE: <strong>0.134</strong></li>
    </ul>
    <a class="project-link" href="https://github.com/MrMister1218/ML-House_Price_Predict" target="_blank">
      <i class="fab fa-github"></i> View on GitHub
    </a>
  </div>

  <div class="glass project-card">
    <h3><i class="fas fa-car" style="color: var(--primary);"></i> Real-Time License Plate Recognition System (ALPR)</h3>
    <span class="project-year">Feb 2026 – Apr 2026</span>
    <p>Global vehicle population growth has created urgent demand for automated traffic management. This project developed a deep learning-based ALPR system to automatically detect and recognize license plates from images and video streams in real time.</p>
    <ul>
      <li><strong>Data:</strong> COCO pre-trained YOLOv8 for vehicle detection; Roboflow license plate dataset (~5,000 images, YOLO format) fine-tuned on Hong Kong plate formats — supporting English letters + digits including special and personalized plates</li>
      <li><strong>Approach:</strong> Two-stage cascade detection: YOLOv8 (COCO) → YOLOv8 (fine-tuned) for plate localization; EasyOCR CRNN (CNN + LSTM + CTC Loss) for OCR; 4-step preprocessing pipeline: 2.5× super-resolution → grayscale → bilateral filtering → Otsu binarization; track-by-position + OCR frequency voting for temporal stability</li>
      <li><strong>Outcome:</strong> Built a complete Streamlit Web app with four input modes (image upload, photo capture, video upload, WebRTC live camera); static image recognition achieved 95–100% accuracy; structured CSV export for downstream traffic management systems; modular architecture enables independent module upgrades</li>
      <li><strong>Contribution:</strong> Led the design and implementation of the Streamlit Web front-end including WebRTC live streaming and real-time result display; fine-tuned YOLOv8 via transfer learning with optimized confidence thresholds and NMS parameters; performed dataset annotation and quality review; designed Hong Kong plate format validation rules and position-aware character correction heuristics; integrated all modules into an end-to-end pipeline</li>
    </ul>
    <a class="project-link" href="https://github.com/yiplm/automatic-license-plate-recognition" target="_blank">
      <i class="fab fa-github"></i> View on GitHub
    </a>
  </div>
</div>

<!-- RESUME -->
<div class="section">
  <h2 class="section-title" data-num="04">Resume</h2>
  <div class="resume-block">
    <p>Interested in my full background? Download my resume for a complete overview.</p>
    <a class="resume-btn" href="./Resume_Dylan.pdf" target="_blank">
      <i class="fas fa-file-pdf"></i> Download Resume (PDF)
    </a>
  </div>
</div>

<!-- CONTACT -->
<div class="section">
  <h2 class="section-title" data-num="05">Contact</h2>
  <div class="contact-grid">

    <a class="glass contact-card" href="mailto:chouyuhsiang1218@gmail.com">
      <div class="contact-icon email"><i class="fas fa-envelope"></i></div>
      <div class="contact-info">
        <div class="label">Email</div>
        <div class="value">chouyuhsiang1218@gmail.com</div>
      </div>
    </a>

    <a class="glass contact-card" href="https://github.com/MrMister1218" target="_blank">
      <div class="contact-icon github"><i class="fab fa-github"></i></div>
      <div class="contact-info">
        <div class="label">GitHub</div>
        <div class="value">@MrMister1218</div>
      </div>
    </a>

    <a class="glass contact-card" href="#">
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
