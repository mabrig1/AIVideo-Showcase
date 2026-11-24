# AIVideo | Engineering Portfolio

**AI filmmaking system design · Multimedia workflow engineering · MABRIG Technologies**

AIVideo is a project focused on cinematic planning and AI-assisted video workflows. This portfolio demonstrates relevant engineering design principles without disclosing production internals.

[Product website](https://aivideo.mabrigkorie.org) · [Developer profile](https://github.com/mabrig1) · [Contact](https://www.mabrigkorie.org)

## Explore the portfolio

- [Conceptual architecture](docs/architecture.md)
- [Engineering case study](docs/case-study.md)
- [Interactive storyboard planner](demo/index.html) — download and open locally in a browser.
- [Independent Python timeline implementation](demo/timeline.py)
- [Automated tests](demo/test_timeline.py)
- [CI workflow](.github/workflows/demo.yml)

## Demonstrated competencies

Scene timing, input validation, deterministic timeline construction, asynchronous media pipeline design, human approval boundaries and cost-aware provider orchestration concepts.

## Run locally

```sh
python demo/timeline.py
python -m unittest discover -s demo -v
```

Python 3.10+; no external dependencies or API keys required. The examples are independently authored for this showcase. They plan timelines but do not generate video, invoke AI models or spend provider credits. Live production functionality and performance have not been independently verified here.

## Intellectual property and technical review

See [NOTICE.md](NOTICE.md). Production source, proprietary prompts, credentials and internal model routing are excluded. Recruiters can contact MABRIG Technologies for a guided demonstration or scoped technical discussion.
