---
layout: post
title: "MetaDiffuser: Diffusion Model as Conditional Planner for Offline Meta-RL"
date: 2023-08-01 21:53:35
auth: "Fei Ni"
internal: true
contain_poster: true
poster: /assets/image/research/metadiffuer.png
excerpt: Recently, diffusion model shines as a promising backbone for the sequence modeling paradigm in offline reinforcement learning. However, these works mostly lack the generalization ability across tasks with reward or dynamics change. To tackle this challenge, in this paper we propose a task-oriented conditioned diffusion planner for offline meta-RL(MetaDiffuser), which considers the generalization problem as conditional trajectory generation task with contextual representation. The key is to learn a context conditioned diffusion model which can generate task-oriented trajectories for planning across diverse tasks. To enhance the dynamics consistency of the generated trajectories while encouraging trajectories to achieve high returns, we further design a dual-guided module in the sampling process of the diffusion model. The proposed framework enjoys the robustness to the quality of collected warm-start data from the testing task and the flexibility to incorporate with different task representation method. The experiment results on MuJoCo benchmarks show that MetaDiffuser outperforms other strong offline meta-RL baselines, demonstrating the outstanding conditional generation ability of diffusion architecture.
links:
  - name: PDF
    icon: picture_as_pdf
    link: http://proceedings.mlr.press/v202/ni23a/ni23a.pdf
  - name: Site
    icon: github
    link: https://metadiffuser.github.io
---

<script>
    window.addEventListener('load', function() {
        window.location.href = 'https://metadiffuser.github.io/';
    });
</script>