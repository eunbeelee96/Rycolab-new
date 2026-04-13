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
          <img src="uploads/teamphoto.jpeg" alt="Team Photo" class="hero-image">
          <div class="hero-content">
            <p class="lab-intro">
              We are a collocation of collaborators working on a diverse range of topics in <em class="hero-highlight">computational linguistics</em>, <em class="hero-highlight">natural language processing</em> and <em class="hero-highlight">machine learning</em>.
            </p>
            <div class="research-topics-section">
              <div class="research-topics-header">
                <span class="research-topics-label-text">RESEARCH AREAS</span>
                <div class="research-topics-line"></div>
              </div>
              <div class="research-topics">
                <a class="research-topic" href="/publications/?topic=Parsing">Parsing</a>
                <a class="research-topic" href="/publications/?topic=Morphology">Morphology</a>
                <a class="research-topic" href="/publications/?topic=Formal Languages">Formal Languages</a>
                <a class="research-topic" href="/publications/?topic=Information Theory">Information Theory</a>
                <a class="research-topic" href="/publications/?topic=Language Modeling">Language Modeling</a>
                <a class="research-topic" href="/publications/?topic=Typology">Typology</a>
                <a class="research-topic" href="/publications/?topic=Alignment">Alignment</a>
                <a class="research-topic" href="/publications/?topic=Bias %26 Fairness">Bias &amp; Fairness</a>
                <a class="research-topic" href="/publications/?topic=Psycholinguistics">Psycholinguistics</a>
                <a class="research-topic" href="/publications/?topic=Decoding">Decoding</a>
                <a class="research-topic" href="/publications/?topic=Tokenization">Tokenization</a>
                <a class="research-topic" href="/publications/?topic=Legal NLP">Legal NLP</a>
                <a class="research-topic" href="/publications/?topic=Probing">Probing</a>
                <a class="research-topic" href="/publications/?topic=Translation">Translation</a>
                <a class="research-topic" href="/publications/?topic=Ethics">Ethics</a>
                <a class="research-topic" href="/publications/?topic=Syntax">Syntax</a>
              </div>
            </div>
          </div>
        </div>
  - block: markdown
    content:
      title: ''
      subtitle: ''
      text: |-
        {{< latest-news >}}
        <!-- NOTE: This footer is duplicated in layouts/partials/rycolab-footer.html.
             HugoBlox RenderString does not support shortcodes so the partial
             cannot be called here. Edit both files when changing footer content.
             Footer styles: layouts/_partials/hooks/head-end/main.html SECTION 7. -->
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
    design:
      css_class: updates-section
---
