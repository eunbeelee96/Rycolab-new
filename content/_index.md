---
# Leave the homepage title empty to use the site title
title: ''
date: 2022-10-24
type: landing

design:
  spacing: '6 rem'

sections:
  - block: markdown
    content:
      title: ''
      subtitle: ''
      text: |-
        <div class="hero-section">
          <img src="{{ .Site.BaseURL }}uploads/teamphoto.png" alt="Team Photo" class="hero-image">
          <div class="hero-content">
            <p class="lab-intro">
            We are a collocation of collaborators working on a <br>diverse range of topics in computational linguistics, natural language processing and machine learning.
            </p>
            <div class="research-topics-section">
              <div class="research-topics">
                <span class="research-topic">Information Theory</span>
                <span class="research-topic">Computational Typology and Morphology</span>
                <span class="research-topic">Algorithms for Parsing</span>
                <span class="research-topic">Formal Aspects of Language Modeling</span>
                <span class="research-topic">Cognitive and (Psycho-) Linguistics</span>
                <span class="research-topic">Bias and Fairness in NLP Systems</span>
                <span class="research-topic">Interpreting Neural Representations of Language</span>
                <span class="research-topic">Computational Social Science</span>
              </div>
            </div>
          </div>
        </div>
  - block: markdown
    content:
      title: ''
      subtitle: ''
      text: |-
        <div style="width: fit-content;">
          <div class="updates-label">LATEST NEWS</div>
        </div>
        <div class="updates-grid">
          <div class="update-card" data-type="papers">PAPERS</div>
          <div class="update-card" data-type="conferences">CONFERENCES</div>
          <div class="update-card" data-type="grants">GRANTS</div>
          <div class="update-card" data-type="people">PEOPLE</div>
          <div class="update-card" data-type="talks">TALKS</div>
        </div>
        <footer class="site-footer">
          <div class="footer-content">
            <div class="footer-group">
              <a href="https://ml.inf.ethz.ch/">Institute for Machine Learning</a>
              <a href="https://inf.ethz.ch/">Department of Computer Science, ETH Zürich</a>
            </div>
            <a href="mailto:contact-rycolab@lists.inf.ethz.ch">contact-rycolab@lists.inf.ethz.ch</a>
            <p>Andreasstrasse 5, 8050 Zürich, Switzerland</p>
          </div>
        </footer>
---
