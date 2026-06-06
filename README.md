# constitutional-ai-mini
<p align="center">
  <img src="./results/figures/_hero.png" alt="constitutional-ai-mini hero" width="100%"/>
</p>

<p align="center">
  <img alt="tests" src="https://img.shields.io/badge/tests-green-brightgreen?style=for-the-badge">
  <img alt="mypy" src="https://img.shields.io/badge/mypy-strict-blue?style=for-the-badge">
  <img alt="lint" src="https://img.shields.io/badge/ruff-clean-orange?style=for-the-badge">
  <img alt="pdf" src="https://img.shields.io/badge/research-15--page%20pdf-purple?style=for-the-badge">
  <img alt="license" src="https://img.shields.io/badge/license-MIT-lightgrey?style=for-the-badge">
</p>

> **Constitutional-AI critique-and-revise loop with per-principle violation tracking and revised-vs-original judge council.**



> A tiny constitutional-AI pipeline: a critique-and-revise loop over a small instruction set, with per-principle violation tracking and a revised-vs-original win-rate plot.
> Last updated: 2025-05-25.

`constitutional-ai-mini` is a minimal reference implementation of the Anthropic Constitutional-AI (CAI) loop: a draft response is critiqued against a small constitution, the reviser redacts violating spans, and a judge compares pre- vs post-revision against the same constitution. The harness reports per-principle violation rates, the revised-vs-original win-rate, the per-revision margin, and the pre vs post violation count.

## Headline

| metric | value |
|---|---|
| instructions | 6 |
| pre-revision violations | reported at runtime |
| post-revision violations | reported at runtime |
| revised-wins (judge majority) | reported at runtime |

Reproduce: `make install && make bench`.

## Pipeline

```mermaid
flowchart LR
  A[6 instructions] --> B[Draft helper response]
  B --> C[Critic: scan against constitution]
  C --> D[Reviser: redact violations]
  D --> E[Judge: compare original vs revised]
  E --> F[5 chart families + summary.json]
```

## Five chart families

- `results/figures/violation_rate_pre.png` - per-principle violation rate, pre-revision
- `results/figures/winrate.png` - revised-vs-original judge pie
- `results/figures/margin.png` - revision margin histogram
- `results/figures/pre_post.png` - total violations before vs after
- `results/figures/heatmap.png` - per-(instruction, principle) violation heatmap, pre vs post

## Repo layout

```
src/caimini/
  types.py              # Principle, Instruction, Response, Critique, Revision, JudgeResult
  principles/library.py # 3-principle constitution
  prompts/instructions.py
  critic/checker.py
  reviser/rewriter.py
  judge/winrate.py
  viz/charts.py
  cli/main.py
  runner.py
tests/                  # tests, all green
docs/research_report.pdf
docs/_report/, docs/test_results/, results/figures/
CITATION.cff, LICENSE, Makefile, .github/workflows/ci.yml
```

## Quick start

```bash
make install
make test
make bench
make pdf
```

## Documentation

[`docs/research_report.pdf`](./docs/research_report.pdf) (15 pages).
Test artifacts in [`docs/test_results/`](./docs/test_results/).

## References

- Bai, Y., Kadavath, S., Kundu, S., et al. "Constitutional AI: Harmlessness from AI Feedback" (Anthropic, 2022)
- Lee, H., Phatale, S., et al. "RLAIF: Scaling Reinforcement Learning from Human Feedback with AI Feedback" (Google, 2023)

## License

MIT.

## Architecture

```mermaid
flowchart LR
    classDef io fill:#9C2C2C,stroke:#1c1c1c,stroke-width:1.5px,color:#fff
    classDef proc fill:#1D1A05,stroke:#1c1c1c,stroke-width:1.5px,color:#fff
    classDef out fill:#A8956E,stroke:#1c1c1c,stroke-width:1.5px,color:#fff
    A["📥 Inputs<br/>fixtures + configs"]:::io --> B["⚙️ Core pipeline<br/>constitutional"]:::proc
    B --> C["🧪 Evaluation<br/>5 chart families"]:::proc
    C --> D["📊 Artifacts<br/>summary.json + PNGs"]:::out
    C --> E["📄 PDF report<br/>15 pages"]:::out
```

## Pipeline sequence

```mermaid
sequenceDiagram
    autonumber
    participant U as User / CI
    participant M as Makefile
    participant R as Runner
    participant V as Viz
    participant P as PDF
    U->>M: make bench
    M->>R: invoke runner with seeded config
    R-->>R: load fixture + execute task
    R->>V: emit per-(metric, slice) records
    V-->>V: render 5 distinct chart families
    V->>U: write summary.json + PNG artifacts
    U->>M: make pdf
    M->>P: pandoc + xelatex
    P->>U: docs/research_report.pdf
```

## Concept mindmap

```mermaid
mindmap
  root((constitutional))
    Inputs
      Fixture
      Seed
      Config
    Core
      Modules
      Tests
      Mypy strict
    Outputs
      5 chart families
      summary json
      15-page PDF
    Quality
      Ruff
      Coverage
      CI on push
```


## Results gallery

<table>
  <tr>
    <td align="center"><strong>Pytest panel</strong><br/><img src="./docs/test_results/pytest_panel.png" width="100%"/></td>
    <td align="center"><strong>Coverage donut</strong><br/><img src="./docs/test_results/coverage_donut.png" width="100%"/></td>
  </tr>
  <tr>
    <td align="center"><strong>Quality gates</strong><br/><img src="./docs/test_results/quality_gates.png" width="100%"/></td>
    <td align="center"><strong>Headline metrics</strong><br/><img src="./docs/test_results/metrics_card.png" width="100%"/></td>
  </tr>
</table>

### Result charts (5 distinct families, palette: *Charter Stamp*)

<table>
  <tr><td align="center"><strong>Heatmap</strong><br/><img src="./results/figures/heatmap.png" width="100%"/></td><td align="center"><strong>Margin</strong><br/><img src="./results/figures/margin.png" width="100%"/></td></tr>
  <tr><td align="center"><strong>Pre Post</strong><br/><img src="./results/figures/pre_post.png" width="100%"/></td><td align="center"><strong>Violation Rate Pre</strong><br/><img src="./results/figures/violation_rate_pre.png" width="100%"/></td></tr>
  <tr><td align="center"><strong>Winrate</strong><br/><img src="./results/figures/winrate.png" width="100%"/></td><td></td></tr>
</table>

