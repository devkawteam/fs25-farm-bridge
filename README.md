# fs25-farm-bridge

Links Farming Simulator 25 server data to an external website via Base44.

## Usage

Install the package:

```bash
python -m pip install .
```

1. Set the `BASE44_API_URL` secret / environment variable to your Base44 API endpoint (example):

```bash
export BASE44_API_URL="https://rough-farm-flow-hub.base44.app/api/functions/farmIntelligenceIngest"
```

2. (Optional) Set the `BASE44_API_KEY` secret / environment variable if your endpoint requires it:

```bash
export BASE44_API_KEY="007ff83f5dea4651a7960eb736b6e86c"
```

3. Run:

```bash
python -m fs25_farm_bridge
```

Or, once installed, run:

```bash
fs25-farm-bridge
```

## GitHub Actions

This repository includes a GitHub Actions workflow that runs every 5 minutes (`.github/workflows/farmsim-bridge.yml`).

### Publishing releases

Pushing a version tag (e.g. `v0.1.0`) will trigger workflows that:

- Build & publish a wheel to **GitHub Packages** (via `.github/workflows/publish.yml`)
- Create a **GitHub Release** and attach the wheel (via `.github/workflows/release.yml`)

```bash
git tag v0.1.0
git push origin v0.1.0
```
